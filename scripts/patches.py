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
already have a commit and continues with the rest. A patch that touches nested
DEPS repositories (v8/, third_party/devtools-frontend/src/, ...) is split, and
each part is committed in its own repository with the same trailer.

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


def same_changes(old: bytes, new: bytes) -> bool:
    """True when two diffs make the same changes, whatever the order of their files."""
    if hunk_lines(old) == hunk_lines(new):
        return True
    try:
        sections = [split_sections(body)[1] for body in (old, new)]
    except ToolError:
        return False
    signatures = [sorted((path, hunk_lines(b"".join(lines))) for path, lines in parts) for parts in sections]
    return signatures[0] == signatures[1]


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
# Nested repositories
# --------------------------------------------------------------------------- #
# A gclient checkout is many Git repositories: chromium/src plus nested DEPS
# such as v8/ or third_party/devtools-frontend/src/, which src/ ignores. A patch
# may touch several of them. apply splits it per repository and commits each
# part there with the same trailer. src/ always gets one commit per patch (empty
# if the patch does not touch src/), so its history is the ledger of the series.
# refresh joins the parts again, with the repository prefix restored.

REPOS_FILE = "brumel-patch-repos"  # in src's Git directory: nested repositories that have a base


def _section_path(line: bytes) -> str | None:
    """Path named by a '--- a/x', '+++ b/x' or 'diff --git a/x b/y' line, without its a/ or b/."""
    if line.startswith(b"diff --git "):
        parts = line[len(b"diff --git "):].rstrip(b"\r\n").split(b" ")
        raw = parts[-1] if parts else b""
    else:
        raw = line[4:].rstrip(b"\r\n").split(b"\t", 1)[0]
    if raw == b"/dev/null" or not raw:
        return None
    return _strip_prefix(raw)


def split_sections(body: bytes) -> tuple[bytes, list[tuple[str, list[bytes]]]]:
    """Split a diff into (preamble, [(path, lines)]), one entry per file.

    Hunk line counts are followed, so a removed line that starts with '--' is
    never taken for a file header.
    """
    preamble: list[bytes] = []
    sections: list[tuple[str, list[bytes]]] = []
    current: list[bytes] | None = None
    git_header_open = False      # inside a 'diff --git' header, before its '---' line
    old_left = new_left = 0
    lines = body.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if old_left > 0 or new_left > 0:
            if line.startswith(b"\\"):
                pass
            elif line.startswith(b"-"):
                old_left -= 1
            elif line.startswith(b"+"):
                new_left -= 1
            else:
                old_left -= 1
                new_left -= 1
            current.append(line)
            continue
        starts_plain = (line.startswith(b"--- ") and index + 1 < len(lines)
                        and lines[index + 1].startswith(b"+++ "))
        if line.startswith(b"diff --git ") or (starts_plain and not git_header_open):
            current = [line]
            sections.append(("", current))
            git_header_open = line.startswith(b"diff --git ")
            continue
        if current is None:
            preamble.append(line)
            continue
        if line.startswith(b"--- "):
            git_header_open = False
        hunk = HUNK.match(line)
        if hunk:
            old_left = int(hunk.group(1)) if hunk.group(1) is not None else 1
            new_left = int(hunk.group(2)) if hunk.group(2) is not None else 1
        current.append(line)
    named = []
    for _, section_lines in sections:
        path = None
        for line in section_lines:
            if line.startswith(b"+++ "):
                path = _section_path(line) or path
                break
            if line.startswith((b"--- ", b"diff --git ")):
                path = _section_path(line) or path
            if line.startswith(b"@@"):
                break
        if path is None:
            raise ToolError("cannot tell which file a diff section changes: " + section_lines[0].decode("utf-8", "replace").strip())
        named.append((path, section_lines))
    return b"".join(preamble), named


def owner_repo(src: Path, path: str, cache: dict[str, str] | None = None) -> str:
    """The nested repository (relative to src, '' for src itself) that holds path."""
    parts = path.split("/")
    for depth in range(len(parts) - 1, 0, -1):
        directory = "/".join(parts[:depth])
        if cache is not None and directory in cache:
            return cache[directory]
        if (src / directory / ".git").exists():
            if cache is not None:
                cache[directory] = directory
            return directory
    return ""


_HEADER_PREFIXES = (b"diff --git ", b"--- ", b"+++ ", b"rename from ", b"rename to ", b"copy from ", b"copy to ")


def _reprefix(line: bytes, old: str, new: str) -> bytes:
    """Replace the repository prefix old/ with new/ in one file header line."""
    old_b = (old + "/").encode() if old else b""
    new_b = (new + "/").encode() if new else b""
    for side in (b"a/", b"b/", b""):
        line = line.replace(b" " + side + old_b, b" " + side + new_b)
    return line


def _rewrite_section(lines: list[bytes], old: str, new: str) -> bytes:
    out = []
    in_header = True
    for line in lines:
        if line.startswith(b"@@") or line.startswith(b"GIT binary patch"):
            in_header = False
        if in_header and line.startswith(_HEADER_PREFIXES):
            line = _reprefix(line, old, new)
        out.append(line)
    return b"".join(out)


def split_by_repo(src: Path, body: bytes) -> list[tuple[str, bytes]]:
    """[(repository relative to src, diff with paths relative to it)], src first, others sorted."""
    _, sections = split_sections(body)
    cache: dict[str, str] = {}
    grouped: dict[str, list[bytes]] = {}
    for path, lines in sections:
        repo = owner_repo(src, path, cache)
        grouped.setdefault(repo, []).append(_rewrite_section(lines, repo, ""))
    return [(repo, b"".join(grouped[repo])) for repo in sorted(grouped, key=lambda r: (r != "", r))]


def git_dir(src: Path) -> Path:
    return Path(git(["rev-parse", "--absolute-git-dir"], src).strip())


def read_patch_repos(src: Path) -> list[str]:
    path = git_dir(src) / REPOS_FILE
    if not path.exists():
        return []
    return [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _record_repos(src: Path, repos: list[str]):
    def write() -> None:
        known = read_patch_repos(src)
        merged = known + [r for r in repos if r not in known]
        (git_dir(src) / REPOS_FILE).write_text("".join(r + "\n" for r in merged), encoding="utf-8", newline="\n")
    return write


def _trailers(repo: Path) -> set[str]:
    return {t for _, t in applied_commits(repo) if t}


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

    # Nested repositories touched before: reset them with src, or check they are clean.
    for repo in read_patch_repos(src) if base is not None else []:
        repo_path = src / repo
        if reset:
            if rev(repo_path, BASE_REF):
                steps.append(Step(f"Discard applied patches in {repo}",
                                  argv=["git", "reset", "--hard", BASE_REF], cwd=repo_path))
        elif not is_clean(repo_path):
            raise ToolError(f"{repo_path} has uncommitted changes; commit or discard them first")

    apply_argv = ["git", "apply", "--index", "--whitespace=nowarn"]
    if three_way:
        apply_argv.append("--3way")
    split_dir = git_dir(src) / "brumel-split"
    new_repos: list[str] = []
    based: set[str] = set()
    for entry in series[len(applied):]:
        patch_file = (patches_dir / entry).resolve()
        parts = split_by_repo(src, split_patch(patch_file.read_bytes())[1]) if patch_file.is_file() else []
        nested = [(repo, body) for repo, body in parts if repo]
        if not nested:
            steps.append(Step(f"Apply {entry}", argv=[*apply_argv, str(patch_file)], cwd=src))
        for repo, body in nested:
            repo_path = src / repo
            if repo not in based:
                based.add(repo)
                if rev(repo_path, BASE_REF) is None:
                    steps.append(Step(f"Record the current commit of {repo} as its patch base",
                                      argv=["git", "update-ref", BASE_REF, "HEAD"], cwd=repo_path))
                    if repo not in new_repos:
                        new_repos.append(repo)
                elif not reset and not is_clean(repo_path):
                    raise ToolError(f"{repo_path} has uncommitted changes; commit or discard them first")
            if not reset and rev(repo_path, BASE_REF) and entry in _trailers(repo_path):
                notes.append(f"{entry}: the part for {repo} is already committed there")
                continue
            part = split_dir / repo.replace("/", "__") / entry
            steps.append(Step(f"Write the part of {entry} for {repo}", action=_writer(part, body)))
            steps.append(Step(f"Apply {entry} in {repo}", argv=[*apply_argv, str(part)], cwd=repo_path))
            steps.append(Step(
                f"Commit {entry} in {repo}",
                argv=["git", "commit", "--quiet", "--allow-empty", "-m", entry, "-m", f"{TRAILER}: {entry}"],
                cwd=repo_path,
                env=COMMIT_ENV,
            ))
        if nested:
            src_body = dict(parts).get("")
            if src_body:
                part = split_dir / "src" / entry
                steps.append(Step(f"Write the part of {entry} for src", action=_writer(part, src_body)))
                steps.append(Step(f"Apply {entry} in src", argv=[*apply_argv, str(part)], cwd=src))
        steps.append(Step(
            f"Commit {entry}",
            argv=["git", "commit", "--quiet", "--allow-empty", "-m", entry, "-m", f"{TRAILER}: {entry}"],
            cwd=src,
            env=COMMIT_ENV,
        ))
    if new_repos:
        # Recorded first, so a failure part-way still leaves the list complete.
        steps.insert(0, Step("Remember the nested repositories the series touches",
                             action=_record_repos(src, new_repos)))
    if not series:
        notes.append("patches/series is empty: there is nothing to apply yet")
    return steps, notes


# --------------------------------------------------------------------------- #
# refresh
# --------------------------------------------------------------------------- #

def diff_commits(src: Path, first: str, last: str, prefix: str = "") -> bytes:
    """Diff of commits first..last; prefix (a nested repository path) goes before every file path."""
    lead = prefix + "/" if prefix else ""
    result = subprocess.run(
        ["git", "-c", "core.quotePath=false", "diff", "--no-color", "--no-ext-diff", "--no-textconv",
         "--no-renames", f"--src-prefix=a/{lead}", f"--dst-prefix=b/{lead}", f"{first}^", last],
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

    # Parts of the same patches committed in nested repositories.
    ledger = {path for path, _ in groups}
    nested: dict[str, dict[str, list[str]]] = {}   # repo -> trailer -> commits
    for repo in read_patch_repos(src):
        repo_path = src / repo
        if not rev(repo_path, BASE_REF):
            continue
        by_trailer: dict[str, list[str]] = {}
        last = None
        for sha, trailer in applied_commits(repo_path):
            if trailer is None:
                raise ToolError(f"a commit in {repo} has no '{TRAILER}: <path>' trailer: {sha[:12]}")
            if trailer not in ledger:
                raise ToolError(
                    f"{repo} has commits for {trailer}, but src has none. Add one in src with "
                    f"git commit --allow-empty -m {trailer} -m '{TRAILER}: {trailer}'"
                )
            if trailer in by_trailer and last != trailer:
                raise ToolError(f"commits for {trailer} in {repo} are not consecutive; squash them first")
            by_trailer.setdefault(trailer, []).append(sha)
            last = trailer
        nested[repo] = by_trailer

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
        for repo in sorted(nested):
            repo_shas = nested[repo].get(path)
            if repo_shas:
                body += diff_commits(src / repo, repo_shas[0], repo_shas[-1], prefix=repo)
        if target.exists():
            header, old_body = split_patch(target.read_bytes())
            if same_changes(old_body, body):
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
