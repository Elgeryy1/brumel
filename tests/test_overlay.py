# SPDX-License-Identifier: MPL-2.0
# Copyright (c) The Brumel Authors
"""Unit tests for scripts/overlay.py."""

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import brumeltools  # noqa: E402
import overlay  # noqa: E402

HEADER = "// SPDX-License-Identifier: MPL-2.0\n"


class OverlayTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        tmp = Path(self._tmp.name)
        self.source = tmp / "repo-src"
        self.checkout = tmp / "checkout" / "src"
        (self.checkout / ".git" / "info").mkdir(parents=True)
        (self.checkout / ".gn").write_text("", encoding="utf-8")
        self.write("browser/core/module_host.h", HEADER + "int a;\n")
        self.write("browser/core/BUILD.gn", "# SPDX-License-Identifier: MPL-2.0\n")

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel, text):
        path = self.source / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def sync(self):
        steps, counts = overlay.plan_sync(self.source, self.checkout)
        brumeltools.run_plan(steps)
        return counts

    def test_check(self):
        self.assertEqual(overlay.check_sources(self.source), [])
        self.write("browser/no_header.cc", "int b;\n")
        self.write("browser/aux.h", HEADER)
        text = "\n".join(overlay.check_sources(self.source))
        self.assertIn("no_header.cc", text)
        self.assertIn("reserved", text)

    def test_repository_src_is_valid(self):
        self.assertEqual(overlay.check_sources(overlay.OVERLAY_SOURCE), [])

    def test_sync_new_changed_deleted(self):
        counts = self.sync()
        self.assertEqual(counts["new"], 2)
        target = self.checkout / "brumel"
        self.assertTrue((target / "browser/core/module_host.h").is_file())
        self.assertIn("/brumel/", (self.checkout / ".git/info/exclude").read_text())

        self.write("browser/core/module_host.h", HEADER + "int changed;\n")
        (self.source / "browser/core/BUILD.gn").unlink()
        counts = self.sync()
        self.assertEqual((counts["changed"], counts["deleted"]), (1, 1))
        self.assertIn("changed", (target / "browser/core/module_host.h").read_text())
        self.assertFalse((target / "browser/core/BUILD.gn").exists())

        steps, counts = overlay.plan_sync(self.source, self.checkout)
        self.assertEqual(counts["unchanged"], 1)
        self.assertEqual(len(steps), 1)  # only the marker/exclude step
        exclude = (self.checkout / ".git/info/exclude").read_text().splitlines()
        self.sync()
        self.assertEqual((self.checkout / ".git/info/exclude").read_text().splitlines(), exclude)

    def test_refuses_foreign_directory(self):
        foreign = self.checkout / "brumel"
        foreign.mkdir()
        (foreign / "mine.txt").write_text("not ours", encoding="utf-8")
        with self.assertRaises(brumeltools.ToolError):
            overlay.plan_sync(self.source, self.checkout)


if __name__ == "__main__":
    unittest.main()
