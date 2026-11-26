#!/usr/bin/env python3
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""Manage Brumel's patch series against Chromium (CORE-002, issue #63).

Commands:

  check     Validate patches/series and every patch header (no checkout needed; runs in CI).
  list      Print the series in application order.
  stats     Patch budget: patches, modified upstream files, added and removed lines.
  apply     Apply the series to a Chromium checkout, one Git commit per patch.
  refresh   Regenerate patch files from those commits after resolving conflicts.

How apply works (see ADR-0013): the commit the checkout starts from is recorded
as refs/brumel/base. Each patch becomes one commit with a "Brumel-Patch: <path>"
trailer and fixed author/committer data, so the same pin and series give the
same commit IDs on every machine. Apply is resumable: it skips patches that
already have a commit and continues with the rest.

apply and refresh only print their plan unless --execute is given.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from brumeltools import (  # noqa: E402
    FEATURES_JSON,
    PATCHES_DIR,
    Step,
    ToolError,
    git,
    main_wrapper,
    print_plan,
    run_plan,
)

AREAS = (
    "branding", "core", "degoogle", "engine", "workspace", "memory", "shield",
    "nano", "connect", "tools", "ui", "dev", "fixes",
)
REQUIRED_FIELDS = ("Description", "Origin", "Module", "Feature", "Upstreamable", "SPDX-License-Identifier")
UPSTREAMABLE = ("yes", "maybe", "no")
BRUMEL_NAME = re.compile(r"^brumel/(?P<area>[a-z]+)/(?P<num>\d{4})-[a-z0-9]+(?:-[a-z0-9]+)*\.patch$")
ORIGIN = re.compile(r"^(brumel|ungoogled-chromium:\S+|upstream:\S+)$")
FEATURE_ID = re.compile(r"^[A-Z]+-\d{3}$")
HEADER_FIELD = re.compile(rb"^([A-Za-z][A-Za-z-]*):[ \t]*(.*?)\s*$")
HUNK = re.compile(rb"^@@ -\d+(?:,(\d+))? \+\d+(?:,(\d+))? @@")

# Added lines that would weaken a security boundary. A patch that matches must
# carry a "Security-Note:" header explaining why it does not (golden rule 2).
SECURITY_PATTERNS = (
    "--no-sandbox", "kNoSandbox", "disable-site-isolation", "kDisableSiteIsolation",
    "--disable-web-security", "kDisableWebSecurity", "is_cfi = false",
    "use_cfi_icall = false", "v8_enable_sandbox = false",
)

BASE_REF = "refs/brumel/base"
TRAILER = "Brumel-Patch"
# Fixed identity and dates make patch commits reproducible across machines.
COMMIT_ENV = {
    "GIT_AUTHOR_NAME": "Brumel patch series",
    "GIT_AUTHOR_EMAIL": "patches@brumel.invalid",
    "GIT_AUTHOR_DATE": "2000-01-01T00:00:00+0000",
    "GIT_COMMITTER_NAME": "Brumel patch series",
    "GIT_COMMITTER_EMAIL": "patches@brumel.invalid",
    "GIT_COMMITTER_DATE": "2000-01-01T00:00:00+0000",
}

NEW_PATCH_HEADER = """Description: TODO describe what this patch changes and why.
Origin: brumel
Module: {area}
Feature: n/a
Upstreamable: no
SPDX-License-Identifier: BSD-3-Clause
"""


# --------------------------------------------------------------------------- #
# Parsing
# --------------------------------------------------------------------------- #

@dataclass
class Patch:
    path: str                      # relative to the patches directory, with forward slashes
    header: bytes                  # everything before the first diff
    body: bytes                    # the diff itself
    fields: dict[str, str] = field(default_factory=dict)
    files: list[str] = field(default_factory=list)
    added: int = 0
    removed: int = 0
    added_lines: list[str] = field(default_factory=list)
    hunks: int = 0


def read_series(patches_dir: Path) -> list[str]:
    series = patches_dir / "series"
    if not series.exists():
        return []
    entries = []
    for raw in series.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line and not line.startswith("#"):
            entries.append(line)
    return entries


def split_patch(data: bytes) -> tuple[bytes, bytes]:
    """Split a patch into (header, diff). The diff starts at 'diff --git' or '--- '."""
    offset = 0
    for line in data.splitlines(keepends=True):
        if line.startswith(b"diff --git ") or line.startswith(b"--- "):
            return data[:offset], data[offset:]
        offset += len(line)
    return data, b""


def parse_patch(path: str, data: bytes) -> Patch:
    header, body = split_patch(data)
    patch = Patch(path=path, header=header, body=body)
    for line in header.splitlines():
        match = HEADER_FIELD.match(line)
        if match:
            patch.fields.setdefault(match.group(1).decode("utf-8", "replace"),
                                    match.group(2).decode("utf-8", "replace"))
    old_left = new_left = 0
    current_old = None
    for line in body.splitlines():
        if old_left > 0 or new_left > 0:
            tag = line[:1]
            if tag == b" " or line == b"":
                old_left -= 1
                new_left -= 1
            elif tag == b"-":
                old_left -= 1
                patch.removed += 1
            elif tag == b"+":
                new_left -= 1
                patch.added += 1
                patch.added_lines.append(line[1:].decode("utf-8", "replace"))
            elif tag == b"\\":
                pass  # "\ No newline at end of file"
            continue
        hunk = HUNK.match(line)
        if hunk:
            patch.hunks += 1
            old_left = int(hunk.group(1)) if hunk.group(1) is not None else 1
            new_left = int(hunk.group(2)) if hunk.group(2) is not None else 1
        elif line.startswith(b"--- "):
            current_old = _strip_prefix(line[4:])
        elif line.startswith(b"+++ "):
            new = _strip_prefix(line[4:])
            name = current_old if new == "/dev/null" else new
            if name and name != "/dev/null" and name not in patch.files:
                patch.files.append(name)
    return patch


def _strip_prefix(raw: bytes) -> str:
    name = raw.decode("utf-8", "replace").split("\t")[0].strip()
    if name.startswith(("a/", "b/")):
        name = name[2:]
    return name


def hunk_lines(body: bytes) -> list[bytes]:
    """The parts of a diff that matter for applying it (ignores index lines and headers)."""
    keep = []
    for line in body.splitlines():
        if line.startswith((b"diff --git ", b"index ", b"--- ", b"+++ ")):
            if line.startswith((b"--- ", b"+++ ")):
                keep.append(line.split(b"\t")[0])
            continue
        keep.append(line)
    return keep


def load_patches(patches_dir: Path) -> tuple[list[Patch], list[str]]:
    """Load every patch named in the series. Returns (patches, errors)."""
    patches, errors = [], []
    for entry in read_series(patches_dir):
        path = patches_dir / entry
        if not path.is_file():
            errors.append(f"series: {entry} does not exist")
            continue
        patches.append(parse_patch(entry, path.read_bytes()))
    return patches, errors


# --------------------------------------------------------------------------- #
# check / list / stats
# --------------------------------------------------------------------------- #

def load_feature_ids(features_json: Path) -> set[str]:
    try:
        data = json.loads(features_json.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return set()
    items = data.get("features", data) if isinstance(data, dict) else data
    return {item["id"] for item in items if isinstance(item, dict) and "id" in item}


def check_series(patches_dir: Path, feature_ids: set[str]) -> list[str]:
    errors: list[str] = []
    entries = read_series(patches_dir)

    seen: set[str] = set()
    for entry in entries:
        if entry in seen:
            errors.append(f"series: {entry} is listed more than once")
        seen.add(entry)
        if "\\" in entry or entry.startswith("/") or ".." in entry.split("/"):
            errors.append(f"series: {entry} must be a relative path with forward slashes")
        if not entry.endswith(".patch"):
            errors.append(f"series: {entry} must end with .patch")

    on_disk = {p.relative_to(patches_dir).as_posix() for p in patches_dir.rglob("*.patch")}
    for orphan in sorted(on_disk - seen):
        errors.append(f"{orphan}: not listed in patches/series")

    patches, load_errors = load_patches(patches_dir)
    errors += load_errors
    numbers: dict[tuple[str, str], str] = {}
    for patch in patches:
        errors += check_patch(patch, feature_ids)
        match = BRUMEL_NAME.match(patch.path)
        if match:
            key = (match.group("area"), match.group("num"))
            if key in numbers:
                errors.append(f"{patch.path}: number {key[1]} already used by {numbers[key]}")
            numbers[key] = patch.path
    return errors


def check_patch(patch: Patch, feature_ids: set[str]) -> list[str]:
    errors: list[str] = []
    where = patch.path
    if not patch.body or patch.hunks == 0:
        errors.append(f"{where}: contains no diff hunks")

    if patch.path.startswith("upstream-ungoogled/"):
        if "Origin" not in patch.fields:
            errors.append(f"{where}: imported patches need an 'Origin: ungoogled-chromium:<path>' line")
    elif patch.path.startswith("brumel/"):
        match = BRUMEL_NAME.match(patch.path)
        if not match:
            errors.append(f"{where}: name must be brumel/<area>/NNNN-short-kebab-name.patch")
        elif match.group("area") not in AREAS:
            errors.append(f"{where}: unknown area {match.group('area')!r} (one of {', '.join(AREAS)})")
        for name in REQUIRED_FIELDS:
            if not patch.fields.get(name):
                errors.append(f"{where}: missing header field {name}")
        fields = patch.fields
        if fields.get("Description", "").startswith("TODO"):
            errors.append(f"{where}: Description is still the TODO placeholder")
        if fields.get("Origin") and not ORIGIN.match(fields["Origin"]):
            errors.append(f"{where}: Origin must be brumel, ungoogled-chromium:<path> or upstream:<ref>")
        if match and fields.get("Module") and fields["Module"] != match.group("area"):
            errors.append(f"{where}: Module {fields['Module']!r} does not match directory {match.group('area')!r}")
        if fields.get("Upstreamable") and fields["Upstreamable"] not in UPSTREAMABLE:
            errors.append(f"{where}: Upstreamable must be one of {', '.join(UPSTREAMABLE)}")
        if fields.get("SPDX-License-Identifier") and fields["SPDX-License-Identifier"] != "BSD-3-Clause":
            errors.append(f"{where}: patches to Chromium files are BSD-3-Clause (ADR-0004)")
        feature = fields.get("Feature", "")
        if feature and feature != "n/a":
            for fid in (part.strip() for part in feature.split(",")):
                if not FEATURE_ID.match(fid):
                    errors.append(f"{where}: Feature {fid!r} is not a catalog ID (or 'n/a')")
                elif feature_ids and fid not in feature_ids:
                    errors.append(f"{where}: Feature {fid} is not in the feature catalog")
    else:
        errors.append(f"{where}: patches live under brumel/ or upstream-ungoogled/")

    if "Security-Note" not in patch.fields:
        for line in patch.added_lines:
            hit = next((p for p in SECURITY_PATTERNS if p in line), None)
            if hit:
                errors.append(
                    f"{where}: adds {hit!r}, which can weaken a security boundary; "
                    "explain why it does not in a 'Security-Note:' header"
                )
                break
    return errors


def stats(patches: list[Patch]) -> dict:
    files = sorted({f for patch in patches for f in patch.files})
    return {
        "patches": len(patches),
        "modified_upstream_files": len(files),
        "added_lines": sum(p.added for p in patches),
        "removed_lines": sum(p.removed for p in patches),
        "by_category": _by_category(patches),
    }


def _by_category(patches: list[Patch]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for patch in patches:
        parts = patch.path.split("/")
        key = "/".join(parts[:2]) if parts[0] == "brumel" and len(parts) > 2 else parts[0]
        counts[key] = counts.get(key, 0) + 1
    return dict(sorted(counts.items()))


# --------------------------------------------------------------------------- #
# Checkout helpers
# --------------------------------------------------------------------------- #

def resolve_src(path: Path) -> Path:
    """Accept either the gclient checkout root or its src/ directory."""
    for candidate in (path / "src", path):
        if (candidate / ".git").exists():
            return candidate
    raise ToolError(f"{path} is not a Chromium checkout (no src/.git or .git found)")


def rev(src: Path, ref: str) -> str | None:
    out = subprocess.run(["git", "rev-parse", "--verify", "--quiet", ref + "^{commit}"],
                         cwd=src, capture_output=True, text=True)
    return out.stdout.strip() or None


def applied_commits(src: Path) -> list[tuple[str, str | None]]:
    """(commit, trailer value) for every commit between the base and HEAD, oldest first."""
    if not rev(src, BASE_REF):
        return []
    out = git(["log", "--reverse", f"--format=%H%x00%(trailers:key={TRAILER},valueonly,separator=%x2C)%x00",
               f"{BASE_REF}..HEAD"], src)
    commits = []
    for record in out.split("\x00\n"):
        record = record.strip("\n")
        if not record:
            continue
        sha, _, trailer = record.partition("\x00")
        trailer = trailer.strip("\x00").strip()
        commits.append((sha, trailer or None))
    return commits


def is_clean(src: Path) -> bool:
    return git(["status", "--porcelain", "--untracked-files=no"], src).strip() == ""


# --------------------------------------------------------------------------- #
# apply
# --------------------------------------------------------------------------- #

def plan_apply(src: Path, patches_dir: Path, three_way: bool, reset: bool) -> tuple[list[Step], list[str]]:
    """Return (steps, notes)."""
    series = read_series(patches_dir)
    notes: list[str] = []
    steps: list[Step] = []
    base = rev(src, BASE_REF)
    applied: list[str] = []

    if base is None:
        steps.append(Step("Record the current commit as the patch base",
                          argv=["git", "update-ref", BASE_REF, "HEAD"], cwd=src))
    elif reset:
        steps.append(Step("Discard applied patches: reset the checkout to the patch base",
                          argv=["git", "reset", "--hard", BASE_REF], cwd=src))
    else:
        commits = applied_commits(src)
        untracked = [sha[:12] for sha, trailer in commits if trailer is None]
        if untracked:
            raise ToolError(
                "commits without a Brumel-Patch trailer on top of the series: " + ", ".join(untracked)
                + ". Export them with 'refresh' or remove them before applying."
            )
        applied = [trailer for _, trailer in commits if trailer]
        if applied != series[: len(applied)]:
            raise ToolError(
                "the patches applied in the checkout do not match the start of patches/series. "
                "Re-run with --reset to start again from the patch base (local changes are lost)."
            )
        if applied:
            notes.append(f"{len(applied)} patch(es) already applied; continuing after {applied[-1]}")

    if not (reset and base is not None) and not is_clean(src):
        raise ToolError(f"{src} has uncommitted changes; commit or discard them first")

    for entry in series[len(applied):]:
        patch_file = (patches_dir / entry).resolve()
        apply_argv = ["git", "apply", "--index", "--whitespace=nowarn"]
        if three_way:
            apply_argv.append("--3way")
        steps.append(Step(f"Apply {entry}", argv=[*apply_argv, str(patch_file)], cwd=src))
        steps.append(Step(
            f"Commit {entry}",
            argv=["git", "commit", "--quiet", "--allow-empty", "-m", entry, "-m", f"{TRAILER}: {entry}"],
            cwd=src,
            env=COMMIT_ENV,
        ))
    if not series:
        notes.append("patches/series is empty: there is nothing to apply yet")
    return steps, notes


# --------------------------------------------------------------------------- #
# refresh
# --------------------------------------------------------------------------- #

def diff_commits(src: Path, first: str, last: str) -> bytes:
    result = subprocess.run(
        ["git", "-c", "core.quotePath=false", "diff", "--no-color", "--no-ext-diff", "--no-textconv",
         "--no-renames", "--src-prefix=a/", "--dst-prefix=b/", f"{first}^", last],
        cwd=src, capture_output=True,
    )
    if result.returncode != 0:
        raise ToolError(f"git diff failed: {result.stderr.decode('utf-8', 'replace').strip()}")
    return result.stdout


def plan_refresh(src: Path, patches_dir: Path) -> tuple[list[Step], list[str]]:
    if not rev(src, BASE_REF):
        raise ToolError(f"{BASE_REF} does not exist in {src}; run 'apply' first")
    commits = applied_commits(src)
    missing = [sha[:12] for sha, trailer in commits if trailer is None]
    if missing:
        raise ToolError(
            "these commits have no 'Brumel-Patch: <path>' trailer: " + ", ".join(missing)
            + ". Amend them (git commit --amend --trailer 'Brumel-Patch: brumel/<area>/NNNN-name.patch'),"
            " or squash them into the patch they fix."
        )

    groups: list[tuple[str, list[str]]] = []
    for sha, trailer in commits:
        if groups and groups[-1][0] == trailer:
            groups[-1][1].append(sha)
        elif any(name == trailer for name, _ in groups):
            raise ToolError(
                f"commits for {trailer} are not consecutive; squash them "
                "(git rebase -i --autosquash) before refreshing"
            )
        else:
            groups.append((trailer, [sha]))

    series = read_series(patches_dir)
    notes: list[str] = []
    steps: list[Step] = []
    new_entries: list[tuple[str, str | None]] = []  # (new path, previous path in commit order)
    previous = None
    for path, shas in groups:
        if ".." in path.split("/") or path.startswith("/") or not path.endswith(".patch"):
            raise ToolError(f"invalid patch path in trailer: {path!r}")
        target = patches_dir / path
        body = diff_commits(src, shas[0], shas[-1])
        if target.exists():
            header, old_body = split_patch(target.read_bytes())
            if hunk_lines(old_body) == hunk_lines(body):
                previous = path
                continue
            notes.append(f"update {path}")
        else:
            match = BRUMEL_NAME.match(path)
            header = NEW_PATCH_HEADER.format(area=match.group("area") if match else "core").encode()
            notes.append(f"new {path} (fill in its header before committing)")
        if path not in series:
            new_entries.append((path, previous))
        content = header.rstrip(b"\r\n") + b"\n\n" + body
        steps.append(Step(f"Write {path}", action=_writer(target, content)))
        previous = path

    applied = {path for path, _ in groups}
    last_index = max((series.index(p) for p in applied if p in series), default=-1)
    for entry in series[: last_index + 1]:
        if entry not in applied:
            notes.append(f"warning: {entry} is in the series but has no commit in the checkout; "
                         "remove it from patches/series if it was dropped on purpose")

    if new_entries:
        steps.append(Step("Add new patches to patches/series",
                          action=lambda: insert_series_entries(patches_dir / "series", new_entries)))
    if not steps:
        notes.append("all patches are up to date")
    return steps, notes


def _writer(target: Path, content: bytes):
    def write() -> None:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    return write


def insert_series_entries(series_path: Path, entries: list[tuple[str, str | None]]) -> None:
    lines = series_path.read_text(encoding="utf-8").splitlines() if series_path.exists() else []
    for path, after in entries:
        index = len(lines)
        if after is not None:
            for i, line in enumerate(lines):
                if line.strip() == after:
                    index = i + 1
                    break
        lines.insert(index, path)
    series_path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--patches-dir", type=Path, default=PATCHES_DIR, help=argparse.SUPPRESS)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="validate the series and patch headers")
    sub.add_parser("list", help="print the series in order")
    stats_parser = sub.add_parser("stats", help="patch budget")
    stats_parser.add_argument("--json", action="store_true", help="machine-readable output")
    for name, text in (("apply", "apply the series to a checkout"), ("refresh", "regenerate patches from a checkout")):
        cmd = sub.add_parser(name, help=text)
        cmd.add_argument("--checkout", required=True, type=Path, help="gclient checkout root or its src/ directory")
        cmd.add_argument("--execute", action="store_true", help="perform the plan instead of printing it")
        if name == "apply":
            cmd.add_argument("--3way", dest="three_way", action="store_true",
                             help="fall back to a three-way merge when a patch does not apply cleanly")
            cmd.add_argument("--reset", action="store_true",
                             help="discard applied patches and local changes, then apply from the base")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    patches_dir: Path = args.patches_dir

    if args.command == "check":
        errors = check_series(patches_dir, load_feature_ids(FEATURES_JSON))
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        count = len(read_series(patches_dir))
        print(f"patches/series: {count} patch(es), {len(errors)} problem(s)")
        return 1 if errors else 0

    if args.command == "list":
        for number, entry in enumerate(read_series(patches_dir), start=1):
            print(f"{number:4d}  {entry}")
        return 0

    if args.command == "stats":
        patches, errors = load_patches(patches_dir)
        if errors:
            raise ToolError("; ".join(errors))
        result = stats(patches)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"Patches: {result['patches']}")
            print(f"Modified upstream files: {result['modified_upstream_files']}")
            print(f"Lines: +{result['added_lines']} -{result['removed_lines']}")
            for category, count in result["by_category"].items():
                print(f"  {category}: {count}")
        return 0

    src = resolve_src(args.checkout)
    if args.command == "apply":
        steps, notes = plan_apply(src, patches_dir, args.three_way, args.reset)
        title = f"Apply patches/series to {src}"
    else:
        steps, notes = plan_refresh(src, patches_dir)
        title = f"Refresh patches from {src}"
    for note in notes:
        print(note)
    print_plan(title, steps, args.execute)
    if args.execute and steps:
        try:
            run_plan(steps)
        except ToolError:
            if args.command == "apply":
                print(
                    "\nA patch did not apply. Resolve it in the checkout, then commit with the trailer\n"
                    f"'{TRAILER}: <patch path>' and run 'apply' again to continue, or 'refresh' to\n"
                    "update the patch files.",
                    file=sys.stderr,
                )
            raise
    return 0


if __name__ == "__main__":
    sys.exit(main_wrapper(main))
