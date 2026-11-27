#!/usr/bin/env python3
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""Replace the product name in Chromium's user-visible strings (CORE-004, issue #68).

Commands:

  apply    Rewrite the branded string files in a checkout from their committed
           content: "Chromium" becomes "Brumel" in the English messages and in
           every translation.
  revert   Restore those files to their committed content.

Why a script and not a patch: the product name appears in about 900 English
messages and 47,000 translated lines. GRIT finds a translation by a fingerprint
of the English text, so changing the English text without renaming the
translations would drop every language back to English. apply asks the
checkout's own GRIT for the fingerprints before and after the change and
renames the translations to match.

What stays "Chromium": attribution and legal text (the company name and the
copyright line, "The Chromium Authors", the link to the Chromium project on the
about page) and other products such as ChromiumOS. See ADR-0015.

apply always starts from the committed content (git show HEAD:<file>), so it
can be run again at any time and gives the same result. The changes are left
uncommitted on purpose: they are generated, never exported by patches.py
refresh. Run revert (or patches.py apply --reset) before applying patches again.

apply and revert only print their plan unless --execute is given.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

sys.path.insert(0, str(Path(__file__).resolve().parent))

from brumeltools import Step, ToolError, main_wrapper, print_plan, run_plan  # noqa: E402

UPSTREAM_NAME = "Chromium"
BRAND_NAME = "Brumel"


@dataclass(frozen=True)
class StringSet:
    grd: str                 # relative to src/
    parts: tuple[str, ...]   # <part> files included by the grd, relative to src/
    xtb_glob: str            # translations, relative to src/


STRING_SETS = (
    StringSet("chrome/app/chromium_strings.grd", ("chrome/app/settings_chromium_strings.grdp",),
              "chrome/app/resources/chromium_strings_*.xtb"),
    StringSet("components/components_chromium_strings.grd", (),
              "components/strings/components_chromium_strings_*.xtb"),
)

# Messages left untouched: attribution of the code Brumel is built on.
KEEP_MESSAGES = frozenset({
    "IDS_ABOUT_VERSION_COMPANY_NAME",
    "IDS_ABOUT_VERSION_COPYRIGHT",
})
# Text between these placeholders names the Chromium project, not the product.
PROTECTED_LINKS = (("BEGIN_LINK_CHROMIUM", "END_LINK_CHROMIUM"),)
# Phrases that name the upstream authors, wherever they appear.
PROTECTED_PHRASES = ("The Chromium Authors",)

# Lowercase letters may touch the name: inflections and prefixes in translations
# ("Chromiumin", "iChromium"). Uppercase ones may not ("ChromiumOS").
EDGE_BEFORE = r"(?<![A-Z0-9_])"
EDGE_AFTER = r"(?![A-Z0-9_])"
# The name with a menu accelerator inside it, e.g. "Chr&amp;omium".
ACCEL = "&amp;"
NAME_VARIANTS = [(UPSTREAM_NAME, BRAND_NAME)] + [
    (UPSTREAM_NAME[:i] + ACCEL + UPSTREAM_NAME[i:], BRAND_NAME[:min(i, len(BRAND_NAME) - 1)] + ACCEL
     + BRAND_NAME[min(i, len(BRAND_NAME) - 1):])
    for i in range(len(UPSTREAM_NAME))
]
NAME = re.compile(EDGE_BEFORE + "(" + "|".join(re.escape(v) for v, _ in sorted(NAME_VARIANTS, key=lambda v: -len(v[0])))
                  + ")" + EDGE_AFTER)
NAME_MAP = dict(NAME_VARIANTS)
# Some translations of Chromium's strings say "Chrome" where the English says
# "Chromium". They are rebranded too, unless the English mentions Chrome itself
# (the Chrome Web Store, for example). Other Chrome products keep their names.
CHROME = re.compile(EDGE_BEFORE + r"(?:Google )?Chrome(?!book|box|cast|base|bit)" + EDGE_AFTER)
PH = re.compile(r"(<ph\b[^>]*/>|<ph\b[^>]*>.*?</ph>)", re.DOTALL)
PH_NAME = re.compile(r'<ph\b[^>]*\bname="([^"]+)"')
MESSAGE = re.compile(r'(<message\b[^>]*\bname="([^"]+)"[^>]*>)(.*?)(</message>)', re.DOTALL)
TRANSLATION = re.compile(r'(<translation\b[^>]*\bid=")(\d+)("[^>]*>)(.*?)(</translation>)', re.DOTALL)


# --------------------------------------------------------------------------- #
# Text rules
# --------------------------------------------------------------------------- #

def _replace_plain(text: str, chrome: bool) -> str:
    """Replace the product name in text that holds no placeholders."""
    pieces = re.split("(" + "|".join(re.escape(p) for p in PROTECTED_PHRASES) + ")", text)
    out = []
    for piece in pieces:
        if piece not in PROTECTED_PHRASES:
            piece = NAME.sub(lambda m: NAME_MAP[m.group(1)], piece)
            if chrome:
                piece = CHROME.sub(BRAND_NAME, piece)
        out.append(piece)
    return "".join(out)


def rebrand_text(body: str, chrome: bool = False) -> str:
    """Rebrand one message or translation body. Placeholders are never changed."""
    out = []
    protected_until: str | None = None
    for token in PH.split(body):
        if PH.fullmatch(token):
            name = PH_NAME.search(token)
            name = name.group(1) if name else ""
            if protected_until is None:
                for begin, end in PROTECTED_LINKS:
                    if name == begin:
                        protected_until = end
            elif name == protected_until:
                protected_until = None
            out.append(token)
        elif protected_until is not None:
            out.append(token)
        else:
            out.append(_replace_plain(token, chrome))
    return "".join(out)


def rebrand_grd(text: str) -> tuple[str, list[str]]:
    """Rebrand every message of a .grd or .grdp file. Returns (text, names of changed messages)."""
    changed: list[str] = []

    def replace(match: re.Match) -> str:
        opening, name, body, closing = match.groups()
        if name in KEEP_MESSAGES:
            return match.group(0)
        new_body = rebrand_text(body)
        if new_body != body:
            changed.append(name)
        return opening + new_body + closing

    return MESSAGE.sub(replace, text), changed


def rebrand_xtb(text: str, renames: dict[str, str], mentions_chrome: frozenset[str] = frozenset()) -> tuple[str, int]:
    """Rename and rebrand the translations of changed messages. Returns (text, translations changed).

    mentions_chrome holds the old IDs of messages whose English text says
    "Chrome"; their translations keep it.
    """
    count = 0

    def replace(match: re.Match) -> str:
        nonlocal count
        start, old_id, middle, body, end = match.groups()
        new_id = renames.get(old_id)
        if new_id is None:
            return match.group(0)
        count += 1
        return start + new_id + middle + rebrand_text(body, chrome=old_id not in mentions_chrome) + end

    return TRANSLATION.sub(replace, text), count


# --------------------------------------------------------------------------- #
# Message IDs (from the checkout's GRIT)
# --------------------------------------------------------------------------- #

IdReader = Callable[[Path], list[tuple[str, str]]]  # grd path -> [(message name, message id)] in order


def grit_id_reader(src: Path) -> IdReader:
    """Read message IDs with the GRIT copy in the checkout (src/tools/grit)."""
    grit_dir = src / "tools" / "grit"
    if not (grit_dir / "grit" / "grd_reader.py").is_file():
        raise ToolError(f"GRIT not found at {grit_dir}")
    if str(grit_dir) not in sys.path:
        sys.path.insert(0, str(grit_dir))
    from grit import grd_reader  # type: ignore  # noqa: E402
    from grit.node import message  # type: ignore  # noqa: E402

    builtins = {"and", "or", "not", "True", "False", "in", "lang", "context", "pp_ifdef", "pp_if"}

    def read(grd: Path) -> list[tuple[str, str]]:
        # Every message counts, whatever its <if> condition: give each
        # condition variable a value so GRIT can parse the whole file.
        text = grd.read_text(encoding="utf-8")
        for part in re.findall(r'<part file="([^"]+)"', text):
            text += (grd.parent / part).read_text(encoding="utf-8")
        names: set[str] = set()
        for expr in re.findall(r'expr="([^"]*)"', text):
            names.update(re.findall(r"[A-Za-z_][A-Za-z0-9_]*", expr))
        # GRIT resolves its own variables (is_win, lang, ...) before defines.
        defines = {name: False for name in names - builtins}
        root = grd_reader.Parse(str(grd), debug=False, first_ids_file=None, defines=defines,
                                target_platform="win32")
        return [(node.attrs["name"], node.GetCliques()[0].GetMessage().GetId())
                for node in root.Preorder() if isinstance(node, message.MessageNode)]

    return read


def id_renames(before: list[tuple[str, str]], after: list[tuple[str, str]]) -> dict[str, str]:
    """Map old message IDs to new ones, pairing messages in document order."""
    if [n for n, _ in before] != [n for n, _ in after]:
        raise ToolError("the rebranded file has different messages than the original")
    renames: dict[str, str] = {}
    for (_, old), (_, new) in zip(before, after):
        if old == new:
            continue
        if renames.get(old, new) != new:
            raise ToolError(f"message ID {old} would become both {renames[old]} and {new}")
        renames[old] = new
    return renames


# --------------------------------------------------------------------------- #
# Checkout
# --------------------------------------------------------------------------- #

def resolve_src(path: Path) -> Path:
    for candidate in (path / "src", path):
        if (candidate / ".git").exists() and (candidate / "chrome" / "app").is_dir():
            return candidate
    raise ToolError(f"{path} is not a Chromium checkout (no src/.git with chrome/app)")


def committed(src: Path, rel: str) -> str:
    result = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=src, capture_output=True)
    if result.returncode != 0:
        raise ToolError(f"cannot read {rel} at HEAD: {result.stderr.decode('utf-8', 'replace').strip()}")
    return result.stdout.decode("utf-8")


def tracked(src: Path, pattern: str) -> list[str]:
    out = subprocess.run(["git", "ls-files", "--", pattern], cwd=src, capture_output=True, text=True, check=True)
    return sorted(line for line in out.stdout.splitlines() if line)


@dataclass
class Rewrite:
    files: dict[str, str] = field(default_factory=dict)   # rel path -> new content
    messages: int = 0
    translations: int = 0
    languages: int = 0


def plan_string_set(src: Path, string_set: StringSet, read_ids: IdReader) -> Rewrite:
    rewrite = Rewrite()
    sources = (string_set.grd, *string_set.parts)
    original = {rel: committed(src, rel) for rel in sources}
    rebranded = {}
    chrome_names: set[str] = set()
    for rel, text in original.items():
        rebranded[rel], changed = rebrand_grd(text)
        rewrite.messages += len(changed)
        chrome_names.update(m.group(2) for m in MESSAGE.finditer(text) if CHROME.search(m.group(3)))
    with tempfile.TemporaryDirectory() as tmp:
        ids = {}
        for label, contents in (("before", original), ("after", rebranded)):
            for rel, text in contents.items():
                target = Path(tmp, label, rel)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(text, encoding="utf-8", newline="\n")
            ids[label] = read_ids(Path(tmp, label, string_set.grd))
    renames = id_renames(ids["before"], ids["after"])
    mentions_chrome = frozenset(i for name, i in ids["before"] if name in chrome_names)
    for rel in sources:
        if rebranded[rel] != original[rel]:
            rewrite.files[rel] = rebranded[rel]
    for rel in tracked(src, string_set.xtb_glob):
        text, count = rebrand_xtb(committed(src, rel), renames, mentions_chrome)
        if count:
            rewrite.files[rel] = text
            rewrite.translations += count
            rewrite.languages += 1
    return rewrite


def all_files(src: Path) -> list[str]:
    files: list[str] = []
    for string_set in STRING_SETS:
        files += [string_set.grd, *string_set.parts, *tracked(src, string_set.xtb_glob)]
    return files


def _writer(path: Path, content: str):
    def write() -> None:
        path.write_text(content, encoding="utf-8", newline="\n")
    return write


def plan_apply(src: Path, read_ids: IdReader) -> tuple[list[Step], list[str]]:
    steps: list[Step] = []
    notes: list[str] = []
    for string_set in STRING_SETS:
        rewrite = plan_string_set(src, string_set, read_ids)
        notes.append(f"{string_set.grd}: {rewrite.messages} message(s), {rewrite.translations} translation(s) "
                     f"in {rewrite.languages} language(s)")
        for rel, content in rewrite.files.items():
            steps.append(Step(f"Write {rel}", action=_writer(src / rel, content)))
    return steps, notes


def plan_revert(src: Path) -> list[Step]:
    return [Step("Restore the branded string files to their committed content",
                 argv=["git", "checkout", "HEAD", "--", *all_files(src)], cwd=src)]


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    for name, text in (("apply", "rebrand the string files"), ("revert", "restore the string files")):
        cmd = sub.add_parser(name, help=text)
        cmd.add_argument("--checkout", required=True, type=Path, help="gclient checkout root or its src/ directory")
        cmd.add_argument("--execute", action="store_true", help="perform the plan instead of printing it")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    src = resolve_src(args.checkout)
    if args.command == "apply":
        steps, notes = plan_apply(src, grit_id_reader(src))
        for note in notes:
            print(note)
        title = f"Rebrand strings in {src} ({UPSTREAM_NAME} -> {BRAND_NAME})"
    else:
        steps = plan_revert(src)
        title = f"Revert rebranded strings in {src}"
    print_plan(title, steps, args.execute)
    if args.execute:
        run_plan(steps)
    return 0


if __name__ == "__main__":
    sys.exit(main_wrapper(main))
