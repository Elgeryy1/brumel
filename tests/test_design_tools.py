# SPDX-License-Identifier: MPL-2.0
# Copyright (c) 2026 Gerard Alvear and Brumel contributors.
"""Unit tests for the design tooling in scripts/design/."""

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / "design" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


surfaces = load("render_surfaces")
tokens = load("render_tokens")
icons = load("inline_icons")


def feature(fid, phase=2, status="Planned", duplicate_of=None):
    return {"id": fid, "phase": phase, "status": status, "duplicate_of": duplicate_of}


class SurfaceTests(unittest.TestCase):
    def setUp(self):
        self.features = {f["id"]: f for f in [
            feature("UI-001", phase=2), feature("CORE-004", phase=1, status="In Development"),
            feature("UI-020", duplicate_of="UI-019"), feature("UI-019", phase=3),
            feature("SHD-021", status="Rejected"),
        ]}
        self.data = {"zones": [{"id": "window", "title": "Main window"}], "surfaces": [
            {"id": "S-WIN-01", "zone": "window", "name": "Toolbar", "tech": "Views",
             "base": "Upstream", "features": ["UI-001", "CORE-004"]},
        ]}

    def test_valid_source_has_no_errors(self):
        self.assertEqual(surfaces.validate(self.data, self.features), [])

    def test_phase_is_the_earliest_and_status_is_counted(self):
        phase, status = surfaces.derive(self.data["surfaces"][0], self.features)
        self.assertEqual(phase, "Technical Foundation")
        self.assertEqual(status, "In Development 1, Planned 1")

    def test_unknown_rejected_and_duplicate_features_fail(self):
        self.data["surfaces"][0]["features"] = ["UI-999", "SHD-021", "UI-020"]
        errors = " ".join(surfaces.validate(self.data, self.features))
        self.assertIn("unknown feature UI-999", errors)
        self.assertIn("SHD-021 is Rejected", errors)
        self.assertIn("UI-020 is a duplicate", errors)

    def test_bad_id_zone_and_tech_fail(self):
        self.data["surfaces"][0].update({"id": "WIN-1", "zone": "nowhere", "tech": "Qt"})
        errors = " ".join(surfaces.validate(self.data, self.features))
        for text in ("bad surface ID", "unknown zone", "unknown tech"):
            self.assertIn(text, errors)

    def test_repository_source_is_valid(self):
        data = json.loads(surfaces.SOURCE.read_text(encoding="utf-8"))
        catalog = {f["id"]: f for f in json.loads(surfaces.CATALOG.read_text(encoding="utf-8"))["features"]}
        self.assertEqual(surfaces.validate(data, catalog), [])


class TokenTests(unittest.TestCase):
    def test_contrast_matches_known_values(self):
        self.assertAlmostEqual(tokens.contrast("#000000", "#FFFFFF"), 21.0, places=2)
        self.assertAlmostEqual(tokens.contrast("#11151C", "#F4F6FA"), 16.91, places=2)
        self.assertAlmostEqual(tokens.contrast("#9AB9E8", "#F4F6FA"), 1.85, places=2)

    def test_references_resolve_and_bad_values_fail(self):
        prims = {"cloud": "#f4f6fa"}
        self.assertEqual(tokens.resolve("{cloud}", prims), "#F4F6FA")
        with self.assertRaises(ValueError):
            tokens.resolve("{missing}", prims)
        with self.assertRaises(ValueError):
            tokens.resolve("blue", prims)

    def test_repository_tokens_load_and_every_pair_passes(self):
        data, themes, errors = tokens.load()
        self.assertEqual(errors, [])
        failing = [row for row in tokens.measure(data, themes) if row[3] < row[4]]
        self.assertEqual(failing, [])

    def test_css_has_every_theme_and_forced_colours(self):
        data, themes, _ = tokens.load()
        css = tokens.render_css(data, themes)
        for selector in (':root[data-theme="dark"]', ':root[data-theme="oled"]',
                         "@media (forced-colors: active)", "@media (prefers-reduced-motion: reduce)"):
            self.assertIn(selector, css)


class IconTests(unittest.TestCase):
    def test_marker_is_filled_and_refilled(self):
        sprite = "<svg><symbol id='a'/></svg>"
        first = icons.render("<body><!--ICONS--><main></main>", sprite)
        self.assertIn("<!--/ICONS-->", first)
        second = icons.render(first, "<svg><symbol id='b'/></svg>")
        self.assertIn("id='b'", second)
        self.assertNotIn("id='a'", second)
        self.assertEqual(second.count("<!--ICONS-->"), 1)


if __name__ == "__main__":
    unittest.main()
