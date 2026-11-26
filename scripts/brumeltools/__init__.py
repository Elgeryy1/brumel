# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""Shared helpers for Brumel's build tooling (fetch.py, patches.py, build.py).

Standard library only. Nothing in this module touches the network or a
Chromium checkout by itself: callers build a *plan* (a list of Step objects),
which is printed by default and executed only when the user passes --execute.
"""

from __future__ import annotations

import json
import os
import shlex
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
UPSTREAM_CONFIG = REPO_ROOT / "config" / "upstream.json"
PATCHES_DIR = REPO_ROOT / "patches"
GN_PROFILES_DIR = REPO_ROOT / "config" / "gn"
FEATURES_JSON = REPO_ROOT / "docs" / "product" / "catalog" / "features.json"

IS_WINDOWS = sys.platform == "win32"


class ToolError(Exception):
    """A user-facing error: printed without a traceback, exit status 2."""


# --------------------------------------------------------------------------- #
# Upstream configuration
# --------------------------------------------------------------------------- #

def parse_version(version: str) -> tuple[int, ...]:
    """Turn '158.0.8127.88' into (158, 0, 8127, 88)."""
    parts = str(version).strip().split(".")
    if len(parts) != 4 or not all(p.isdigit() for p in parts):
        raise ToolError(f"not a Chromium version: {version!r}")
    return tuple(int(p) for p in parts)


@dataclass(frozen=True)
class UpstreamPin:
    version: str
    repository: str
    revision: str | None
    ungoogled_tag: str | None
    platforms: tuple[str, ...]

    @property
    def tag_ref(self) -> str:
        return f"refs/tags/{self.version}"


def load_pin(path: Path = UPSTREAM_CONFIG) -> UpstreamPin:
    try:
        with path.open(encoding="utf-8") as fh:
            config = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        raise ToolError(f"cannot read {path}: {exc}") from exc
    try:
        chromium = config["chromium"]
        version = chromium["version"]
        repository = chromium["repository"]
    except (KeyError, TypeError) as exc:
        raise ToolError(f"{path}: missing chromium.version or chromium.repository") from exc
    parse_version(version)
    if not str(repository).startswith("https://"):
        raise ToolError(f"{path}: chromium.repository must be an https URL")
    revision = chromium.get("revision")
    if revision is not None and not _is_sha1(revision):
        raise ToolError(f"{path}: chromium.revision must be a 40-character hex commit or null")
    ungoogled = config.get("ungoogled_chromium") or {}
    tag = ungoogled.get("tag")
    if tag is not None and not str(tag).startswith(version + "-"):
        raise ToolError(
            f"{path}: ungoogled_chromium.tag {tag!r} does not match chromium.version {version!r}"
        )
    platforms = tuple(config.get("platforms") or ("Windows", "Linux"))
    return UpstreamPin(version, repository, revision, tag, platforms)


def _is_sha1(value: object) -> bool:
    return isinstance(value, str) and len(value) == 40 and all(c in "0123456789abcdef" for c in value)


# --------------------------------------------------------------------------- #
# Plans: printable, testable lists of commands
# --------------------------------------------------------------------------- #

@dataclass
class Step:
    """One action of a plan. Either a command (argv) or a Python callable."""

    description: str
    argv: list[str] | None = None
    cwd: Path | None = None
    env: dict[str, str] = field(default_factory=dict)
    action: object = None  # callable taking no arguments, for file writes

    def render(self) -> str:
        lines = [f"- {self.description}"]
        if self.argv is not None:
            prefix = "".join(f"{k}={v} " for k, v in sorted(self.env.items()))
            where = f"  (in {self.cwd})" if self.cwd else ""
            lines.append(f"    $ {prefix}{join_command(self.argv)}{where}")
        return "\n".join(lines)


def join_command(argv: list[str]) -> str:
    if IS_WINDOWS:
        return subprocess.list2cmdline(argv)
    return shlex.join(argv)


def print_plan(title: str, steps: list[Step], execute: bool) -> None:
    print(title)
    for step in steps:
        print(step.render())
    if not execute:
        print("\nPlan only: nothing was run. Re-run with --execute to perform these steps.")


def run_plan(steps: list[Step]) -> None:
    for number, step in enumerate(steps, start=1):
        print(f"\n[{number}/{len(steps)}] {step.description}", flush=True)
        if step.action is not None:
            step.action()
        if step.argv is not None:
            env = os.environ.copy()
            env.update(step.env)
            argv = resolve_executable(step.argv)
            result = subprocess.run(argv, cwd=step.cwd, env=env)
            if result.returncode != 0:
                raise ToolError(
                    f"step {number} failed with exit status {result.returncode}: "
                    f"{join_command(step.argv)}"
                )


def resolve_executable(argv: list[str]) -> list[str]:
    """Resolve argv[0] through PATH (and PATHEXT on Windows, e.g. gclient.bat)."""
    found = shutil.which(argv[0])
    return [found or argv[0], *argv[1:]]


def require_tools(names: list[str]) -> list[str]:
    """Return the names of tools that are not on PATH."""
    return [name for name in names if shutil.which(name) is None]


def git(args: list[str], cwd: Path, check: bool = True) -> str:
    """Run git and return stdout as text. Used for read-only queries and small writes."""
    result = subprocess.run(
        ["git", *args], cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    if check and result.returncode != 0:
        raise ToolError(f"git {' '.join(args)} failed: {result.stderr.strip() or result.stdout.strip()}")
    return result.stdout


def free_gigabytes(path: Path) -> float:
    probe = path
    while not probe.exists() and probe != probe.parent:
        probe = probe.parent
    return shutil.disk_usage(probe).free / 1024**3


def toolchain_env() -> dict[str, str]:
    """Environment needed by depot_tools outside Google.

    On Windows, DEPOT_TOOLS_WIN_TOOLCHAIN=0 makes depot_tools use the locally
    installed Visual Studio instead of Google's internal toolchain package.
    """
    return {"DEPOT_TOOLS_WIN_TOOLCHAIN": "0"} if IS_WINDOWS else {}


def main_wrapper(main) -> int:
    try:
        return main()
    except ToolError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("interrupted", file=sys.stderr)
        return 130
