# SPDX-License-Identifier: MPL-2.0
# Copyright (c) The Brumel Authors
"""Unit tests for scripts/validate_docs.py."""

import copy
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_SPEC = importlib.util.spec_from_file_location("validate_docs", ROOT / "scripts" / "validate_docs.py")
validate_docs = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(validate_docs)


def make_feature(fid, epic, origin="A", **overrides):
    feature = {
        "id": fid, "name": f"Feature {fid}", "module": fid.split("-")[0], "epic": epic,
        "pillar": "Efficiency", "tier": "Secondary", "status": "Planned", "priority": "P2",
        "impact": "Medium", "complexity": "M", "phase": 2,
        "description": "d", "problem": "p", "use_case": "u", "segments": ["Everyday users"],
        "dependencies": [],
        "platforms": {"windows": "Planned", "linux": "Planned", "macos": "Deferred", "android": "N/A"},
        "ai": "None", "resource_cost": "Low", "infra_cost": "None",
        "security_risk": "Low", "privacy_risk": "Low — local only", "competitors": [],
        "evidence": "Hypothesis", "acceptance": ["It works"], "origin": origin,
        "duplicate_of": None, "limitations": "None known",
    }
    feature.update(overrides)
    return feature


def make_catalog():
    """A valid catalog with 52 research-origin features plus one other."""
    features = [make_feature(f"ENG-{n:03d}", "EP-ENG-01", origin=f"R52-{n:02d}") for n in range(1, 53)]
    features.append(make_feature("SHD-001", "EP-SHD-01", origin="D", dependencies=["ENG-001"]))
    epics = [
        {"id": "EP-ENG-01", "title": "Engine", "module": "ENG", "summary": "s", "phase": 2,
         "priority": "P1", "features": [f["id"] for f in features if f["epic"] == "EP-ENG-01"],
         "depends_on": []},
        {"id": "EP-SHD-01", "title": "Shield", "module": "SHD", "summary": "s", "phase": 2,
         "priority": "P1", "features": ["SHD-001"], "depends_on": ["EP-ENG-01"]},
    ]
    return {"features": features}, {"epics": epics}


class CatalogValidationTests(unittest.TestCase):
    def test_valid_catalog_has_no_errors(self):
        features, epics = make_catalog()
        self.assertEqual(validate_docs.validate_catalog(features, epics), [])

    def test_duplicate_id_detected(self):
        features, epics = make_catalog()
        features["features"].append(copy.deepcopy(features["features"][-1]))
        errors = validate_docs.validate_catalog(features, epics)
        self.assertTrue(any("duplicate id" in e for e in errors), errors)

    def test_bad_id_and_module_mismatch(self):
        features, epics = make_catalog()
        features["features"][-1]["id"] = "XYZ-1"
        errors = validate_docs.validate_catalog(features, epics)
        self.assertTrue(any("does not match <PREFIX>-NNN" in e for e in errors), errors)
        features, epics = make_catalog()
        features["features"][-1]["module"] = "ENG"
        errors = validate_docs.validate_catalog(features, epics)
        self.assertTrue(any("does not match id prefix" in e for e in errors), errors)

    def test_invalid_enum_detected(self):
        features, epics = make_catalog()
        features["features"][0]["status"] = "Shipped"
        errors = validate_docs.validate_catalog(features, epics)
        self.assertTrue(any("'status'" in e for e in errors), errors)

    def test_missing_key_detected(self):
        features, epics = make_catalog()
        del features["features"][0]["problem"]
        errors = validate_docs.validate_catalog(features, epics)
        self.assertTrue(any("missing required key 'problem'" in e for e in errors), errors)

    def test_unknown_dependency_and_duplicate_of(self):
        features, epics = make_catalog()
        features["features"][-1]["dependencies"] = ["ENG-999"]
        features["features"][-1]["duplicate_of"] = "CORE-404"
        errors = validate_docs.validate_catalog(features, epics)
        self.assertTrue(any("dependency 'ENG-999'" in e for e in errors), errors)
        self.assertTrue(any("duplicate_of 'CORE-404'" in e for e in errors), errors)

    def test_r52_coverage(self):
        features, epics = make_catalog()
        features["features"][1]["origin"] = "R52-01"  # R52-02 missing, R52-01 twice
        errors = validate_docs.validate_catalog(features, epics)
        self.assertTrue(any("R52-02 appears 0 times" in e for e in errors), errors)
        self.assertTrue(any("R52-01 appears 2 times" in e for e in errors), errors)
        self.assertEqual(
            [e for e in validate_docs.validate_catalog(features, epics, require_r52=False)], [])

    def test_epic_membership_consistency(self):
        features, epics = make_catalog()
        epics["epics"][1]["features"] = []
        features["features"][0]["epic"] = "EP-NANO-07"
        errors = validate_docs.validate_catalog(features, epics)
        self.assertTrue(any("does not list its feature SHD-001" in e for e in errors), errors)
        self.assertTrue(any("epic 'EP-NANO-07' does not exist" in e for e in errors), errors)

    def test_epic_unknown_dependency(self):
        features, epics = make_catalog()
        epics["epics"][1]["depends_on"] = ["EP-CORE-01"]
        errors = validate_docs.validate_catalog(features, epics)
        self.assertTrue(any("depends_on 'EP-CORE-01'" in e for e in errors), errors)

    def test_platform_values(self):
        features, epics = make_catalog()
        features["features"][0]["platforms"]["windows"] = "Maybe"
        del features["features"][0]["platforms"]["android"]
        errors = validate_docs.validate_catalog(features, epics)
        self.assertTrue(any("platforms.windows" in e for e in errors), errors)
        self.assertTrue(any("platforms missing 'android'" in e for e in errors), errors)


class LinkCheckTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        (self.root / "docs").mkdir()
        (self.root / "docs" / "exists.md").write_text("# Exists\n", encoding="utf-8")
        (self.root / "img.svg").write_text("<svg/>", encoding="utf-8")

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, text):
        (self.root / "README.md").write_text(text, encoding="utf-8")
        return validate_docs.check_links(self.root)

    def test_valid_links_pass(self):
        errors = self.write(
            "[ok](docs/exists.md)\n[anchor](docs/exists.md#exists)\n![img](img.svg)\n"
            "[dir](docs/)\n[ext](https://example.com/x)\n[mail](mailto:a@b.c)\n[top](#top)\n"
            '<img src="img.svg" alt="">\n[ref]: docs/exists.md\n[t](docs/exists.md "Title")\n')
        self.assertEqual(errors, [])

    def test_broken_link_reported_with_line(self):
        errors = self.write("line one\n[bad](docs/missing.md)\n")
        self.assertEqual(len(errors), 1)
        self.assertIn("README.md:2", errors[0])
        self.assertIn("docs/missing.md", errors[0])

    def test_code_blocks_and_comments_ignored(self):
        errors = self.write(
            "```\n[bad](nope.md)\n```\n`[bad](nope2.md)`\n<!-- [bad](nope3.md) -->\n")
        self.assertEqual(errors, [])

    def test_nested_badge_link(self):
        errors = self.write("[![badge](img.svg)](docs/missing.md)\n")
        self.assertEqual(len(errors), 1)
        self.assertIn("docs/missing.md", errors[0])

    def test_relative_to_subdirectory(self):
        (self.root / "docs" / "child.md").write_text("[up](../img.svg)\n[bad](../nope.md)\n",
                                                     encoding="utf-8")
        errors = validate_docs.check_links(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("docs/child.md:2", errors[0])


if __name__ == "__main__":
    unittest.main()
