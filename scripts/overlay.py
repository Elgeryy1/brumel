#!/usr/bin/env python3
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""Mirror Brumel's added sources (src/) into a Chromium checkout as //brumel.

Commands:

  check   Validate src/ (SPDX headers, no symlinks, no reserved Windows names).
  sync    Copy new and changed files into <checkout>/src/brumel and delete stale
          ones. The overlay is excluded from the checkout's Git
          (.git/info/exclude), so patches.py refresh never treats it as patch
          content. See docs/architecture/MODULE_SYSTEM.md section 7.

sync only prints its plan unless --execute is given. The tree it writes to
contains nothing else, so deleting stale files there is safe.
"""

from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from brumeltools import REPO_ROOT, Step, ToolError, main_wrapper, print_plan, run_plan  # noqa: E402

OVERLAY_SOURCE = REPO_ROOT / "src"
OVERLAY_NAME = "brumel"
EXCLUDE_LINE = f"/{OVERLAY_NAME}/"
MARKER = ".brumel-overlay"
SPDX_SUFFIXES = {".cc", ".h", ".mm", ".rs", ".gn", ".gni", ".py", ".ts", ".js", ".css", ".html", ".mojom", ".proto"}
WINDOWS_RESERVED = {"con", "prn", "aux", "nul", *(f"com{i}" for i in range(1, 10)), *(f"lpt{i}" for i in range(1, 10))}


def source_files(source: Path) -> list[Path]:
    if not source.is_dir():
        return []
    return sorted(p for p in source.rglob("*") if p.is_file() or p.is_symlink())


def check_sources(source: Path) -> list[str]:
    errors = []
    for path in source_files(source):
        rel = path.relative_to(source).as_posix()
        if path.is_symlink():
            errors.append(f"src/{rel}: symlinks are not allowed in the overlay")
            continue
        for part in path.relative_to(source).parts:
            if part.split(".")[0].lower() in WINDOWS_RESERVED:
                errors.append(f"src/{rel}: {part!r} is a reserved file name on Windows")
        if path.suffix in SPDX_SUFFIXES:
            head = path.read_text(encoding="utf-8", errors="replace")[:600]
            if "SPDX-License-Identifier: MPL-2.0" not in head:
                errors.append(f"src/{rel}: Brumel-original files need 'SPDX-License-Identifier: MPL-2.0' near the top")
    return errors


def plan_sync(source: Path, checkout_src: Path) -> tuple[list[Step], dict[str, int]]:
    target = checkout_src / OVERLAY_NAME
    if target.exists() and any(target.iterdir()) and not (target / MARKER).exists():
        raise ToolError(f"{target} exists and was not created by overlay.py; refusing to touch it")

    wanted = {p.relative_to(source).as_posix(): p for p in source_files(source)}
    existing = {}
    if target.exists():
        existing = {p.relative_to(target).as_posix(): p for p in target.rglob("*")
                    if p.is_file() and p.name != MARKER}

    steps: list[Step] = []
    counts = {"new": 0, "changed": 0, "unchanged": 0, "deleted": 0}
    for rel, src_path in wanted.items():
        dst = target / rel
        if rel not in existing:
            counts["new"] += 1
        elif not filecmp.cmp(src_path, dst, shallow=False):
            counts["changed"] += 1
        else:
            counts["unchanged"] += 1
            continue
        steps.append(Step(f"Copy {rel}", action=_copier(src_path, dst)))
    for rel in sorted(set(existing) - set(wanted)):
        counts["deleted"] += 1
        steps.append(Step(f"Delete stale {rel}", action=existing[rel].unlink))

    def finish() -> None:
        target.mkdir(parents=True, exist_ok=True)
        (target / MARKER).write_text("Managed by brumel scripts/overlay.py. Do not edit files here.\n",
                                     encoding="utf-8", newline="\n")
        _prune_empty_dirs(target)
        _ensure_excluded(checkout_src)

    steps.append(Step("Mark the overlay and exclude it from the checkout's Git", action=finish))
    return steps, counts


def _copier(src: Path, dst: Path):
    def copy() -> None:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    return copy


def _prune_empty_dirs(root: Path) -> None:
    for directory in sorted((p for p in root.rglob("*") if p.is_dir()), key=lambda p: len(p.parts), reverse=True):
        if not any(directory.iterdir()):
            directory.rmdir()


def _ensure_excluded(checkout_src: Path) -> None:
    git_dir = checkout_src / ".git"
    if not git_dir.is_dir():
        return  # not a Git checkout (for example a release tarball)
    exclude = git_dir / "info" / "exclude"
    exclude.parent.mkdir(parents=True, exist_ok=True)
    lines = exclude.read_text(encoding="utf-8").splitlines() if exclude.exists() else []
    if EXCLUDE_LINE not in lines:
        lines.append(EXCLUDE_LINE)
        exclude.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def resolve_src(path: Path) -> Path:
    for candidate in (path / "src", path):
        if (candidate / ".gn").is_file():
            return candidate
    raise ToolError(f"{path} does not look like a Chromium checkout (no src/.gn or .gn)")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", type=Path, default=OVERLAY_SOURCE, help=argparse.SUPPRESS)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="validate src/")
    sync = sub.add_parser("sync", help="mirror src/ into the checkout as //brumel")
    sync.add_argument("--checkout", required=True, type=Path, help="gclient checkout root or its src/ directory")
    sync.add_argument("--execute", action="store_true", help="perform the plan instead of printing it")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    source: Path = args.source
    errors = check_sources(source)
    if args.command == "check":
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        print(f"src/: {len(source_files(source))} file(s), {len(errors)} problem(s)")
        return 1 if errors else 0
    if errors:
        raise ToolError("src/ has problems; run 'overlay.py check'")
    checkout_src = resolve_src(args.checkout)
    steps, counts = plan_sync(source, checkout_src)
    print(", ".join(f"{v} {k}" for k, v in counts.items()))
    print_plan(f"Sync src/ into {checkout_src / OVERLAY_NAME}", steps, args.execute)
    if args.execute:
        run_plan(steps)
    return 0


if __name__ == "__main__":
    sys.exit(main_wrapper(main))
