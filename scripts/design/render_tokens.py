#!/usr/bin/env python3
# SPDX-License-Identifier: MPL-2.0
# Copyright (c) 2026 Gerard Alvear and Brumel contributors.
"""Render the Brumel UI tokens and check their contrast.

Reads docs/design/tokens/brumel.tokens.json and writes:
  - docs/design/tokens/tokens.css: CSS custom properties for WebUI and mockups
  - docs/design/tokens/CONTRAST.md: every required pair, measured with WCAG 2.x

Every pair listed under "checks" must meet its minimum in every theme, or the
script fails. Ratios are computed, never estimated.

Usage:
    python3 scripts/design/render_tokens.py           # write both files
    python3 scripts/design/render_tokens.py --check   # exit 1 if stale or a pair fails
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOKENS_DIR = ROOT / "docs" / "design" / "tokens"
SOURCE = TOKENS_DIR / "brumel.tokens.json"
CSS_OUT = TOKENS_DIR / "tokens.css"
MD_OUT = TOKENS_DIR / "CONTRAST.md"
HEX_RE = re.compile(r"^#[0-9A-Fa-f]{6}$")
REF_RE = re.compile(r"^\{([a-z0-9-]+)\}$")
PREFIX = "--brumel"

# Forced-colours mode replaces every role with a CSS system colour.
FORCED = {
    "frame": "Canvas", "toolbar": "Canvas", "surface": "Canvas", "raised": "Canvas",
    "hover": "Canvas", "selected": "Highlight", "ink": "CanvasText", "ink-muted": "CanvasText",
    "accent": "LinkText", "accent-fill": "ButtonText", "on-accent": "ButtonFace",
    "focus": "Highlight", "control-border": "ButtonText", "divider": "GrayText",
    "danger": "CanvasText", "warning": "CanvasText", "success": "CanvasText",
}


def luminance(hex_colour: str) -> float:
    channels = [int(hex_colour[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def contrast(a: str, b: str) -> float:
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def resolve(value: str, primitives: dict[str, str]) -> str:
    m = REF_RE.match(value)
    if m:
        name = m.group(1)
        if name not in primitives:
            raise ValueError(f"unknown primitive {name!r}")
        value = primitives[name]
    if not HEX_RE.match(value):
        raise ValueError(f"not a #RRGGBB colour: {value!r}")
    return value.upper()


def load() -> tuple[dict, dict[str, dict[str, str]], list[str]]:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    errors: list[str] = []
    prims = data["primitives"]
    roles = list(data["roles"])
    themes: dict[str, dict[str, str]] = {}
    for theme, values in data["themes"].items():
        missing = set(roles) - set(values)
        extra = set(values) - set(roles)
        if missing:
            errors.append(f"{theme}: missing roles {sorted(missing)}")
        if extra:
            errors.append(f"{theme}: undeclared roles {sorted(extra)}")
        themes[theme] = {}
        for role, value in values.items():
            try:
                themes[theme][role] = resolve(value, prims)
            except ValueError as exc:
                errors.append(f"{theme}.{role}: {exc}")
    if set(FORCED) != set(roles):
        errors.append("forced-colours map does not match the declared roles")
    return data, themes, errors


def measure(data: dict, themes: dict[str, dict[str, str]]) -> list[tuple]:
    rows = []
    for check in data["checks"]:
        for theme, values in themes.items():
            for bg in check["bg"]:
                ratio = contrast(values[check["fg"]], values[bg])
                rows.append((theme, check["fg"], bg, ratio, check["min"]))
    return rows


def block(selector: str, values: dict[str, str], indent: str = "") -> list[str]:
    lines = [f"{indent}{selector} {{"]
    lines += [f"{indent}  {PREFIX}-color-{role}: {value};" for role, value in values.items()]
    lines.append(f"{indent}}}")
    return lines


def render_css(data: dict, themes: dict[str, dict[str, str]]) -> str:
    scale = data["scale"]
    out = [
        "/* SPDX-License-Identifier: MPL-2.0 */",
        "/* GENERATED FILE: do not edit by hand. Source: docs/design/tokens/brumel.tokens.json.",
        "   Regenerate: python3 scripts/design/render_tokens.py */",
        "",
        ":root {",
        "  color-scheme: light dark;",
    ]
    out += [f"  {PREFIX}-color-{role}: {value};" for role, value in themes["light"].items()]
    out.append(f"  {PREFIX}-font-ui: {scale['font']['ui']};")
    out.append(f"  {PREFIX}-font-mono: {scale['font']['mono']};")
    for group in ("text", "leading", "weight", "space", "radius", "control", "motion"):
        for key, value in scale[group].items():
            out.append(f"  {PREFIX}-{group}-{key}: {value};")
    out.append("}")
    out.append("")
    out.append("@media (prefers-color-scheme: dark) {")
    out += block(':root:not([data-theme="light"]):not([data-theme="oled"])', themes["dark"], "  ")
    out.append("}")
    out += block(':root[data-theme="light"]', themes["light"])
    out += block(':root[data-theme="dark"]', themes["dark"])
    out += block(':root[data-theme="oled"]', themes["oled"])
    out.append(':root[data-theme="light"] { color-scheme: light; }')
    out.append(':root[data-theme="dark"], :root[data-theme="oled"] { color-scheme: dark; }')
    out.append("")
    out.append("@media (forced-colors: active) {")
    out += block(":root, :root[data-theme]", FORCED, "  ")
    out.append("}")
    out.append("")
    out.append("@media (prefers-reduced-motion: reduce) {")
    out.append("  :root {")
    for key in ("quick", "standard", "gentle"):
        out.append(f"    {PREFIX}-motion-{key}: 0ms;")
    out.append("  }")
    out.append("}")
    return "\n".join(out) + "\n"


def render_md(rows: list[tuple]) -> str:
    out = [
        "<!-- GENERATED FILE: do not edit by hand. Source: docs/design/tokens/brumel.tokens.json. "
        "Regenerate: python3 scripts/design/render_tokens.py -->",
        "",
        "# Token contrast",
        "",
        "Every pair below is measured with the WCAG 2.x relative-luminance formula by",
        "`scripts/design/render_tokens.py`. The script fails if any pair falls below its",
        "minimum, so this table is always true for the committed tokens. Text pairs need",
        "4.5:1; focus rings and control borders need 3:1 (WCAG 2.2 SC 1.4.11 and 2.4.13).",
        "",
        "| Theme | Foreground | Background | Ratio | Minimum | Result |",
        "|---|---|---|---|---|---|",
    ]
    for theme, fg, bg, ratio, minimum in rows:
        result = "Pass" if ratio >= minimum else "**Fail**"
        out.append(f"| {theme} | `{fg}` | `{bg}` | {ratio:.2f} | {minimum:.1f} | {result} |")
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="fail if outputs are stale or a pair fails")
    args = ap.parse_args()

    data, themes, errors = load()
    if not errors:
        for theme, fg, bg, ratio, minimum in measure(data, themes):
            if ratio < minimum:
                errors.append(f"{theme}: {fg} on {bg} is {ratio:.2f}, needs {minimum}")
    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        return 1

    outputs = {CSS_OUT: render_css(data, themes), MD_OUT: render_md(measure(data, themes))}
    if args.check:
        stale = [p for p, text in outputs.items()
                 if not p.exists() or p.read_text(encoding="utf-8") != text]
        for p in stale:
            print(f"error: {p.relative_to(ROOT)} is stale; run scripts/design/render_tokens.py",
                  file=sys.stderr)
        if stale:
            return 1
        print("Tokens are up to date and every contrast pair passes.")
        return 0
    for path, text in outputs.items():
        path.write_text(text, encoding="utf-8", newline="\n")
    print(f"Wrote {CSS_OUT.relative_to(ROOT)} and {MD_OUT.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
