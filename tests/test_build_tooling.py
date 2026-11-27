# SPDX-License-Identifier: MPL-2.0
# Copyright (c) The Brumel Authors
"""Unit tests for scripts/fetch.py, scripts/patches.py and scripts/build.py.

Nothing here downloads Chromium. Git-based tests run against tiny temporary
repositories with an isolated Git configuration.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import brumeltools  # noqa: E402
import build  # noqa: E402
import fetch  # noqa: E402
import patches  # noqa: E402

HAS_GIT = shutil.which("git") is not None

DIFF = b"""diff --git a/hello.txt b/hello.txt
--- a/hello.txt
+++ b/hello.txt
@@ -1,3 +1,3 @@
 line one
--- not a header, a removed line
+line two
 line three
"""

GOOD_HEADER = """Description: Change the second line.
Origin: brumel
Module: core
Feature: n/a
Upstreamable: no
SPDX-License-Identifier: BSD-3-Clause
"""


def write_patch(patches_dir: Path, rel: str, header: str = GOOD_HEADER, diff: bytes = DIFF) -> None:
    path = patches_dir / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(header.encode() + b"\n" + diff)


def write_series(patches_dir: Path, *entries: str) -> None:
    patches_dir.mkdir(parents=True, exist_ok=True)
    (patches_dir / "series").write_text("# test series\n" + "".join(e + "\n" for e in entries), encoding="utf-8")


class IsolatedGit:
    """Point Git at empty configuration so the developer's settings do not leak in."""

    def __enter__(self):
        self.tmp = tempfile.TemporaryDirectory()
        empty = Path(self.tmp.name) / "gitconfig"
        empty.write_text("", encoding="utf-8")
        self.patcher = mock.patch.dict(os.environ, {
            "GIT_CONFIG_GLOBAL": str(empty), "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_AUTHOR_NAME": "Test", "GIT_AUTHOR_EMAIL": "test@example.invalid",
            "GIT_COMMITTER_NAME": "Test", "GIT_COMMITTER_EMAIL": "test@example.invalid",
        })
        self.patcher.start()
        return self

    def __exit__(self, *exc):
        self.patcher.stop()
        self.tmp.cleanup()


def run_git(cwd: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout


def make_repo(path: Path) -> Path:
    path.mkdir(parents=True)
    run_git(path, "init", "--quiet", "--initial-branch=main")
    (path / "hello.txt").write_bytes(b"line one\n-- not a header, a removed line\nline three\n")
    run_git(path, "add", "hello.txt")
    run_git(path, "commit", "--quiet", "-m", "base")
    return path


# --------------------------------------------------------------------------- #
# brumeltools / fetch.py
# --------------------------------------------------------------------------- #

class UpstreamPinTests(unittest.TestCase):
    def write_config(self, tmp: Path, **chromium) -> Path:
        data = {
            "chromium": {"version": "158.0.8127.88",
                         "repository": "https://chromium.googlesource.com/chromium/src.git", **chromium},
            "ungoogled_chromium": {"tag": "158.0.8127.88-1"},
        }
        path = tmp / "upstream.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def test_repository_pin_is_valid(self):
        pin = brumeltools.load_pin()
        self.assertEqual(pin.tag_ref, f"refs/tags/{pin.version}")

    def test_rejects_bad_version_and_revision(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(brumeltools.ToolError):
                brumeltools.load_pin(self.write_config(Path(tmp), version="158.0"))
            with self.assertRaises(brumeltools.ToolError):
                brumeltools.load_pin(self.write_config(Path(tmp), revision="abc"))
            pin = brumeltools.load_pin(self.write_config(Path(tmp), revision="a" * 40))
            self.assertEqual(pin.revision, "a" * 40)

    def test_rejects_ungoogled_tag_for_another_version(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_config(Path(tmp), version="159.0.8154.34")
            with self.assertRaises(brumeltools.ToolError):
                brumeltools.load_pin(path)


class FetchTests(unittest.TestCase):
    pin = brumeltools.UpstreamPin("158.0.8127.88", "https://chromium.googlesource.com/chromium/src.git",
                                  None, "158.0.8127.88-1", ("Windows", "Linux"))

    def test_gclient_file_is_python_with_unmanaged_solution(self):
        text = fetch.gclient_file(self.pin, ["win", "linux"])
        scope: dict = {}
        exec(compile(text, ".gclient", "exec"), scope)  # .gclient files are Python
        self.assertEqual(scope["solutions"][0]["name"], "src")
        self.assertIs(scope["solutions"][0]["managed"], False)
        self.assertEqual(scope["target_os"], ["linux", "win"])

    def test_plan_clones_the_pinned_tag(self):
        with tempfile.TemporaryDirectory() as tmp:
            steps = fetch.build_plan(Path(tmp) / "c", self.pin, 4, [])
            clone = next(s for s in steps if s.argv and "clone" in s.argv)
            self.assertIn("--depth", clone.argv)
            self.assertEqual(clone.argv[clone.argv.index("--branch") + 1], "158.0.8127.88")
            sync = next(s for s in steps if s.argv and "sync" in s.argv)
            self.assertIn("--no-history", sync.argv)
            self.assertIn("--nohooks", sync.argv)

    def test_plan_skips_clone_when_src_exists(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "src" / ".git").mkdir(parents=True)
            steps = fetch.build_plan(Path(tmp), self.pin, 4, [])
            self.assertFalse(any(s.argv and "clone" in s.argv for s in steps))

    def test_preflight_reports_disk_tools_and_spaces(self):
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.object(fetch, "require_tools", return_value=["gclient"]), \
                 mock.patch.object(fetch, "free_gigabytes", return_value=10.0):
                errors, _ = fetch.preflight(Path(tmp) / "with space", self.pin, 100)
            text = "\n".join(errors)
            self.assertIn("gclient", text)
            self.assertIn("10 GB free", text)
            self.assertIn("spaces", text)

    def test_refuses_checkout_inside_repository(self):
        with self.assertRaises(brumeltools.ToolError):
            fetch.main(["--checkout", str(ROOT / "chromium")])

    @unittest.skipUnless(HAS_GIT, "git not available")
    def test_record_state_checks_pinned_revision(self):
        with IsolatedGit(), tempfile.TemporaryDirectory() as tmp:
            checkout = Path(tmp)
            src = make_repo(checkout / "src")
            head = run_git(src, "rev-parse", "HEAD").strip()
            state = fetch.record_state(checkout, self.pin)
            self.assertEqual(state["revision"], head)
            self.assertTrue((checkout / ".brumel" / "fetch.json").is_file())
            wrong = brumeltools.UpstreamPin(self.pin.version, self.pin.repository, "0" * 40, None, ())
            with self.assertRaises(brumeltools.ToolError):
                fetch.record_state(checkout, wrong)


# --------------------------------------------------------------------------- #
# patches.py
# --------------------------------------------------------------------------- #

class PatchParsingTests(unittest.TestCase):
    def test_counts_lines_inside_hunks(self):
        patch = patches.parse_patch("brumel/core/0001-x.patch", GOOD_HEADER.encode() + b"\n" + DIFF)
        self.assertEqual(patch.fields["Module"], "core")
        self.assertEqual(patch.files, ["hello.txt"])
        self.assertEqual((patch.added, patch.removed, patch.hunks), (1, 1, 1))

    def test_hunk_lines_ignore_index_lines(self):
        with_index = DIFF.replace(b"--- a/", b"index 1111111..2222222 100644\n--- a/", 1)
        self.assertEqual(patches.hunk_lines(DIFF), patches.hunk_lines(with_index))


class PatchCheckTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name) / "patches"
        self.features = {"CORE-002"}

    def tearDown(self):
        self._tmp.cleanup()

    def errors(self):
        return patches.check_series(self.dir, self.features)

    def test_empty_series_is_valid(self):
        self.dir.mkdir()
        self.assertEqual(self.errors(), [])

    def test_valid_patch(self):
        write_patch(self.dir, "brumel/core/0001-change-line.patch",
                    GOOD_HEADER.replace("Feature: n/a", "Feature: CORE-002"))
        write_series(self.dir, "brumel/core/0001-change-line.patch")
        self.assertEqual(self.errors(), [])

    def test_header_problems(self):
        bad = (GOOD_HEADER.replace("Module: core", "Module: engine")
               .replace("BSD-3-Clause", "MPL-2.0")
               .replace("Feature: n/a", "Feature: CORE-999")
               .replace("Change the second line.", "TODO"))
        write_patch(self.dir, "brumel/core/0001-change-line.patch", bad)
        write_series(self.dir, "brumel/core/0001-change-line.patch")
        text = "\n".join(self.errors())
        for expected in ("does not match directory", "BSD-3-Clause", "CORE-999", "TODO"):
            self.assertIn(expected, text)

    def test_naming_orphans_and_duplicates(self):
        write_patch(self.dir, "brumel/core/change-line.patch")
        write_patch(self.dir, "brumel/core/0002-orphan.patch")
        write_series(self.dir, "brumel/core/change-line.patch", "brumel/core/change-line.patch")
        text = "\n".join(self.errors())
        self.assertIn("NNNN-short-kebab-name", text)
        self.assertIn("not listed", text)
        self.assertIn("more than once", text)

    def test_missing_file_and_bad_location(self):
        write_patch(self.dir, "elsewhere/0001-x.patch")
        write_series(self.dir, "elsewhere/0001-x.patch", "brumel/core/0009-missing.patch")
        text = "\n".join(self.errors())
        self.assertIn("does not exist", text)
        self.assertIn("brumel/ or upstream-ungoogled/", text)

    def test_imported_patch_needs_origin(self):
        write_patch(self.dir, "upstream-ungoogled/core/x.patch", "# imported\n")
        write_series(self.dir, "upstream-ungoogled/core/x.patch")
        self.assertIn("Origin", "\n".join(self.errors()))

    def test_security_pattern_needs_a_note(self):
        diff = DIFF.replace(b"+line two", b"+  command_line->AppendSwitch(switches::kNoSandbox);")
        write_patch(self.dir, "brumel/core/0001-change-line.patch", diff=diff)
        write_series(self.dir, "brumel/core/0001-change-line.patch")
        self.assertIn("kNoSandbox", "\n".join(self.errors()))
        write_patch(self.dir, "brumel/core/0001-change-line.patch",
                    GOOD_HEADER + "Security-Note: test-only switch list, not used at runtime.\n", diff)
        self.assertEqual(self.errors(), [])

    def test_repository_series_is_valid(self):
        self.assertEqual(patches.check_series(patches.PATCHES_DIR, patches.load_feature_ids(patches.FEATURES_JSON)), [])

    def test_stats(self):
        write_patch(self.dir, "brumel/core/0001-change-line.patch")
        write_series(self.dir, "brumel/core/0001-change-line.patch")
        loaded, errors = patches.load_patches(self.dir)
        self.assertEqual(errors, [])
        result = patches.stats(loaded)
        self.assertEqual(result["modified_upstream_files"], 1)
        self.assertEqual(result["by_category"], {"brumel/core": 1})


@unittest.skipUnless(HAS_GIT, "git not available")
class PatchApplyRefreshTests(unittest.TestCase):
    def setUp(self):
        self._git = IsolatedGit().__enter__()
        self._tmp = tempfile.TemporaryDirectory()
        tmp = Path(self._tmp.name)
        self.src = make_repo(tmp / "checkout" / "src")
        self.dir = tmp / "patches"
        write_patch(self.dir, "brumel/core/0001-change-line.patch")
        write_series(self.dir, "brumel/core/0001-change-line.patch")

    def tearDown(self):
        self._tmp.cleanup()
        self._git.__exit__(None, None, None)

    def apply(self, **kwargs):
        steps, _ = patches.plan_apply(self.src, self.dir, three_way=False, reset=kwargs.get("reset", False))
        brumeltools.run_plan(steps)
        return steps

    def test_apply_is_reproducible_and_resumable(self):
        self.apply()
        self.assertEqual((self.src / "hello.txt").read_text(), "line one\nline two\nline three\n")
        commits = patches.applied_commits(self.src)
        self.assertEqual([t for _, t in commits], ["brumel/core/0001-change-line.patch"])
        first_sha = commits[0][0]
        # Nothing left to do on a second run.
        steps, _ = patches.plan_apply(self.src, self.dir, False, False)
        self.assertEqual(steps, [])
        # Reset and apply again: fixed commit metadata gives the same commit ID.
        self.apply(reset=True)
        self.assertEqual(patches.applied_commits(self.src)[0][0], first_sha)

    def test_dirty_tree_is_refused(self):
        self.apply()
        (self.src / "hello.txt").write_text("changed\n")
        with self.assertRaises(brumeltools.ToolError):
            patches.plan_apply(self.src, self.dir, False, False)

    def test_refresh_updates_and_adds_patches(self):
        self.apply()
        steps, notes = patches.plan_refresh(self.src, self.dir)
        self.assertEqual(steps, [])
        self.assertIn("all patches are up to date", notes)

        # Amend the patch commit, as after resolving a conflict.
        (self.src / "hello.txt").write_text("line one\nline 2\nline three\n")
        run_git(self.src, "commit", "--quiet", "-a", "--amend", "--no-edit")
        # A new commit that should become a new patch.
        (self.src / "new.txt").write_text("brand new\n")
        run_git(self.src, "add", "new.txt")
        run_git(self.src, "commit", "--quiet", "-m", "add file", "-m",
                "Brumel-Patch: brumel/branding/0001-add-file.patch")

        steps, notes = patches.plan_refresh(self.src, self.dir)
        brumeltools.run_plan(steps)
        updated = (self.dir / "brumel/core/0001-change-line.patch").read_bytes()
        self.assertTrue(updated.startswith(GOOD_HEADER.encode()))
        self.assertIn(b"+line 2", updated)
        new_patch = (self.dir / "brumel/branding/0001-add-file.patch").read_text()
        self.assertIn("Module: branding", new_patch)
        self.assertEqual(patches.read_series(self.dir),
                         ["brumel/core/0001-change-line.patch", "brumel/branding/0001-add-file.patch"])
        # The new patch still has a TODO description, so check fails until it is filled in.
        self.assertIn("TODO", "\n".join(patches.check_series(self.dir, set())))

    def test_refresh_refuses_commits_without_trailer(self):
        self.apply()
        (self.src / "other.txt").write_text("x\n")
        run_git(self.src, "add", "other.txt")
        run_git(self.src, "commit", "--quiet", "-m", "no trailer")
        with self.assertRaises(brumeltools.ToolError):
            patches.plan_refresh(self.src, self.dir)


# A patch that changes src/ and a nested DEPS repository at third_party/dep/src.
NESTED_DIFF = DIFF + b"""--- a/third_party/dep/src/dep.txt
+++ b/third_party/dep/src/dep.txt
@@ -1,2 +1,2 @@
 dep one
-dep two
+dep 2
"""
NESTED_ONLY_DIFF = b"""diff --git a/third_party/dep/src/other.txt b/third_party/dep/src/other.txt
new file mode 100644
--- /dev/null
+++ b/third_party/dep/src/other.txt
@@ -0,0 +1 @@
+other
"""


class PatchSplitTests(unittest.TestCase):
    def test_sections_follow_hunk_counts(self):
        _, sections = patches.split_sections(NESTED_DIFF)
        self.assertEqual([path for path, _ in sections], ["hello.txt", "third_party/dep/src/dep.txt"])
        # The removed line '--- not a header' stays inside the first section.
        self.assertIn(b"--- not a header, a removed line\n", sections[0][1])

    def test_new_file_section_takes_its_path_from_plus_line(self):
        _, sections = patches.split_sections(NESTED_ONLY_DIFF)
        self.assertEqual(sections[0][0], "third_party/dep/src/other.txt")

    def test_same_changes_ignores_file_order(self):
        _, sections = patches.split_sections(NESTED_DIFF)
        reordered = b"".join(sections[1][1]) + b"".join(sections[0][1])
        self.assertTrue(patches.same_changes(NESTED_DIFF, reordered))
        self.assertFalse(patches.same_changes(NESTED_DIFF, DIFF))


@unittest.skipUnless(HAS_GIT, "git not available")
class NestedRepositoryTests(unittest.TestCase):
    def setUp(self):
        self._git = IsolatedGit().__enter__()
        self._tmp = tempfile.TemporaryDirectory()
        tmp = Path(self._tmp.name)
        self.src = make_repo(tmp / "checkout" / "src")
        # src ignores its nested DEPS repositories, as chromium/src does.
        (self.src / ".gitignore").write_text("/third_party/dep/src/\n")
        run_git(self.src, "add", ".gitignore")
        run_git(self.src, "commit", "--quiet", "-m", "ignore deps")
        self.dep = self.src / "third_party" / "dep" / "src"
        self.dep.mkdir(parents=True)
        run_git(self.dep, "init", "--quiet", "--initial-branch=main")
        (self.dep / "dep.txt").write_bytes(b"dep one\ndep two\n")
        run_git(self.dep, "add", "dep.txt")
        run_git(self.dep, "commit", "--quiet", "-m", "dep base")
        self.dir = tmp / "patches"
        write_patch(self.dir, "brumel/core/0001-both.patch", diff=NESTED_DIFF)
        write_patch(self.dir, "brumel/core/0002-dep-only.patch", diff=NESTED_ONLY_DIFF)
        write_series(self.dir, "brumel/core/0001-both.patch", "brumel/core/0002-dep-only.patch")

    def tearDown(self):
        self._tmp.cleanup()
        self._git.__exit__(None, None, None)

    def apply(self, reset=False):
        steps, notes = patches.plan_apply(self.src, self.dir, three_way=False, reset=reset)
        brumeltools.run_plan(steps)
        return notes

    def test_split_by_repo_strips_the_repository_prefix(self):
        parts = patches.split_by_repo(self.src, NESTED_DIFF)
        self.assertEqual([repo for repo, _ in parts], ["", "third_party/dep/src"])
        self.assertIn(b"--- a/dep.txt\n+++ b/dep.txt\n", parts[1][1])
        self.assertNotIn(b"third_party", parts[1][1])

    def test_apply_commits_in_each_repository(self):
        self.apply()
        self.assertEqual((self.dep / "dep.txt").read_text(), "dep one\ndep 2\n")
        self.assertEqual((self.dep / "other.txt").read_text(), "other\n")
        self.assertEqual((self.src / "hello.txt").read_text(), "line one\nline two\nline three\n")
        # src keeps one commit per patch, even for a patch that does not touch it.
        self.assertEqual([t for _, t in patches.applied_commits(self.src)],
                         ["brumel/core/0001-both.patch", "brumel/core/0002-dep-only.patch"])
        self.assertEqual([t for _, t in patches.applied_commits(self.dep)],
                         ["brumel/core/0001-both.patch", "brumel/core/0002-dep-only.patch"])
        self.assertEqual(patches.read_patch_repos(self.src), ["third_party/dep/src"])
        # Nothing left to do, and the patch files are already up to date.
        self.assertEqual(patches.plan_apply(self.src, self.dir, False, False)[0], [])
        steps, notes = patches.plan_refresh(self.src, self.dir)
        self.assertEqual(steps, [])
        self.assertIn("all patches are up to date", notes)

    def test_reset_restores_nested_repositories_and_ids_repeat(self):
        self.apply()
        dep_head = run_git(self.dep, "rev-parse", "HEAD")
        self.apply(reset=True)
        self.assertEqual(run_git(self.dep, "rev-parse", "HEAD"), dep_head)

    def test_resume_skips_parts_already_committed(self):
        # Simulate a stop after the nested part of 0001 was committed, before src's commit.
        steps, _ = patches.plan_apply(self.src, self.dir, False, False)
        upto = next(i for i, s in enumerate(steps) if s.description == "Commit brumel/core/0001-both.patch in third_party/dep/src")
        brumeltools.run_plan(steps[: upto + 1])
        steps, notes = patches.plan_apply(self.src, self.dir, False, False)
        self.assertTrue(any("already committed there" in n for n in notes))
        brumeltools.run_plan(steps)
        self.assertEqual(len(patches.applied_commits(self.dep)), 2)
        self.assertEqual((self.src / "hello.txt").read_text(), "line one\nline two\nline three\n")

    def test_refresh_joins_nested_changes_with_their_prefix(self):
        self.apply()
        (self.dep / "dep.txt").write_bytes(b"dep one\ndep two, edited\n")
        run_git(self.dep, "commit", "--quiet", "-a", "--fixup=HEAD~1")
        run_git(self.dep, "-c", "sequence.editor=true", "rebase", "--quiet", "-i", "--autosquash",
                patches.BASE_REF)
        steps, notes = patches.plan_refresh(self.src, self.dir)
        self.assertIn("update brumel/core/0001-both.patch", notes)
        brumeltools.run_plan(steps)
        text = (self.dir / "brumel/core/0001-both.patch").read_bytes()
        self.assertTrue(text.startswith(GOOD_HEADER.encode()))
        self.assertIn(b"+++ b/third_party/dep/src/dep.txt", text)
        self.assertIn(b"+dep two, edited", text)
        self.assertIn(b"+line two", text)

    def test_nested_commit_without_src_ledger_is_refused(self):
        self.apply()
        (self.dep / "x.txt").write_text("x\n")
        run_git(self.dep, "add", "x.txt")
        run_git(self.dep, "commit", "--quiet", "-m", "x", "-m", "Brumel-Patch: brumel/core/0003-x.patch")
        with self.assertRaises(brumeltools.ToolError):
            patches.plan_refresh(self.src, self.dir)


# --------------------------------------------------------------------------- #
# build.py
# --------------------------------------------------------------------------- #

class BuildProfileTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)
        self.write("_base", "use_official_google_api_keys = false\nis_debug = true\n")

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, name, text):
        (self.dir / f"{name}.gn").write_text(text, encoding="utf-8")

    def test_inheritance_and_override(self):
        self.write("child", "# brumel-inherit: _base\nis_debug = false  # inline comment\nsymbol_level = 0\n")
        profile = build.load_profile("child", self.dir)
        self.assertEqual(profile.args["is_debug"], "false")
        self.assertEqual(list(profile.args)[-1], "symbol_level")
        self.assertEqual(profile.sources, ["_base.gn", "child.gn"])
        self.assertEqual(build.guard(profile), [])

    def test_cycle_is_detected(self):
        self.write("a", "# brumel-inherit: b\n")
        self.write("b", "# brumel-inherit: a\n")
        with self.assertRaises(brumeltools.ToolError):
            build.load_profile("a", self.dir)

    def test_guard_rejects_keys_and_weakened_hardening(self):
        self.write("bad", '# brumel-inherit: _base\ngoogle_api_key = "x"\nis_cfi = false\n'
                          "use_official_google_api_keys = true\nis_official_build = true\n")
        text = "\n".join(build.guard(build.load_profile("bad", self.dir)))
        for expected in ("google_api_key", "is_cfi", "use_official_google_api_keys", "is_debug", "is_component_build"):
            self.assertIn(expected, text)

    def test_invalid_line(self):
        self.write("broken", "this is not gn\n")
        with self.assertRaises(brumeltools.ToolError):
            build.load_profile("broken", self.dir)

    def test_repository_profiles_pass_the_guard(self):
        names = build.buildable_profiles()
        self.assertEqual(names, ["dev", "minimal", "release"])
        for name in names:
            self.assertEqual(build.guard(build.load_profile(name)), [], name)
        release = build.load_profile("release")
        self.assertEqual(release.args["is_official_build"], "true")

    def test_plan_build(self):
        profile = build.load_profile("dev")
        steps = build.plan_build(self.dir, profile, ["chrome"], build=True)
        self.assertEqual(steps[1].argv, ["gn", "gen", "out/Dev"])
        self.assertEqual(steps[2].argv, ["autoninja", "-C", "out/Dev", "chrome"])
        limited = build.plan_build(self.dir, profile, ["chrome"], build=True, jobs=8)
        self.assertEqual(limited[2].argv, ["autoninja", "-j", "8", "-C", "out/Dev", "chrome"])
        limited[0].action()
        self.assertIn("action_pool_depth = 8", (self.dir / "out" / "Dev" / "args.gn").read_text(encoding="utf-8"))
        with self.assertRaises(SystemExit), mock.patch("sys.stderr"):
            build.parse_args(["build", "--checkout", ".", "--profile", "dev", "--jobs", "0"])
        steps[0].action()
        written = (self.dir / "out" / "Dev" / "args.gn").read_text(encoding="utf-8")
        self.assertIn("is_component_build = true", written)

    def test_profiles_that_use_the_overlay_need_it_in_the_checkout(self):
        profile = build.load_profile("release")
        self.assertEqual(build.overlay_files(profile), ["//brumel/branding/BRANDING"])
        self.assertEqual(build.missing_overlay_files(self.dir, profile), ["//brumel/branding/BRANDING"])
        (self.dir / "brumel" / "branding").mkdir(parents=True)
        (self.dir / "brumel" / "branding" / "BRANDING").write_text("PRODUCT_FULLNAME=Brumel\n", encoding="utf-8")
        self.assertEqual(build.missing_overlay_files(self.dir, profile), [])

    def test_repository_branding_file_is_valid(self):
        # Chromium's build/util/version.py accepts only KEY=VALUE lines.
        lines = (ROOT / "src" / "branding" / "BRANDING").read_text(encoding="utf-8").splitlines()
        values = dict(line.split("=", 1) for line in lines)
        self.assertEqual(values["PRODUCT_FULLNAME"], "Brumel")
        self.assertIn("The Chromium Authors", values["COPYRIGHT"])


if __name__ == "__main__":
    unittest.main()
