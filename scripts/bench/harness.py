#!/usr/bin/env python3
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""Prototype benchmark harness for stock Chromium-based browsers (ENG-031, issue #71).

It measures, per browser and tab count:

- startup: launch -> first contentful paint of the first tab (ms)
- all_loaded: launch -> load event of every tab (ms)
- memory: summed private bytes (Windows) or PSS (Linux) of all browser processes
  after a settle period (MiB), plus the process count
- idle CPU: CPU time used by all browser processes during an idle window,
  as a percentage of one logical core

Pages come from a small synthetic corpus generated at run time and served on
127.0.0.1 only. Each run uses a fresh temporary profile, which is deleted
afterwards. Browsers run with their default settings: no sandbox or security
flag is ever changed (docs/benchmarks/BENCHMARKS.md, section 10).

This is a prototype for validating the methodology. Its numbers are not
Brumel results and must not be published as such.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import random
import shutil
import statistics
import subprocess
import sys
import tempfile
import threading
import time
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

CORPUS_VERSION = "synthetic-1"
IS_WINDOWS = sys.platform == "win32"
KNOWN_BROWSERS = {
    "win32": {
        "chrome": [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                   r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"],
        "edge": [r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                 r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"],
        "brave": [r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
                  r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\Application\brave.exe"],
    },
    "linux": {
        "chrome": ["google-chrome", "google-chrome-stable"],
        "chromium": ["chromium", "chromium-browser"],
        "edge": ["microsoft-edge", "microsoft-edge-stable"],
        "brave": ["brave-browser", "brave"],
    },
}
# Only flags that skip first-run UI. Nothing that changes security or performance behavior.
LAUNCH_FLAGS = ["--no-first-run", "--no-default-browser-check"]


# --------------------------------------------------------------------------- #
# Corpus
# --------------------------------------------------------------------------- #

BEACON_JS = """
<script>
(function () {
  const tab = new URLSearchParams(location.search).get("tab") || "0";
  function send(kind, value) {
    navigator.sendBeacon("/beacon", JSON.stringify(
      {tab: tab, kind: kind, value: value, timeOrigin: performance.timeOrigin}));
  }
  new PerformanceObserver(function (list) {
    for (const e of list.getEntries()) {
      if (e.name === "first-contentful-paint") send("fcp", e.startTime);
    }
  }).observe({type: "paint", buffered: true});
  addEventListener("load", function () { send("load", performance.now()); });
})();
</script>
"""


def corpus_pages() -> dict[str, str]:
    """Synthetic, license-free pages with different costs (text, DOM, script, canvas, images)."""
    words = ("less noise more control browser memory privacy reliable fast local open source "
             "tabs pages history search window profile engine render layout paint").split()
    rng = random.Random(42)
    paragraph = lambda n: " ".join(rng.choice(words) for _ in range(n))  # noqa: E731
    article = "".join(f"<h2>{paragraph(4)}</h2><p>{paragraph(120)}</p>" for _ in range(40))
    table_rows = "".join(f"<tr>{''.join(f'<td>{rng.randint(0, 99999)}</td>' for _ in range(8))}</tr>"
                         for _ in range(1500))
    svgs = "".join(
        f'<svg width="160" height="120"><rect width="160" height="120" fill="#{rng.randint(0, 0xFFFFFF):06x}"/>'
        f'<circle cx="80" cy="60" r="{rng.randint(10, 55)}" fill="#{rng.randint(0, 0xFFFFFF):06x}"/></svg>'
        for _ in range(300))
    script_app = """
<div id="app"></div>
<script>
  const app = document.getElementById("app");
  const items = [];
  for (let i = 0; i < 20000; i++) items.push({id: i, label: "Item " + i, value: Math.sqrt(i)});
  const ul = document.createElement("ul");
  for (const item of items.slice(0, 3000)) {
    const li = document.createElement("li");
    li.textContent = item.label + " = " + item.value.toFixed(3);
    ul.appendChild(li);
  }
  app.appendChild(ul);
  window.__state = items;
</script>"""
    canvas = """
<canvas id="c" width="640" height="360"></canvas>
<script>
  const ctx = document.getElementById("c").getContext("2d");
  let t = 0;
  function frame() {
    ctx.fillStyle = "#11151C"; ctx.fillRect(0, 0, 640, 360);
    for (let i = 0; i < 200; i++) {
      ctx.fillStyle = "hsl(" + ((i * 7 + t) % 360) + ",60%,60%)";
      ctx.fillRect((i * 37 + t) % 640, (i * 53) % 360, 12, 12);
    }
    t++; requestAnimationFrame(frame);
  }
  frame();
</script>"""

    def page(title: str, body: str) -> str:
        return (f"<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><title>{title}</title>"
                f"{BEACON_JS}</head><body><h1>{title}</h1>{body}</body></html>")

    return {
        "article.html": page("Article", article),
        "table.html": page("Table", f"<table>{table_rows}</table>"),
        "images.html": page("Images", svgs),
        "app.html": page("Script app", script_app),
        "canvas.html": page("Canvas animation", canvas),
    }


def tab_urls(base: str, count: int) -> list[str]:
    names = sorted(corpus_pages())
    return [f"{base}/{names[i % len(names)]}?tab={i}" for i in range(count)]


# --------------------------------------------------------------------------- #
# Local server (127.0.0.1 only)
# --------------------------------------------------------------------------- #

class BeaconLog:
    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.events: list[dict] = []
        self.received = threading.Condition(self.lock)

    def add(self, event: dict) -> None:
        with self.received:
            event["server_time"] = time.time()
            self.events.append(event)
            self.received.notify_all()

    def reset(self) -> None:
        with self.lock:
            self.events = []

    def wait_until(self, predicate, timeout: float) -> bool:
        deadline = time.monotonic() + timeout
        with self.received:
            while not predicate(self.events):
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    return False
                self.received.wait(remaining)
        return True

    def wait_for_loads(self, count: int, timeout: float) -> bool:
        return self.wait_until(lambda events: len({e["tab"] for e in events if e.get("kind") == "load"}) >= count,
                               timeout)

    def wait_for_first_paint(self, timeout: float) -> bool:
        # Fast local pages can fire "load" before the first paint is reported.
        return self.wait_until(lambda events: any(e.get("kind") == "fcp" and e["tab"] == "0" for e in events),
                               timeout)

    def snapshot(self) -> list[dict]:
        with self.lock:
            return list(self.events)


def make_server(pages: dict[str, str], log: BeaconLog) -> ThreadingHTTPServer:
    encoded = {f"/{name}": body.encode("utf-8") for name, body in pages.items()}

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802
            body = encoded.get(urlparse(self.path).path)
            if body is None:
                self.send_error(404)
                return
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_POST(self) -> None:  # noqa: N802
            if urlparse(self.path).path != "/beacon":
                self.send_error(404)
                return
            length = min(int(self.headers.get("Content-Length", "0") or 0), 4096)
            try:
                data = json.loads(self.rfile.read(length) or b"{}")
                event = {"tab": str(data.get("tab")), "kind": str(data.get("kind")),
                         "value": float(data.get("value")), "time_origin": float(data.get("timeOrigin"))}
            except (ValueError, TypeError):
                self.send_error(400)
                return
            log.add(event)
            self.send_response(204)
            self.end_headers()

        def log_message(self, *args) -> None:
            pass

    return ThreadingHTTPServer(("127.0.0.1", 0), Handler)


# --------------------------------------------------------------------------- #
# Processes
# --------------------------------------------------------------------------- #

@dataclass
class ProcSample:
    pid: int
    memory_bytes: int      # Windows: private bytes; Linux: PSS
    cpu_seconds: float


def browser_processes(marker: str) -> list[ProcSample]:
    return _windows_processes(marker) if IS_WINDOWS else _linux_processes(marker)


def _windows_processes(marker: str) -> list[ProcSample]:
    escaped = marker.replace("'", "''")
    script = (
        "$ErrorActionPreference='SilentlyContinue';"
        f"$m='{escaped}';"
        "$out=@(Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -and $_.CommandLine.Contains($m) } |"
        " ForEach-Object { $p=Get-Process -Id $_.ProcessId; if ($p) {"
        " [pscustomobject]@{pid=$_.ProcessId; mem=$p.PrivateMemorySize64; cpu=$p.TotalProcessorTime.TotalSeconds} } });"
        "ConvertTo-Json -InputObject $out -Compress"
    )
    result = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-Command", script],
                            capture_output=True, text=True, timeout=60)
    return parse_windows_json(result.stdout)


def parse_windows_json(text: str) -> list[ProcSample]:
    text = text.strip()
    if not text:
        return []
    data = json.loads(text)
    if isinstance(data, dict):
        data = [data]
    return [ProcSample(int(d["pid"]), int(d.get("mem") or 0), float(d.get("cpu") or 0.0)) for d in data]


def _linux_processes(marker: str) -> list[ProcSample]:
    samples = []
    tick = os.sysconf("SC_CLK_TCK")
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit():
            continue
        try:
            cmdline = (entry / "cmdline").read_bytes().replace(b"\0", b" ").decode("utf-8", "replace")
            if marker not in cmdline:
                continue
            samples.append(ProcSample(int(entry.name), parse_pss((entry / "smaps_rollup").read_text()),
                                      parse_proc_stat_cpu((entry / "stat").read_text(), tick)))
        except (OSError, ValueError):
            continue
    return samples


def parse_pss(smaps_rollup: str) -> int:
    for line in smaps_rollup.splitlines():
        if line.startswith("Pss:"):
            return int(line.split()[1]) * 1024
    return 0


def parse_proc_stat_cpu(stat: str, tick: int) -> float:
    fields = stat[stat.rindex(")") + 2:].split()
    return (int(fields[11]) + int(fields[12])) / tick  # utime, stime


def terminate(marker: str, main: subprocess.Popen) -> None:
    try:
        main.terminate()
        main.wait(timeout=10)
    except (subprocess.TimeoutExpired, OSError):
        pass
    for sample in browser_processes(marker):
        try:
            if IS_WINDOWS:
                subprocess.run(["taskkill", "/PID", str(sample.pid), "/T", "/F"], capture_output=True)
            else:
                os.kill(sample.pid, 9)
        except OSError:
            pass


# --------------------------------------------------------------------------- #
# Statistics
# --------------------------------------------------------------------------- #

def summarize(values: list[float], seed: int = 1, resamples: int = 2000) -> dict:
    clean = [v for v in values if v is not None]
    if not clean:
        return {"n": 0}
    result = {"n": len(clean), "median": statistics.median(clean)}
    if len(clean) >= 2:
        q1, _, q3 = statistics.quantiles(clean, n=4, method="inclusive")
        result.update(q1=q1, q3=q3, iqr=q3 - q1)
        rng = random.Random(seed)
        medians = sorted(statistics.median(rng.choices(clean, k=len(clean))) for _ in range(resamples))
        result.update(ci95_low=medians[int(0.025 * resamples)], ci95_high=medians[int(0.975 * resamples) - 1])
    return result


# --------------------------------------------------------------------------- #
# Runs
# --------------------------------------------------------------------------- #

@dataclass
class RunConfig:
    browser: str
    executable: str
    tabs: int
    repetition: int


@dataclass
class RunResult:
    browser: str
    tabs: int
    repetition: int
    ok: bool
    error: str | None = None
    startup_ms: float | None = None
    all_loaded_ms: float | None = None
    memory_mib: float | None = None
    processes: int | None = None
    idle_cpu_pct: float | None = None
    memory_samples_mib: list[float] = field(default_factory=list)


def run_once(cfg: RunConfig, base_url: str, log: BeaconLog, settle: float, idle_window: float,
             load_timeout: float) -> RunResult:
    profile = Path(tempfile.mkdtemp(prefix="brumel-bench-"))
    marker = str(profile)
    result = RunResult(cfg.browser, cfg.tabs, cfg.repetition, ok=False)
    log.reset()
    argv = [cfg.executable, f"--user-data-dir={profile}", *LAUNCH_FLAGS, *tab_urls(base_url, cfg.tabs)]
    launch = time.time()
    proc = subprocess.Popen(argv, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        if not log.wait_for_loads(cfg.tabs, load_timeout):
            result.error = f"only {len({e['tab'] for e in log.snapshot() if e['kind'] == 'load'})} of {cfg.tabs} tabs loaded"
            return result
        log.wait_for_first_paint(timeout=10)
        events = log.snapshot()
        loads = [e["time_origin"] + e["value"] for e in events if e["kind"] == "load"]
        result.all_loaded_ms = (max(loads) / 1000 - launch) * 1000
        fcp = [e for e in events if e["kind"] == "fcp" and e["tab"] == "0"]
        if fcp:
            result.startup_ms = ((fcp[0]["time_origin"] + fcp[0]["value"]) / 1000 - launch) * 1000
        time.sleep(settle)
        for _ in range(3):
            samples = browser_processes(marker)
            result.memory_samples_mib.append(sum(s.memory_bytes for s in samples) / 2**20)
            result.processes = len(samples)
            time.sleep(2)
        result.memory_mib = statistics.median(result.memory_samples_mib)
        before = sum(s.cpu_seconds for s in browser_processes(marker))
        start = time.monotonic()
        time.sleep(idle_window)
        after = sum(s.cpu_seconds for s in browser_processes(marker))
        result.idle_cpu_pct = 100 * max(0.0, after - before) / (time.monotonic() - start)
        result.ok = True
        return result
    finally:
        terminate(marker, proc)
        shutil.rmtree(profile, ignore_errors=True)


def find_browsers(requested: list[str]) -> dict[str, str]:
    found: dict[str, str] = {}
    explicit = [r for r in requested if "=" in r]
    names = [r for r in requested if "=" not in r]
    for item in explicit:
        name, path = item.split("=", 1)
        found[name] = path
    known = KNOWN_BROWSERS.get("win32" if IS_WINDOWS else "linux", {})
    for name in names or ([] if explicit else list(known)):
        for candidate in known.get(name, []):
            path = os.path.expandvars(candidate)
            resolved = path if os.path.isfile(path) else shutil.which(path)
            if resolved:
                found[name] = resolved
                break
    return found


def browser_version(executable: str) -> str:
    if IS_WINDOWS:
        script = f"(Get-Item -LiteralPath '{executable.replace(chr(39), chr(39) * 2)}').VersionInfo.ProductVersion"
        out = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-Command", script],
                             capture_output=True, text=True, timeout=30)
        return out.stdout.strip() or "unknown"
    out = subprocess.run([executable, "--version"], capture_output=True, text=True, timeout=30)
    return out.stdout.strip() or "unknown"


def manifest() -> dict:
    return {
        "os": platform.platform(),
        "machine": platform.machine(),
        "logical_cpus": os.cpu_count(),
        "python": platform.python_version(),
        "corpus": CORPUS_VERSION,
        "note": "Hardware model is recorded generically; add it by hand when publishing (BENCHMARKS.md section 7).",
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--browser", action="append", default=[], metavar="NAME[=PATH]",
                        help="browser to test (repeatable); default: every known browser that is installed")
    parser.add_argument("--tabs", default="1,10,25", help="comma-separated tab counts (default 1,10,25)")
    parser.add_argument("--runs", type=int, default=5, help="repetitions per configuration (default 5)")
    parser.add_argument("--settle", type=float, default=20, help="seconds to wait after load before sampling memory")
    parser.add_argument("--idle-window", type=float, default=20, help="seconds of idle CPU measurement")
    parser.add_argument("--cooldown", type=float, default=10, help="seconds between runs")
    parser.add_argument("--load-timeout", type=float, default=120)
    parser.add_argument("--seed", type=int, default=None, help="seed for the randomized run order")
    parser.add_argument("--output", type=Path, required=True, help="JSON file for raw results and summary")
    parser.add_argument("--list", action="store_true", help="list detected browsers and exit")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    browsers = find_browsers(args.browser)
    if args.list or not browsers:
        for name, path in browsers.items():
            print(f"{name}: {path}")
        if not browsers:
            print("no browsers found; pass --browser NAME=PATH", file=sys.stderr)
            return 2
        return 0

    tab_counts = [int(t) for t in args.tabs.split(",") if t.strip()]
    seed = args.seed if args.seed is not None else random.SystemRandom().randrange(2**31)
    configs = [RunConfig(name, path, tabs, rep) for name, path in browsers.items()
               for tabs in tab_counts for rep in range(args.runs)]
    random.Random(seed).shuffle(configs)

    log = BeaconLog()
    server = make_server(corpus_pages(), log)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base_url = f"http://127.0.0.1:{server.server_address[1]}"
    versions = {name: browser_version(path) for name, path in browsers.items()}
    results: list[RunResult] = []
    try:
        for number, cfg in enumerate(configs, start=1):
            print(f"[{number}/{len(configs)}] {cfg.browser} {versions[cfg.browser]} tabs={cfg.tabs} run={cfg.repetition}",
                  flush=True)
            result = run_once(cfg, base_url, log, args.settle, args.idle_window, args.load_timeout)
            results.append(result)
            print(f"    {'ok' if result.ok else 'FAILED: ' + str(result.error)}"
                  f" startup={result.startup_ms} memory_mib={result.memory_mib} idle_cpu={result.idle_cpu_pct}",
                  flush=True)
            time.sleep(args.cooldown)
    finally:
        server.shutdown()

    summary = {}
    for name in browsers:
        for tabs in tab_counts:
            runs = [r for r in results if r.browser == name and r.tabs == tabs and r.ok]
            summary[f"{name}/{tabs}"] = {
                metric: summarize([getattr(r, metric) for r in runs])
                for metric in ("startup_ms", "all_loaded_ms", "memory_mib", "idle_cpu_pct")
            }
    report = {
        "manifest": manifest(),
        "browsers": {name: {"path": path, "version": versions[name]} for name, path in browsers.items()},
        "settings": {k: v for k, v in vars(args).items() if k not in ("output", "list", "browser")} | {"seed": seed},
        "runs": [r.__dict__ for r in results],
        "summary": summary,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, default=str) + "\n", encoding="utf-8")
    print(f"\nWrote {args.output}")
    for key, metrics in summary.items():
        line = ", ".join(f"{m}={v.get('median', float('nan')):.1f} (n={v['n']})" for m, v in metrics.items() if v["n"])
        print(f"  {key}: {line}")
    return 0 if all(r.ok for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
