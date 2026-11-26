#!/usr/bin/env python3
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""Compare the pinned Chromium version with the current Chromium stable release.

Reads config/upstream.json and queries Chromium Dash for the latest Stable
release on each platform Brumel targets. It never downloads Chromium source.

Exit codes:
  0  pin matches the latest stable release on every platform
  1  pin is behind (or differs from) the latest stable release on a platform
  2  error (network, parsing, invalid config)
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

CHROMIUM_DASH = "https://chromiumdash.appspot.com/fetch_releases"
DEFAULT_CONFIG = Path(__file__).resolve().parents[2] / "config" / "upstream.json"
USER_AGENT = "brumel-upstream-check/1 (+https://github.com/Elgeryy1/brumel)"
TIMEOUT_SECONDS = 20


def parse_version(version: str) -> tuple[int, ...]:
    """Turn '158.0.8127.88' into (158, 0, 8127, 88)."""
    parts = version.strip().split(".")
    if len(parts) != 4 or not all(p.isdigit() for p in parts):
        raise ValueError(f"not a Chromium version: {version!r}")
    return tuple(int(p) for p in parts)


def load_pin(config_path: Path) -> tuple[str, list[str]]:
    with config_path.open(encoding="utf-8") as fh:
        config = json.load(fh)
    version = config["chromium"]["version"]
    parse_version(version)  # validate
    platforms = config.get("platforms") or ["Windows", "Linux"]
    return version, platforms


def fetch_latest_stable(platform: str) -> dict:
    query = urllib.parse.urlencode({"channel": "Stable", "platform": platform, "num": 1})
    request = urllib.request.Request(f"{CHROMIUM_DASH}?{query}", headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        payload = json.load(response)
    if not isinstance(payload, list) or not payload:
        raise ValueError(f"unexpected Chromium Dash response for {platform}")
    release = payload[0]
    version = str(release.get("version", ""))
    parse_version(version)  # validate before trusting it
    return {
        "platform": platform,
        "version": version,
        "milestone": release.get("milestone"),
        "previous_version": release.get("previous_version"),
    }


def compare(pinned: str, latest: str) -> str:
    p, l = parse_version(pinned), parse_version(latest)
    if p == l:
        return "up-to-date"
    if p < l:
        return "major-behind" if p[0] < l[0] else "behind"
    return "ahead"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG, help="path to upstream.json")
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    args = parser.parse_args(argv)

    try:
        pinned, platforms = load_pin(args.config)
    except (OSError, KeyError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: cannot read pin from {args.config}: {exc}", file=sys.stderr)
        return 2

    results = []
    try:
        for platform in platforms:
            latest = fetch_latest_stable(platform)
            latest["status"] = compare(pinned, latest["version"])
            results.append(latest)
    except (urllib.error.URLError, TimeoutError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: cannot query Chromium Dash: {exc}", file=sys.stderr)
        return 2

    outdated = any(r["status"] != "up-to-date" for r in results)

    if args.json:
        print(json.dumps({"pinned": pinned, "results": results, "outdated": outdated}, indent=2))
    else:
        print(f"Pinned Chromium: {pinned}")
        for r in results:
            print(f"  {r['platform']:<8} latest stable {r['version']:<16} -> {r['status']}")
        print("Action needed: update config/upstream.json" if outdated else "Pin matches latest stable.")

    return 1 if outdated else 0


if __name__ == "__main__":
    sys.exit(main())
