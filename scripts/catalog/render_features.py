# SPDX-License-Identifier: MPL-2.0
# Copyright (c) 2026 Gerard Alvear and Brumel contributors.
"""Render the Brumel feature catalog pages from the canonical JSON catalog.

Outputs:
    docs/product/FEATURES.md            index, legend, counts, epics, R52 mapping
    docs/product/features/<module>.md   full feature cards, one page per module

Usage:
    python scripts/catalog/render_features.py           # write the pages
    python scripts/catalog/render_features.py --check   # exit 1 if any page is stale

Standard library only (Python 3.11+).
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "docs" / "product" / "catalog"
OUTPUT = ROOT / "docs" / "product" / "FEATURES.md"
# Page names use full module names: short prefixes such as "con" are reserved
# device names on Windows (CON, PRN, AUX, NUL) and would break checkouts there.
PAGE_NAMES = {"CORE": "core", "ENG": "engine", "WRK": "workspace", "MEM": "memory",
              "SHD": "shield", "NANO": "nano", "CON": "connect", "TLS": "tools",
              "UI": "interface", "DEV": "dev"}


def page(mod: str) -> str:
    return PAGE_NAMES[mod.upper()] + ".md"
MODULE_DIR = ROOT / "docs" / "product" / "features"

MODULES = {
    "CORE": "Brumel Core — Chromium parity, build, update and distribution",
    "ENG": "Brumel Engine — performance and efficiency",
    "WRK": "Brumel Workspace — tabs and productivity",
    "MEM": "Brumel Memory — memory and recovery",
    "SHD": "Brumel Shield — privacy and security",
    "NANO": "Brumel Nano — local AI",
    "CON": "Brumel Connect — continuity between devices",
    "TLS": "Brumel Tools — media and everyday utilities",
    "UI": "Personalization and interface",
    "DEV": "Brumel Dev — developers",
}
STATUSES = ["Available", "In Development", "Planned", "Research", "Experimental", "Deferred", "Rejected"]
TIERS = ["Essential", "Flagship", "Secondary", "Experimental", "Community", "Deferred", "Rejected"]
PHASES = {
    0: "Pre-development",
    1: "Technical Foundation",
    2: "Internal Alpha",
    3: "Public Alpha",
    4: "Public Beta",
    5: "Version 1.0",
    6: "Future",
}
PRIORITIES = ["P0", "P1", "P2", "P3"]
GENERATED = "<!-- GENERATED FILE — Do not edit by hand. Source: docs/product/catalog/*.json. Regenerate: python scripts/catalog/render_features.py -->"


def load() -> tuple[list[dict], list[dict]]:
    features = json.loads((CATALOG / "features.json").read_text(encoding="utf-8"))["features"]
    epics = json.loads((CATALOG / "epics.json").read_text(encoding="utf-8"))["epics"]
    return features, epics


def esc(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def link(fid: str, here: str | None = None) -> str:
    """Markdown link to a feature card. `here` is the module page being rendered (None = FEATURES.md)."""
    mod = fid.split("-")[0]
    if here is None:
        return f"[{fid}](features/{page(mod)}#{fid.lower()})"
    if here.upper() == mod:
        return f"[{fid}](#{fid.lower()})"
    return f"[{fid}]({page(mod)}#{fid.lower()})"


def count_table(title: str, counter: Counter, keys: list, label=lambda k: str(k)) -> list[str]:
    lines = [f"| {title} | Entries |", "| --- | ---: |"]
    for k in keys:
        if counter.get(k):
            lines.append(f"| {label(k)} | {counter[k]} |")
    lines.append(f"| **Total** | **{sum(counter.values())}** |")
    return lines


def short_title(epic: dict) -> str:
    return epic["title"].replace("[EPIC] ", "")


def render_index(features: list[dict], epics: list[dict]) -> str:
    out: list[str] = []
    w = out.append
    w(GENERATED)
    w("")
    w("# Brumel Feature Catalog")
    w("")
    w("> **Project status: Pre-development.** Nothing in this catalog is available yet. "
      "Every entry is a proposal with a status, a priority and acceptance criteria. "
      "Performance and resource targets are hypotheses until the public benchmark suite measures them.")
    w("")
    w("This catalog is the single source of truth for what Brumel might become. It keeps every idea that has "
      "been proposed — including deferred and rejected ones — under a stable ID, so that issues, pull requests, "
      "ADRs and roadmap items can reference it. Technical duplicates keep their own ID and point to the entry "
      "that implements them (*Duplicate of*), so no use case is silently dropped.")
    w("")
    w("- Canonical data: [`catalog/features.json`](catalog/features.json) and [`catalog/epics.json`](catalog/epics.json)")
    w("- Related: [Vision](VISION.md) · [Product requirements](PRODUCT_REQUIREMENTS.md) · "
      "[Feature matrix](FEATURE_MATRIX.md) · [Roadmap](../../ROADMAP.md) · [Architecture](../architecture/ARCHITECTURE.md)")
    w("- To propose a change, open a *Feature request* issue or edit the JSON and run the renderer (see [CONTRIBUTING](../../CONTRIBUTING.md)).")
    w("")
    w("## Contents")
    w("")
    for anchor, label in [("legend", "Legend"), ("summary", "Summary"), ("epics", "Epics"),
                          ("feature-cards-by-module", "Feature cards by module"),
                          ("the-52-research-proposals", "The 52 research proposals"),
                          ("feature-index", "Feature index")]:
        w(f"- [{label}](#{anchor})")
    w("")

    w("## Legend")
    w("")
    w("**Status** — where the work stands:")
    w("")
    w("| Status | Meaning |")
    w("| --- | --- |")
    w("| Available | Shipped in a public build. *(None yet.)* |")
    w("| In Development | Actively being implemented. *(None yet.)* |")
    w("| Planned | Accepted for a phase; understood well enough to build. Chromium-inherited items are Planned until the first build proves them. |")
    w("| Research | Needs investigation (feasibility, licensing, quality, security) before committing. |")
    w("| Experimental | Built behind a flag for evaluation; may be removed. *(None yet.)* |")
    w("| Deferred | Valid idea postponed because of risk, cost or dependencies; revisited later. |")
    w("| Rejected | Not pursued as stated, for technical or security reasons. The entry records why and names the safer alternative. |")
    w("")
    w("**Tier** — role in the product: **Essential** (required for a credible daily browser), "
      "**Flagship** (differentiating; communicates the pillars), **Secondary** (useful, lower priority), "
      "**Experimental** (uncertain value or feasibility), **Community** (best driven by contributors), "
      "**Deferred**, **Rejected**.")
    w("")
    w("**Priority** — P0 blocking for its phase · P1 high · P2 normal · P3 low/opportunistic. "
      "**Impact** — Low, Medium, High, Critical. **Complexity** — XS, S, M, L, XL (relative effort, not time).")
    w("")
    w("**Phases** — " + " · ".join(f"{k} {v}" for k, v in PHASES.items()) + ". See [ROADMAP.md](../../ROADMAP.md).")
    w("")
    w("**Pillars** — Efficiency · Memory · Clean Web · Trust · Everyday Tools. *Foundation* marks platform work. "
      "Brumel Nano is a cross-cutting technology, not a pillar.")
    w("")
    w("**Origin** — `S8` Chromium-inherited essentials · `A`–`I` module backlogs (A Engine, B Workspace, C Memory, "
      "D Shield, E Nano, F Connect, G Tools, H Interface, I Dev) · `R52-nn` the 52 product-research proposals · "
      "`FOUND` foundation work required by the plan · `S3`/`S16` project principles (rejected patterns).")
    w("")
    w("**Platforms** — Windows and Linux x64 are the primary targets; macOS is Deferred; Android belongs to the Future phase. "
      "`N/A` means the feature does not apply to that platform.")
    w("")

    w("## Summary")
    w("")
    dups = sum(1 for f in features if f["duplicate_of"])
    w(f"The catalog holds **{len(features)} entries** grouped in **{len(epics)} epics**. "
      f"**{dups}** of them are technical duplicates tracked under a primary entry, so the number of distinct "
      f"implementation items is **{len(features) - dups}**.")
    w("")
    w("### By module")
    w("")
    out.extend(count_table("Module", Counter(f["module"] for f in features), list(MODULES),
                           lambda k: f"[{k}](features/{page(k)}) — {MODULES[k].split(' — ')[0]}"))
    w("")
    w("### By tier")
    w("")
    out.extend(count_table("Tier", Counter(f["tier"] for f in features), TIERS))
    w("")
    w("### By status")
    w("")
    out.extend(count_table("Status", Counter(f["status"] for f in features), STATUSES))
    w("")
    w("### By proposed phase")
    w("")
    out.extend(count_table("Phase", Counter(f["phase"] for f in features), list(PHASES), lambda k: f"{k} — {PHASES[k]}"))
    w("")
    w("### By priority")
    w("")
    out.extend(count_table("Priority", Counter(f["priority"] for f in features), PRIORITIES))
    w("")

    w("## Epics")
    w("")
    w("Epics group features for planning and are mirrored as GitHub issues. The epic phase is the earliest phase "
      "in which the epic is expected to deliver something.")
    w("")
    w("| Epic | Title | Phase | Priority | Entries | Depends on |")
    w("| --- | --- | --- | --- | ---: | --- |")
    for e in epics:
        deps = ", ".join(e["depends_on"]) or "—"
        w(f"| {e['id']} | {esc(short_title(e))} | {e['phase']} — {PHASES[e['phase']]} | {e['priority']} | {len(e['features'])} | {deps} |")
    w("")

    w("## Feature cards by module")
    w("")
    w("Full cards — problem, use case, segments, dependencies, platforms, AI need, resource and infrastructure cost, "
      "security and privacy risks, competitors, evidence, acceptance criteria, origin and limitations — are on one page per module:")
    w("")
    w("| Module | Entries |")
    w("| --- | ---: |")
    for mod, title in MODULES.items():
        n = sum(1 for f in features if f["module"] == mod)
        w(f"| [{title}](features/{page(mod)}) | {n} |")
    w("")

    w("## The 52 research proposals")
    w("")
    w("Each of the 52 proposals from the product research appears exactly once in the catalog. They are proposals "
      "to evaluate, not commitments: many are Research or Experimental, and none is assumed to be unique to Brumel.")
    w("")
    w("| Proposal | ID | Name | Module | Tier | Status | Phase |")
    w("| --- | --- | --- | --- | --- | --- | --- |")
    for f in sorted((f for f in features if f["origin"].startswith("R52-")), key=lambda f: f["origin"]):
        w(f"| {f['origin']} | {link(f['id'])} | {esc(f['name'])} | {f['module']} | {f['tier']} | {f['status']} | {f['phase']} |")
    w("")

    w("## Feature index")
    w("")
    w("| ID | Name | Module | Tier | Status | Priority | Phase |")
    w("| --- | --- | --- | --- | --- | --- | --- |")
    for f in features:
        name = esc(f["name"]) + (f" *(→ {f['duplicate_of']})*" if f["duplicate_of"] else "")
        w(f"| {link(f['id'])} | {name} | {f['module']} | {f['tier']} | {f['status']} | {f['priority']} | {f['phase']} |")
    return "\n".join(out).rstrip() + "\n"


def render_module(mod: str, features: list[dict], epics: list[dict]) -> str:
    epic_by_id = {e["id"]: e for e in epics}
    mod_feats = [f for f in features if f["module"] == mod]
    out: list[str] = []
    w = out.append
    w(GENERATED)
    w("")
    w(f"# {MODULES[mod]}")
    w("")
    w("> **Project status: Pre-development.** Nothing listed here is available yet. Statuses, priorities and phases "
      "are proposals. See the [catalog index and legend](../FEATURES.md#legend).")
    w("")
    w(f"{len(mod_feats)} entries. Epics in this module:")
    w("")
    for e in epics:
        if e["module"] == mod:
            w(f"- **{e['id']}** {short_title(e)} — phase {e['phase']} ({PHASES[e['phase']]}), {e['priority']}")
    w("")
    w("| ID | Name | Tier | Status | Priority | Phase |")
    w("| --- | --- | --- | --- | --- | --- |")
    for f in mod_feats:
        name = esc(f["name"]) + (f" *(→ {f['duplicate_of']})*" if f["duplicate_of"] else "")
        w(f"| {link(f['id'], mod)} | {name} | {f['tier']} | {f['status']} | {f['priority']} | {f['phase']} |")
    w("")
    for f in mod_feats:
        epic = epic_by_id.get(f["epic"])
        w(f'<a id="{f["id"].lower()}"></a>')
        w("")
        w(f"## {f['id']} — {f['name']}")
        w("")
        w(f"`{f['tier']}` · `{f['status']}` · **{f['priority']}** · Impact {f['impact']} · Complexity {f['complexity']} · "
          f"Phase {f['phase']} ({PHASES[f['phase']]}) · Pillar {f['pillar']} · Epic {f['epic']}"
          + (f" ({short_title(epic)})" if epic else ""))
        w("")
        w(f["description"])
        w("")
        deps = ", ".join(link(d, mod) for d in f["dependencies"]) or "—"
        plats = " · ".join(f"{'macOS' if k == 'macos' else k.capitalize()} {v}" for k, v in f["platforms"].items())
        w(f"- **Problem:** {f['problem']}")
        w(f"- **Use case:** {f['use_case']}")
        w(f"- **Segments:** {', '.join(f['segments'])}")
        w(f"- **Dependencies:** {deps}")
        w(f"- **Platforms:** {plats}")
        w(f"- **AI:** {f['ai']} · **Resource cost:** {f['resource_cost']} · **Infrastructure cost:** {f['infra_cost']}")
        w(f"- **Security risk:** {f['security_risk']}")
        w(f"- **Privacy risk:** {f['privacy_risk']}")
        w(f"- **Competitors / precedents:** {', '.join(f['competitors']) or '—'}")
        w(f"- **Evidence:** {f['evidence']}")
        w("- **Acceptance criteria:**")
        for a in f["acceptance"]:
            w(f"  - {a}")
        dup = link(f["duplicate_of"], mod) if f["duplicate_of"] else "—"
        w(f"- **Origin:** {f['origin']} · **Duplicate of:** {dup}")
        if f.get("limitations"):
            w(f"- **Limitations / notes:** {f['limitations']}")
        w("")
    return "\n".join(out).rstrip() + "\n"


def outputs(features: list[dict], epics: list[dict]) -> dict[Path, str]:
    files = {OUTPUT: render_index(features, epics)}
    for mod in MODULES:
        files[MODULE_DIR / page(mod)] = render_module(mod, features, epics)
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description="Render the Brumel feature catalog pages.")
    parser.add_argument("--check", action="store_true", help="fail if any generated page is out of date")
    args = parser.parse_args()
    features, epics = load()
    files = outputs(features, epics)
    if args.check:
        stale = [p for p, c in files.items()
                 if not p.exists() or p.read_text(encoding="utf-8").replace("\r\n", "\n") != c]
        if stale:
            for p in stale:
                print(f"stale: {p.relative_to(ROOT).as_posix()}", file=sys.stderr)
            print("Run: python scripts/catalog/render_features.py", file=sys.stderr)
            return 1
        print("Feature catalog pages are up to date.")
        return 0
    MODULE_DIR.mkdir(parents=True, exist_ok=True)
    for p, c in files.items():
        p.write_text(c, encoding="utf-8", newline="\n")
    print(f"Wrote {len(files)} files ({len(features)} features, {len(epics)} epics).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
