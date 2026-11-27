#!/usr/bin/env python3
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""Render the body of the "Upstream update available" tracking issue (CORE-003, #64).

Input is the JSON printed by check_upstream.py --json and, optionally, the JSON
list of ungoogled-chromium tags from the GitHub API. Every version string is
validated before it is written, so untrusted API data cannot inject Markdown.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_upstream import parse_version  # noqa: E402

TITLE = "Upstream update available"
MARKER = "<!-- brumel:upstream-check -->"
STATUS_TEXT = {
    "up-to-date": "up to date",
    "behind": "behind (same major: likely a security respin)",
    "major-behind": "behind by a major version",
    "ahead": "ahead of stable (check the pin)",
}


def safe_version(value: object) -> str:
    version = str(value)
    parse_version(version)  # raises ValueError for anything that is not a.b.c.d
    return version


def ungoogled_versions(tags: list) -> set[str]:
    """Chromium versions that have an ungoogled-chromium tag ('<version>-<revision>')."""
    versions = set()
    for tag in tags:
        name = str(tag.get("name", "")) if isinstance(tag, dict) else ""
        base, sep, revision = name.rpartition("-")
        if sep and revision.isdigit():
            try:
                versions.add(safe_version(base))
            except ValueError:
                continue
    return versions


def render(check: dict, tags: list | None) -> str:
    pinned = safe_version(check["pinned"])
    available = ungoogled_versions(tags) if tags is not None else None
    lines = [
        MARKER,
        f"The pinned Chromium version **{pinned}** (`config/upstream.json`) is not the latest stable "
        "release on every platform Brumel targets.",
        "",
        "| Platform | Latest stable | Status | ungoogled-chromium tag |",
        "|---|---|---|---|",
    ]
    for result in check["results"]:
        platform = str(result["platform"])
        if platform not in ("Windows", "Linux", "Mac", "Android"):
            raise ValueError(f"unexpected platform {platform!r}")
        version = safe_version(result["version"])
        status = STATUS_TEXT.get(str(result["status"]), "unknown")
        if available is None:
            tag = "not checked"
        else:
            tag = "available" if version in available else "not yet"
        lines.append(f"| {platform} | {version} | {status} | {tag} |")
    lines += [
        "",
        "### What to do",
        "",
        "1. Decide the new pin following the pin policy ([#65](https://github.com/Elgeryy1/brumel/issues/65)): "
        "prefer a version with a matching ungoogled-chromium tag; for an exploited vulnerability, do not wait for it.",
        "2. Update `config/upstream.json`, fetch, apply the series with `scripts/patches.py apply --3way`, "
        "refresh conflicting patches and build.",
        "3. Record the rebase time ([Upstream Strategy, metrics](https://github.com/Elgeryy1/brumel/blob/main/docs/architecture/UPSTREAM_STRATEGY.md#8-metrics)).",
        "",
        "_This issue is opened and updated by the scheduled `Upstream check` workflow. It closes itself when the pin "
        "matches the latest stable release again._",
    ]
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("check_json", type=Path, help="output of check_upstream.py --json")
    parser.add_argument("--ungoogled-tags", type=Path, help="GitHub API tag list for ungoogled-chromium")
    args = parser.parse_args(argv)
    check = json.loads(args.check_json.read_text(encoding="utf-8"))
    tags = None
    if args.ungoogled_tags and args.ungoogled_tags.is_file():
        try:
            loaded = json.loads(args.ungoogled_tags.read_text(encoding="utf-8"))
            tags = loaded if isinstance(loaded, list) else None
        except json.JSONDecodeError:
            tags = None
    sys.stdout.write(render(check, tags))
    return 0


if __name__ == "__main__":
    sys.exit(main())
