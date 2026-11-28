#!/usr/bin/env python3
# SPDX-License-Identifier: MPL-2.0
# Copyright (c) 2026 Gerard Alvear and Brumel contributors.
"""Inline the shared icon sprite into every design mockup.

The mockups open straight from disk, where browsers refuse <use> references to
another file. Each page therefore carries the sprite from
docs/design/mockups/_icons.svg between <!--ICONS--> and <!--/ICONS-->.

Usage:
    python3 scripts/design/inline_icons.py           # rewrite the pages
    python3 scripts/design/inline_icons.py --check   # exit 1 if a page is stale
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MOCKUPS = ROOT / "docs" / "design" / "mockups"
SPRITE = MOCKUPS / "_icons.svg"
BLOCK = re.compile(r"<!--ICONS-->(?:.*?<!--/ICONS-->)?", re.S)


def render(page: str, sprite: str) -> str:
    replacement = "<!--ICONS-->\n" + sprite.strip() + "\n<!--/ICONS-->"
    return BLOCK.sub(lambda _m: replacement, page, count=1)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="fail if a page does not carry the current sprite")
    args = ap.parse_args()
    sprite = SPRITE.read_text(encoding="utf-8")
    stale = []
    for page in sorted(MOCKUPS.glob("*.html")):
        text = page.read_text(encoding="utf-8")
        if "<!--ICONS-->" not in text:
            continue
        new = render(text, sprite)
        if new != text:
            stale.append(page)
            if not args.check:
                page.write_text(new, encoding="utf-8", newline="\n")
    if args.check and stale:
        for page in stale:
            print(f"error: {page.relative_to(ROOT)} is stale; run scripts/design/inline_icons.py", file=sys.stderr)
        return 1
    print("Icon sprite is current in every mockup." if args.check else f"Updated {len(stale)} page(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
