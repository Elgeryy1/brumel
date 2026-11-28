#!/usr/bin/env python3
# SPDX-License-Identifier: MPL-2.0
# Copyright (c) 2026 Gerard Alvear and Brumel contributors.
"""Render the UI surface inventory from docs/design/surfaces.json.

Each surface lists the catalog features it carries. Its phase and status are
derived from docs/product/catalog/features.json, so the inventory can never
disagree with the catalog.

Usage:
    python3 scripts/design/render_surfaces.py           # write the page
    python3 scripts/design/render_surfaces.py --check   # exit 1 if stale or invalid
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "docs" / "design" / "surfaces.json"
CATALOG = ROOT / "docs" / "product" / "catalog" / "features.json"
OUTPUT = ROOT / "docs" / "design" / "UI_INVENTORY.md"

PHASES = {
    0: "Pre-development",
    1: "Technical Foundation",
    2: "Internal Alpha",
    3: "Public Alpha",
    4: "Public Beta",
    5: "Version 1.0",
    6: "Future Releases",
}
STATUS_ORDER = ["Available", "In Development", "Planned", "Research", "Experimental", "Deferred"]
TECHS = {"Views", "WebUI", "Views + WebUI", "Installer", "Assets"}
BASES = {"Upstream", "New"}
SURFACE_ID_RE = re.compile(r"^S-(WIN|WEB|DLG|INS)-\d{2}$")
PAGE_NAMES = {"CORE": "core", "ENG": "engine", "WRK": "workspace", "MEM": "memory",
              "SHD": "shield", "NANO": "nano", "CON": "connect", "TLS": "tools",
              "UI": "interface", "DEV": "dev"}
GENERATED = ("<!-- GENERATED FILE — Do not edit by hand. Source: docs/design/surfaces.json "
             "and docs/product/catalog/features.json. Regenerate: "
             "python3 scripts/design/render_surfaces.py -->")


def link(fid: str) -> str:
    mod = fid.split("-")[0]
    return f"[{fid}](../product/features/{PAGE_NAMES[mod]}.md#{fid.lower()})"


def validate(data: dict, features: dict[str, dict]) -> list[str]:
    errors: list[str] = []
    zones = {z["id"] for z in data["zones"]}
    seen: set[str] = set()
    for s in data["surfaces"]:
        sid = s.get("id", "?")
        if not SURFACE_ID_RE.match(sid):
            errors.append(f"{sid}: bad surface ID")
        if sid in seen:
            errors.append(f"{sid}: duplicate surface ID")
        seen.add(sid)
        if s.get("zone") not in zones:
            errors.append(f"{sid}: unknown zone {s.get('zone')!r}")
        if s.get("tech") not in TECHS:
            errors.append(f"{sid}: unknown tech {s.get('tech')!r}")
        if s.get("base") not in BASES:
            errors.append(f"{sid}: unknown base {s.get('base')!r}")
        refs = s.get("features", []) + s.get("related", [])
        if not refs:
            errors.append(f"{sid}: lists no features and no related features")
        for fid in refs:
            f = features.get(fid)
            if f is None:
                errors.append(f"{sid}: unknown feature {fid}")
            elif f["status"] == "Rejected":
                errors.append(f"{sid}: {fid} is Rejected")
            elif f.get("duplicate_of"):
                errors.append(f"{sid}: {fid} is a duplicate of {f['duplicate_of']}")
    return errors


def derive(s: dict, features: dict[str, dict]) -> tuple[str, str]:
    """Return the surface's phase and status summary from its features."""
    fs = [features[fid] for fid in s.get("features", [])]
    if not fs:
        return "Unassigned (catalog gap)", "No catalog entry"
    phase = PHASES[min(f["phase"] for f in fs)]
    counts = Counter(f["status"] for f in fs)
    status = ", ".join(f"{st} {counts[st]}" for st in STATUS_ORDER if counts[st])
    return phase, status


def render(data: dict, features: dict[str, dict]) -> str:
    out: list[str] = [GENERATED, ""]
    w = out.append
    w("# Brumel UI Surface Inventory")
    w("")
    w("> **Status: Research.** No Brumel interface has been built yet. This inventory lists")
    w("> every screen and surface the browser needs, linked to the")
    w("> [feature catalog](../product/FEATURES.md), which stays the source of truth.")
    w("")
    w("How to read it:")
    w("")
    w("- **Phase** is the earliest catalog phase among the surface's features, so it is the")
    w("  phase in which the surface first has to exist. Later features extend it.")
    w("- **Status** counts the catalog status of the features on the surface. A surface is")
    w("  never further along than its features.")
    w("- **Tech** is how the surface is built in Chromium: native **Views** (C++), **WebUI**")
    w("  (HTML, CSS and TypeScript served from an internal origin), the installer, or assets.")
    w("- **Base** says whether Chromium already ships the surface (**Upstream**, so Brumel")
    w("  restyles or extends it with small patches) or Brumel adds it (**New**).")
    w("- Security surfaces (omnibox security indicator, permission prompts, download")
    w("  warnings, interstitials, credential bubbles) keep their upstream layout and wording.")
    w("  Brumel changes them only through the colour pipeline. See")
    w("  [DESIGN_SYSTEM.md § 9](DESIGN_SYSTEM.md#9-implementation-notes-chromium).")
    w("")

    surfaces = data["surfaces"]
    derived = {s["id"]: derive(s, features) for s in surfaces}

    w("## Summary")
    w("")
    w("| Phase | Surfaces |")
    w("|---|---|")
    by_phase = Counter(derived[s["id"]][0] for s in surfaces)
    for name in list(PHASES.values()) + ["Unassigned (catalog gap)"]:
        if by_phase[name]:
            w(f"| {name} | {by_phase[name]} |")
    w(f"| **Total** | **{len(surfaces)}** |")
    w("")

    for zone in data["zones"]:
        rows = [s for s in surfaces if s["zone"] == zone["id"]]
        w(f"## {zone['title']}")
        w("")
        w("| ID | Surface | Tech | Base | Phase | Features | Status | Notes |")
        w("|---|---|---|---|---|---|---|---|")
        for s in sorted(rows, key=lambda r: (min([features[f]["phase"] for f in r.get("features", [])] or [9]), r["id"])):
            phase, status = derived[s["id"]]
            feats = ", ".join(link(f) for f in s.get("features", [])) or "—"
            if s.get("related"):
                feats += " (related: " + ", ".join(link(f) for f in s["related"]) + ")"
            w(f"| {s['id']} | {s['name']} | {s['tech']} | {s['base']} | {phase} | {feats} | {status} | {s.get('notes', '')} |")
        w("")

    covered = {f for s in surfaces for f in s.get("features", [])}
    w("## Catalog coverage")
    w("")
    w(f"{len(covered)} catalog features appear on at least one surface. Features without a")
    w("surface are build, engine or service work with no screen of their own (for example")
    w("the patch series, sandboxing or the sync relay); their effects show up on the")
    w("surfaces above, such as Glass Box or Browser Health.")
    w("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="fail if the page is stale or the source invalid")
    args = ap.parse_args()

    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    features = {f["id"]: f for f in json.loads(CATALOG.read_text(encoding="utf-8"))["features"]}
    errors = validate(data, features)
    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        return 1
    text = render(data, features)
    if args.check:
        current = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if current != text:
            print(f"error: {OUTPUT.relative_to(ROOT)} is stale; run scripts/design/render_surfaces.py",
                  file=sys.stderr)
            return 1
        print("UI inventory is up to date.")
        return 0
    OUTPUT.write_text(text, encoding="utf-8", newline="\n")
    print(f"Wrote {OUTPUT.relative_to(ROOT)} ({len(data['surfaces'])} surfaces).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
