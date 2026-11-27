# SPDX-License-Identifier: MPL-2.0
# Copyright (c) The Brumel Authors
"""Unit tests for scripts/upstream/render_issue.py (no network)."""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts" / "upstream"))

import render_issue  # noqa: E402

CHECK = {
    "pinned": "158.0.8127.88",
    "outdated": True,
    "results": [
        {"platform": "Windows", "version": "159.0.8154.34", "status": "major-behind"},
        {"platform": "Linux", "version": "158.0.8127.88", "status": "up-to-date"},
    ],
}
TAGS = [{"name": "158.0.8127.88-1"}, {"name": "157.0.8000.1-2"}, {"name": "not-a-tag"}, "junk"]


class RenderIssueTests(unittest.TestCase):
    def test_table_and_ungoogled_availability(self):
        body = render_issue.render(CHECK, TAGS)
        self.assertTrue(body.startswith(render_issue.MARKER))
        self.assertIn("| Windows | 159.0.8154.34 | behind by a major version | not yet |", body)
        self.assertIn("| Linux | 158.0.8127.88 | up to date | available |", body)

    def test_without_tags(self):
        self.assertIn("not checked", render_issue.render(CHECK, None))

    def test_rejects_untrusted_values(self):
        bad = {**CHECK, "results": [{"platform": "Windows", "version": "1.2.3.4 | [x](http://e)", "status": "behind"}]}
        with self.assertRaises(ValueError):
            render_issue.render(bad, None)
        bad_platform = {**CHECK, "results": [{"platform": "<b>x</b>", "version": "1.2.3.4", "status": "behind"}]}
        with self.assertRaises(ValueError):
            render_issue.render(bad_platform, None)

    def test_ungoogled_versions(self):
        self.assertEqual(render_issue.ungoogled_versions(TAGS), {"158.0.8127.88", "157.0.8000.1"})


if __name__ == "__main__":
    unittest.main()
