#!/usr/bin/env python3
# SPDX-License-Identifier: MPL-2.0
# Copyright (c) The Brumel Authors
"""Validate Brumel repository documentation and the feature catalog.

Checks:
  1. Every relative link and image in Markdown files resolves to an existing
     file or directory (external URLs, mailto: and pure #anchors are ignored).
  2. docs/product/catalog/features.json and epics.json follow the catalog
     schema: required keys, stable ID formats, valid enums, resolvable
     references, consistent epic membership, and exactly one entry for each of
     the 52 research proposals (R52-01 .. R52-52).

Usage:
  python3 scripts/validate_docs.py [--root PATH] [--links-only] [--catalog-only]

Exit status is 1 if any error is found. Standard library only.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------

MODULE_PREFIXES = ("CORE", "ENG", "WRK", "MEM", "SHD", "NANO", "CON", "TLS", "UI", "DEV")
FEATURE_ID_RE = re.compile(r"^(%s)-\d{3}$" % "|".join(MODULE_PREFIXES))
EPIC_ID_RE = re.compile(r"^EP-(%s)-\d{2}$" % "|".join(MODULE_PREFIXES))
R52_RE = re.compile(r"^R52-(\d{2})$")

STATUSES = ("Available", "In Development", "Planned", "Research", "Experimental", "Deferred", "Rejected")
TIERS = ("Flagship", "Essential", "Secondary", "Experimental", "Community", "Deferred", "Rejected")
PRIORITIES = ("P0", "P1", "P2", "P3")
IMPACTS = ("Low", "Medium", "High", "Critical")
COMPLEXITIES = ("XS", "S", "M", "L", "XL")
PILLARS = ("Efficiency", "Memory", "Clean Web", "Trust", "Everyday Tools", "Foundation")
AI_LEVELS = ("None", "Optional", "Required", "Deterministic-first")
INFRA_COSTS = ("None", "Low", "Medium", "High")
RISK_LEVELS = ("Low", "Medium", "High", "Critical")
PLATFORM_KEYS = ("windows", "linux", "macos", "android")
PLATFORM_VALUES = STATUSES + ("Partial", "N/A")

FEATURE_REQUIRED = {
    "id": str, "name": str, "module": str, "epic": str, "pillar": str, "tier": str,
    "status": str, "priority": str, "impact": str, "complexity": str, "phase": int,
    "description": str, "problem": str, "use_case": str, "segments": list,
    "dependencies": list, "platforms": dict, "ai": str, "resource_cost": str,
    "infra_cost": str, "security_risk": str, "privacy_risk": str, "competitors": list,
    "evidence": str, "acceptance": list, "origin": str, "limitations": str,
}
EPIC_REQUIRED = {
    "id": str, "title": str, "module": str, "summary": str, "phase": int,
    "priority": str, "features": list, "depends_on": list,
}

SKIP_DIRS = {".git", "node_modules", "src", "chromium", "chromium-src", "out",
             "depot_tools", ".venv", "venv", "__pycache__", "downloads", "cache"}

CATALOG_DIR = Path("docs") / "product" / "catalog"

# --------------------------------------------------------------------------
# Link checking
# --------------------------------------------------------------------------

_INLINE_LINK_RE = re.compile(r"\]\(\s*<?([^)\s>]+)>?(?:\s+[\"'][^\"']*[\"'])?\s*\)")
_REF_DEF_RE = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*<?(\S+?)>?(?:\s|$)")
_HTML_ATTR_RE = re.compile(r"""(?:src|href)\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
_INLINE_CODE_RE = re.compile(r"`+[^`]*`+")
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


def iter_markdown_files(root: Path):
    """Yield Markdown files under root, skipping build and vendor directories."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in sorted(filenames):
            if name.lower().endswith(".md"):
                yield Path(dirpath) / name


def extract_link_targets(text: str):
    """Return (line_number, target) pairs for links found outside code."""
    text = _HTML_COMMENT_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    results = []
    in_fence = False
    fence_marker = ""
    for lineno, line in enumerate(text.splitlines(), start=1):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence, fence_marker = True, marker
            elif marker == fence_marker:
                in_fence = False
            continue
        if in_fence:
            continue
        clean = _INLINE_CODE_RE.sub("", line)
        for regex in (_INLINE_LINK_RE, _HTML_ATTR_RE):
            for match in regex.finditer(clean):
                results.append((lineno, match.group(1)))
        ref = _REF_DEF_RE.match(clean)
        if ref:
            results.append((lineno, ref.group(1)))
    return results


def is_external(target: str) -> bool:
    return bool(_SCHEME_RE.match(target)) or target.startswith("//")


def check_links(root) -> list:
    """Check relative links in all Markdown files under root. Returns error strings."""
    root = Path(root).resolve()
    errors = []
    for md_file in iter_markdown_files(root):
        try:
            text = md_file.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{md_file.relative_to(root).as_posix()}: not valid UTF-8 ({exc})")
            continue
        for lineno, target in extract_link_targets(text):
            if not target or target.startswith("#") or is_external(target):
                continue
            path_part = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not path_part:
                continue
            if path_part.startswith("/"):
                resolved = root / path_part.lstrip("/")
            else:
                resolved = md_file.parent / path_part
            if not resolved.exists():
                rel = md_file.relative_to(root).as_posix()
                errors.append(f"{rel}:{lineno}: broken link -> {target}")
    return errors

# --------------------------------------------------------------------------
# Catalog validation
# --------------------------------------------------------------------------


def _items(doc, key):
    if isinstance(doc, dict):
        return doc.get(key, [])
    if isinstance(doc, list):
        return doc
    return []


def _check_types(obj, required, label, errors):
    for key, expected in required.items():
        if key not in obj:
            errors.append(f"{label}: missing required key '{key}'")
            continue
        value = obj[key]
        if expected is int:
            if not isinstance(value, int) or isinstance(value, bool):
                errors.append(f"{label}: '{key}' must be an integer")
        elif not isinstance(value, expected):
            errors.append(f"{label}: '{key}' must be of type {expected.__name__}")
        elif expected is str and not value.strip():
            errors.append(f"{label}: '{key}' must not be empty")


def _check_enum(obj, key, allowed, label, errors):
    value = obj.get(key)
    if isinstance(value, str) and value not in allowed:
        errors.append(f"{label}: '{key}' = {value!r} is not one of {', '.join(allowed)}")


def _check_leveled(obj, key, levels, label, errors):
    """Value must be a level, optionally followed by a range ("Low/Medium") or a note."""
    value = obj.get(key)
    if not isinstance(value, str):
        return
    head = re.split(r"\s", value.strip(), maxsplit=1)[0]
    parts = head.rstrip(".,;:").split("/")
    if not all(part in levels for part in parts):
        errors.append(f"{label}: '{key}' must start with one of {', '.join(levels)} "
                      f"(optionally 'A/B' and a note), got {value!r}")


def _check_risk(obj, key, label, errors):
    _check_leveled(obj, key, RISK_LEVELS, label, errors)


def validate_catalog(features_doc, epics_doc, require_r52: bool = True) -> list:
    """Validate the feature and epic catalogs. Returns a list of error strings."""
    errors = []
    features = _items(features_doc, "features")
    epics = _items(epics_doc, "epics")
    if not isinstance(features, list) or not features:
        return ["features.json: 'features' must be a non-empty list"]
    if not isinstance(epics, list):
        return ["epics.json: 'epics' must be a list"]

    # ---- Features: structure and enums
    feature_ids = []
    for index, feat in enumerate(features):
        if not isinstance(feat, dict):
            errors.append(f"features[{index}]: must be an object")
            continue
        fid = feat.get("id", f"features[{index}]")
        label = f"feature {fid}"
        _check_types(feat, FEATURE_REQUIRED, label, errors)
        if isinstance(fid, str):
            if not FEATURE_ID_RE.match(fid):
                errors.append(f"{label}: id does not match <PREFIX>-NNN with a known module prefix")
            elif feat.get("module") != fid.split("-")[0]:
                errors.append(f"{label}: module {feat.get('module')!r} does not match id prefix")
            feature_ids.append(fid)
        _check_enum(feat, "module", MODULE_PREFIXES, label, errors)
        _check_enum(feat, "status", STATUSES, label, errors)
        _check_enum(feat, "tier", TIERS, label, errors)
        _check_enum(feat, "priority", PRIORITIES, label, errors)
        _check_enum(feat, "impact", IMPACTS, label, errors)
        _check_enum(feat, "complexity", COMPLEXITIES, label, errors)
        _check_enum(feat, "pillar", PILLARS, label, errors)
        _check_enum(feat, "ai", AI_LEVELS, label, errors)
        _check_leveled(feat, "infra_cost", INFRA_COSTS, label, errors)
        _check_risk(feat, "security_risk", label, errors)
        _check_risk(feat, "privacy_risk", label, errors)
        phase = feat.get("phase")
        if isinstance(phase, int) and not 0 <= phase <= 6:
            errors.append(f"{label}: phase must be between 0 and 6")
        if isinstance(feat.get("acceptance"), list) and not feat["acceptance"]:
            errors.append(f"{label}: 'acceptance' must contain at least one criterion")
        platforms = feat.get("platforms")
        if isinstance(platforms, dict):
            for key in PLATFORM_KEYS:
                if key not in platforms:
                    errors.append(f"{label}: platforms missing '{key}'")
            for key, value in platforms.items():
                if key not in PLATFORM_KEYS:
                    errors.append(f"{label}: unknown platform key '{key}'")
                elif not isinstance(value, str) or not any(
                        value == v or value.startswith(v + " ") for v in PLATFORM_VALUES):
                    errors.append(f"{label}: platforms.{key} = {value!r} must start with one of "
                                  f"{', '.join(PLATFORM_VALUES)}")

    # ---- Features: uniqueness and references
    seen = set()
    for fid in feature_ids:
        if fid in seen:
            errors.append(f"feature {fid}: duplicate id")
        seen.add(fid)
    for feat in features:
        if not isinstance(feat, dict):
            continue
        fid = feat.get("id")
        for dep in feat.get("dependencies") or []:
            if dep == fid:
                errors.append(f"feature {fid}: depends on itself")
            elif dep not in seen:
                errors.append(f"feature {fid}: dependency {dep!r} does not exist")
        dup = feat.get("duplicate_of")
        if dup is not None:
            if dup == fid:
                errors.append(f"feature {fid}: duplicate_of points to itself")
            elif dup not in seen:
                errors.append(f"feature {fid}: duplicate_of {dup!r} does not exist")

    # ---- Research-52 coverage
    if require_r52:
        r52_count = {}
        for feat in features:
            origin = feat.get("origin") if isinstance(feat, dict) else None
            match = R52_RE.match(origin or "")
            if match:
                number = int(match.group(1))
                if not 1 <= number <= 52:
                    errors.append(f"feature {feat.get('id')}: origin {origin} is outside R52-01..R52-52")
                r52_count[number] = r52_count.get(number, 0) + 1
        for number in range(1, 53):
            count = r52_count.get(number, 0)
            if count != 1:
                errors.append(f"research proposal R52-{number:02d} appears {count} times (expected exactly 1)")

    # ---- Epics
    epic_ids = set()
    for index, epic in enumerate(epics):
        if not isinstance(epic, dict):
            errors.append(f"epics[{index}]: must be an object")
            continue
        eid = epic.get("id", f"epics[{index}]")
        label = f"epic {eid}"
        _check_types(epic, EPIC_REQUIRED, label, errors)
        if isinstance(eid, str):
            if not EPIC_ID_RE.match(eid):
                errors.append(f"{label}: id does not match EP-<PREFIX>-NN")
            elif epic.get("module") != eid.split("-")[1]:
                errors.append(f"{label}: module {epic.get('module')!r} does not match id")
            if eid in epic_ids:
                errors.append(f"{label}: duplicate id")
            epic_ids.add(eid)
        _check_enum(epic, "priority", PRIORITIES, label, errors)
        phase = epic.get("phase")
        if isinstance(phase, int) and not 0 <= phase <= 6:
            errors.append(f"{label}: phase must be between 0 and 6")

    features_by_epic = {}
    for feat in features:
        if isinstance(feat, dict) and isinstance(feat.get("epic"), str):
            features_by_epic.setdefault(feat["epic"], set()).add(feat.get("id"))
            if feat["epic"] not in epic_ids:
                errors.append(f"feature {feat.get('id')}: epic {feat['epic']!r} does not exist")

    for epic in epics:
        if not isinstance(epic, dict):
            continue
        eid = epic.get("id")
        listed = set(epic.get("features") or [])
        for fid in sorted(listed - seen):
            errors.append(f"epic {eid}: lists unknown feature {fid!r}")
        expected = features_by_epic.get(eid, set())
        for fid in sorted((listed & seen) - expected):
            errors.append(f"epic {eid}: lists {fid} but that feature belongs to another epic")
        for fid in sorted(expected - listed):
            errors.append(f"epic {eid}: does not list its feature {fid}")
        for dep in epic.get("depends_on") or []:
            if dep == eid:
                errors.append(f"epic {eid}: depends on itself")
            elif dep not in epic_ids:
                errors.append(f"epic {eid}: depends_on {dep!r} does not exist")

    return errors


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)

# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=Path(__file__).resolve().parent.parent,
                        help="repository root (default: parent of scripts/)")
    parser.add_argument("--links-only", action="store_true")
    parser.add_argument("--catalog-only", action="store_true")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()
    errors = []

    if not args.catalog_only:
        link_errors = check_links(root)
        print(f"[links] {len(link_errors)} problem(s) found")
        errors += link_errors

    if not args.links_only:
        features_path = root / CATALOG_DIR / "features.json"
        epics_path = root / CATALOG_DIR / "epics.json"
        if not features_path.exists() or not epics_path.exists():
            print("[catalog] skipped: docs/product/catalog/features.json or epics.json not found")
        else:
            try:
                features_doc = load_json(features_path)
                epics_doc = load_json(epics_path)
            except json.JSONDecodeError as exc:
                errors.append(f"catalog: invalid JSON ({exc})")
            else:
                catalog_errors = validate_catalog(features_doc, epics_doc)
                count = len(_items(features_doc, "features"))
                epic_count = len(_items(epics_doc, "epics"))
                print(f"[catalog] {count} features, {epic_count} epics, "
                      f"{len(catalog_errors)} problem(s) found")
                errors += catalog_errors

    for error in errors:
        print(f"  ERROR {error}")
    if errors:
        print(f"FAILED with {len(errors)} error(s)")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
