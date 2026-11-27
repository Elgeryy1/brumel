#!/usr/bin/env python3
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""Compose GN arguments and build Brumel from a prepared checkout.

Commands:

  check   Validate every profile in config/gn/ (no checkout needed; runs in CI).
  args    Print the composed args.gn for a profile.
  gen     Write out/<Profile>/args.gn in the checkout and run gn gen.
  build   gen, then autoninja the requested targets.

Profiles live in config/gn/<name>.gn. Files starting with "_" are shared
fragments and cannot be built. A profile inherits another with a line
"# brumel-inherit: <name>"; later values win.

The guard refuses profiles that add Google API keys, leave
use_official_google_api_keys enabled, or set security hardening arguments to
false. gen and build only print their plan unless --execute is given.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from brumeltools import (  # noqa: E402
    GN_PROFILES_DIR,
    Step,
    ToolError,
    main_wrapper,
    print_plan,
    run_plan,
    toolchain_env,
)

ARG_LINE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+?)\s*$")
INHERIT_LINE = re.compile(r"^#\s*brumel-inherit:\s*([A-Za-z0-9_-]+)\s*$")
PROFILE_NAME = re.compile(r"^[a-z][a-z0-9-]*$")

# Never allowed in any profile: Brumel does not ship Google API keys.
FORBIDDEN_ARGS = ("google_api_key", "google_default_client_id", "google_default_client_secret")
# Must have exactly these values after composition.
REQUIRED_VALUES = {"use_official_google_api_keys": "false"}
# Security hardening that must never be switched off (SECURITY.md, golden rule 2).
# Leaving them unset keeps upstream defaults, which is what Brumel wants.
HARDENING_ARGS = ("is_cfi", "use_cfi_icall", "v8_enable_sandbox", "v8_enable_pointer_compression",
                  "use_partition_alloc")
DEFAULT_TARGETS = ("chrome",)


@dataclass
class Profile:
    name: str
    args: dict[str, str]          # composed, in order
    sources: list[str]            # files that contributed, base first


def read_fragment(path: Path) -> tuple[list[str], list[tuple[str, str]]]:
    """Return (inherited profile names, [(key, value)]) for one file."""
    inherits: list[str] = []
    pairs: list[tuple[str, str]] = []
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        inherit = INHERIT_LINE.match(line)
        if inherit:
            inherits.append(inherit.group(1))
            continue
        if line.startswith("#"):
            continue
        match = ARG_LINE.match(line)
        if not match:
            raise ToolError(f"{path.name}:{number}: expected 'name = value', got {raw!r}")
        value = match.group(2)
        if "#" in value and not value.startswith('"'):
            value = value.split("#", 1)[0].rstrip()
        pairs.append((match.group(1), value))
    return inherits, pairs


def load_profile(name: str, profiles_dir: Path = GN_PROFILES_DIR, _stack: tuple[str, ...] = ()) -> Profile:
    if name in _stack:
        raise ToolError("profile inheritance cycle: " + " -> ".join((*_stack, name)))
    path = profiles_dir / f"{name}.gn"
    if not path.is_file():
        raise ToolError(f"unknown profile {name!r} (no {path})")
    inherits, pairs = read_fragment(path)
    args: dict[str, str] = {}
    sources: list[str] = []
    for parent in inherits:
        base = load_profile(parent, profiles_dir, (*_stack, name))
        args.update(base.args)
        sources += [s for s in base.sources if s not in sources]
    for key, value in pairs:
        args.pop(key, None)  # keep the final position of the overriding value
        args[key] = value
    sources.append(path.name)
    return Profile(name, args, sources)


def buildable_profiles(profiles_dir: Path = GN_PROFILES_DIR) -> list[str]:
    return sorted(p.stem for p in profiles_dir.glob("*.gn") if not p.stem.startswith("_"))


def guard(profile: Profile) -> list[str]:
    errors = []
    args = profile.args
    for key in FORBIDDEN_ARGS:
        if key in args:
            errors.append(f"{profile.name}: {key} must not be set (Brumel uses no Google API keys)")
    for key, value in REQUIRED_VALUES.items():
        if args.get(key) != value:
            errors.append(f"{profile.name}: {key} must be {value}")
    for key in HARDENING_ARGS:
        if args.get(key) == "false":
            errors.append(f"{profile.name}: {key} = false turns off security hardening; not allowed")
    if args.get("is_official_build") == "true":
        if args.get("is_debug") != "false":
            errors.append(f"{profile.name}: official builds need is_debug = false")
        if args.get("is_component_build") != "false":
            errors.append(f"{profile.name}: official builds need is_component_build = false")
    return errors


OVERLAY_PATH = re.compile(r'"(//brumel/[^"]+)"')


def overlay_files(profile: Profile) -> list[str]:
    """GN paths into the //brumel overlay that a profile refers to."""
    return [m.group(1) for value in profile.args.values() for m in OVERLAY_PATH.finditer(value)]


def missing_overlay_files(src: Path, profile: Profile) -> list[str]:
    return [path for path in overlay_files(profile) if not (src / path[2:]).exists()]


def compose_args_gn(profile: Profile, jobs: int | None = None) -> str:
    lines = [
        f"# Generated by brumel scripts/build.py from config/gn/ ({', '.join(profile.sources)}).",
        "# Edit the profile in the Brumel repository, not this file.",
    ]
    lines += [f"{key} = {value}" for key, value in profile.args.items()]
    if jobs:
        # GN actions (code generators, TypeScript checks) run in their own pool,
        # one per CPU thread by default, which -j does not limit. Machine-local.
        lines += ["# From --jobs: limits parallel GN actions as well as compile jobs.",
                  f"action_pool_depth = {jobs}"]
    return "\n".join(lines) + "\n"


def out_dir_name(profile: str) -> str:
    return "out/" + profile.capitalize()


def resolve_src(path: Path) -> Path:
    for candidate in (path / "src", path):
        if (candidate / "BUILD.gn").is_file() and (candidate / ".gn").is_file():
            return candidate
    raise ToolError(f"{path} does not look like a Chromium src checkout (no .gn and BUILD.gn)")


def plan_build(src: Path, profile: Profile, targets: list[str], build: bool, jobs: int | None = None) -> list[Step]:
    out = out_dir_name(profile.name)
    args_path = src / out / "args.gn"
    content = compose_args_gn(profile, jobs)
    env = toolchain_env()

    def write_args() -> None:
        args_path.parent.mkdir(parents=True, exist_ok=True)
        args_path.write_text(content, encoding="utf-8", newline="\n")

    steps = [
        Step(f"Write {out}/args.gn from profile {profile.name}", action=write_args),
        Step(f"Generate build files in {out}", argv=["gn", "gen", out], cwd=src, env=env),
    ]
    if build:
        jobs_args = ["-j", str(jobs)] if jobs else []
        steps.append(Step(f"Build {' '.join(targets)}", argv=["autoninja", *jobs_args, "-C", out, *targets],
                          cwd=src, env=env))
    return steps


def positive_int(text: str) -> int:
    value = int(text)
    if value < 1:
        raise argparse.ArgumentTypeError("must be 1 or more")
    return value


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--profiles-dir", type=Path, default=GN_PROFILES_DIR, help=argparse.SUPPRESS)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="validate every profile")
    args_cmd = sub.add_parser("args", help="print the composed args.gn")
    args_cmd.add_argument("--profile", required=True)
    for name in ("gen", "build"):
        cmd = sub.add_parser(name, help=f"{name} a profile in a checkout")
        cmd.add_argument("--checkout", required=True, type=Path, help="gclient checkout root or its src/ directory")
        cmd.add_argument("--profile", required=True)
        cmd.add_argument("--execute", action="store_true", help="perform the plan instead of printing it")
        if name == "build":
            cmd.add_argument("--target", action="append", dest="targets", metavar="TARGET",
                             help=f"Ninja target (repeatable; default: {' '.join(DEFAULT_TARGETS)})")
            cmd.add_argument("--jobs", "-j", type=positive_int, metavar="N",
                             help="parallel compile jobs and GN actions (default: one per CPU thread). "
                                  "Lower it when the machine has little free memory")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    profiles_dir: Path = args.profiles_dir

    if args.command == "check":
        names = buildable_profiles(profiles_dir)
        errors = []
        for name in names:
            if not PROFILE_NAME.match(name):
                errors.append(f"{name}: profile names are lowercase kebab-case")
            errors += guard(load_profile(name, profiles_dir))
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        print(f"GN profiles: {', '.join(names) or 'none'}; {len(errors)} problem(s)")
        return 1 if errors else 0

    if args.profile.startswith("_"):
        raise ToolError(f"{args.profile} is a shared fragment, not a buildable profile")
    profile = load_profile(args.profile, profiles_dir)
    errors = guard(profile)
    if errors:
        raise ToolError("; ".join(errors))

    if args.command == "args":
        sys.stdout.write(compose_args_gn(profile))
        return 0

    src = resolve_src(args.checkout)
    missing = missing_overlay_files(src, profile)
    if missing:
        raise ToolError(
            f"profile {profile.name} needs {', '.join(missing)}, which is not in the checkout. "
            f"Run: python3 scripts/overlay.py sync --checkout {args.checkout} --execute"
        )
    targets = args.targets if args.command == "build" and args.targets else list(DEFAULT_TARGETS)
    steps = plan_build(src, profile, targets, build=args.command == "build",
                       jobs=getattr(args, "jobs", None))
    print_plan(f"{args.command} profile {profile.name} in {src}", steps, args.execute)
    if args.execute:
        run_plan(steps)
    return 0


if __name__ == "__main__":
    sys.exit(main_wrapper(main))
