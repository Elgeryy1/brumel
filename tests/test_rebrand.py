# SPDX-License-Identifier: MPL-2.0
# Copyright (c) The Brumel Authors
"""Unit tests for scripts/rebrand.py.

The real ID reader needs GRIT from a Chromium checkout. These tests use a tiny
repository and a stand-in that derives IDs from the message text, which is
enough to check that translations follow their messages.
"""

import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "tests"))

import rebrand  # noqa: E402
from test_build_tooling import IsolatedGit, run_git  # noqa: E402

HAS_GIT = shutil.which("git") is not None


def fake_ids(grd: Path) -> list[tuple[str, str]]:
    """Stand-in for GRIT: an ID per message derived from its text, parts included."""
    text = grd.read_text(encoding="utf-8")
    for part in re.findall(r'<part file="([^"]+)"', text):
        text = text.replace(f'<part file="{part}" />', (grd.parent / part).read_text(encoding="utf-8"))
    return [(m.group(2), str(int(hashlib.sha1(m.group(3).strip().encode()).hexdigest()[:12], 16)))
            for m in rebrand.MESSAGE.finditer(text)]


class TextRuleTests(unittest.TestCase):
    def test_product_name_is_replaced(self):
        self.assertEqual(rebrand.rebrand_text("Welcome to Chromium"), "Welcome to Brumel")
        self.assertEqual(rebrand.rebrand_text("Chromium's settings"), "Brumel's settings")

    def test_inflections_and_prefixes_in_translations(self):
        self.assertEqual(rebrand.rebrand_text("Chromiumin asetukset"), "Brumelin asetukset")
        self.assertEqual(rebrand.rebrand_text("Vula iChromium"), "Vula iBrumel")

    def test_other_products_and_attribution_are_kept(self):
        self.assertEqual(rebrand.rebrand_text("ChromiumOS update"), "ChromiumOS update")
        self.assertEqual(rebrand.rebrand_text("Copyright The Chromium Authors"), "Copyright The Chromium Authors")

    def test_accelerator_inside_the_name(self):
        self.assertEqual(rebrand.rebrand_text("Open in Chr&amp;omium"), "Open in Bru&amp;mel")
        self.assertEqual(rebrand.rebrand_text("&amp;Chromium"), "&amp;Brumel")

    def test_placeholders_are_never_changed(self):
        body = 'Update <ph name="PRODUCT">$1<ex>Chromium</ex></ph> now, Chromium'
        self.assertEqual(rebrand.rebrand_text(body), 'Update <ph name="PRODUCT">$1<ex>Chromium</ex></ph> now, Brumel')

    def test_link_to_the_chromium_project_is_kept(self):
        grd = ('Chromium is made possible by the <ph name="BEGIN_LINK_CHROMIUM">&lt;a&gt;</ph>Chromium'
               '<ph name="END_LINK_CHROMIUM">&lt;/a&gt;</ph> open source project.')
        self.assertTrue(rebrand.rebrand_text(grd).startswith("Brumel is made possible by"))
        self.assertIn("</ph>Chromium<ph", rebrand.rebrand_text(grd))
        xtb = 'Chromium es posible gracias al proyecto <ph name="BEGIN_LINK_CHROMIUM" />Chromium<ph name="END_LINK_CHROMIUM" />.'
        self.assertEqual(rebrand.rebrand_text(xtb),
                         'Brumel es posible gracias al proyecto <ph name="BEGIN_LINK_CHROMIUM" />Chromium'
                         '<ph name="END_LINK_CHROMIUM" />.')

    def test_chrome_in_translations_only_when_allowed(self):
        self.assertEqual(rebrand.rebrand_text("Abre Google Chrome", chrome=True), "Abre Brumel")
        self.assertEqual(rebrand.rebrand_text("Abre Chrome"), "Abre Chrome")
        self.assertEqual(rebrand.rebrand_text("Chromebook y Chromecast", chrome=True), "Chromebook y Chromecast")

    def test_keep_messages_and_changed_names(self):
        grd = ('<message name="IDS_ABOUT_VERSION_COMPANY_NAME" desc="x">The Chromium Authors</message>\n'
               '<message name="IDS_PRODUCT_NAME" desc="x">Chromium</message>\n'
               '<message name="IDS_OTHER" desc="x">Nothing here</message>\n')
        text, changed = rebrand.rebrand_grd(grd)
        self.assertEqual(changed, ["IDS_PRODUCT_NAME"])
        self.assertIn(">The Chromium Authors<", text)
        self.assertIn('name="IDS_PRODUCT_NAME" desc="x">Brumel<', text)

    def test_id_renames(self):
        before = [("A", "1"), ("B", "2"), ("C", "3")]
        after = [("A", "1"), ("B", "20"), ("C", "30")]
        self.assertEqual(rebrand.id_renames(before, after), {"2": "20", "3": "30"})
        with self.assertRaises(rebrand.ToolError):
            rebrand.id_renames(before, [("A", "1"), ("B", "2")])
        with self.assertRaises(rebrand.ToolError):
            rebrand.id_renames([("A", "1"), ("B", "1")], [("A", "10"), ("B", "11")])


GRD = """<?xml version="1.0" encoding="UTF-8"?>
<grit latest_public_release="0" current_release="1">
  <translations>
    <file path="resources/chromium_strings_es.xtb" lang="es" />
  </translations>
  <release seq="1">
    <messages>
      <message name="IDS_PRODUCT_NAME" desc="Product">Chromium</message>
      <message name="IDS_ABOUT_VERSION_COMPANY_NAME" desc="Company">The Chromium Authors</message>
      <message name="IDS_STORE" desc="Store">Open the Chrome Web Store in Chromium</message>
      <part file="settings_chromium_strings.grdp" />
    </messages>
  </release>
</grit>
"""
GRDP = """<?xml version="1.0" encoding="utf-8"?>
<grit-part>
  <message name="IDS_SETTINGS_TITLE" desc="Settings">Chromium settings</message>
</grit-part>
"""


@unittest.skipUnless(HAS_GIT, "git not available")
class CheckoutTests(unittest.TestCase):
    def setUp(self):
        self._git = IsolatedGit().__enter__()
        self._tmp = tempfile.TemporaryDirectory()
        self.src = Path(self._tmp.name) / "src"
        (self.src / "chrome" / "app" / "resources").mkdir(parents=True)
        (self.src / "components" / "strings").mkdir(parents=True)
        app = self.src / "chrome" / "app"
        (app / "chromium_strings.grd").write_text(GRD, encoding="utf-8")
        (app / "settings_chromium_strings.grdp").write_text(GRDP, encoding="utf-8")
        ids = dict(fake_ids(app / "chromium_strings.grd"))
        (app / "resources" / "chromium_strings_es.xtb").write_text(
            '<?xml version="1.0" ?>\n<translationbundle lang="es">\n'
            f'<translation id="{ids["IDS_PRODUCT_NAME"]}">Chromium</translation>\n'
            f'<translation id="{ids["IDS_ABOUT_VERSION_COMPANY_NAME"]}">The Chromium Authors</translation>\n'
            f'<translation id="{ids["IDS_STORE"]}">Abre Chrome Web Store en Chromium</translation>\n'
            f'<translation id="{ids["IDS_SETTINGS_TITLE"]}">Configuración de Chrome</translation>\n'
            '</translationbundle>\n', encoding="utf-8")
        (self.src / "components" / "components_chromium_strings.grd").write_text(
            GRD.replace("settings_chromium_strings.grdp", "none.grdp").replace('      <part file="none.grdp" />\n', ""),
            encoding="utf-8")
        run_git(self.src, "init", "--quiet", "--initial-branch=main")
        run_git(self.src, "add", ".")
        run_git(self.src, "commit", "--quiet", "-m", "base")
        self.ids = ids

    def tearDown(self):
        self._tmp.cleanup()
        self._git.__exit__(None, None, None)

    def test_apply_renames_translations_and_is_repeatable(self):
        steps, notes = rebrand.plan_apply(self.src, fake_ids)
        self.assertIn("chrome/app/chromium_strings.grd: 3 message(s), 3 translation(s) in 1 language(s)", notes)
        rebrand.run_plan(steps)
        app = self.src / "chrome" / "app"
        new_ids = dict(fake_ids(app / "chromium_strings.grd"))
        xtb = (app / "resources" / "chromium_strings_es.xtb").read_text(encoding="utf-8")
        self.assertIn(f'<translation id="{new_ids["IDS_PRODUCT_NAME"]}">Brumel</translation>', xtb)
        self.assertIn(f'<translation id="{self.ids["IDS_ABOUT_VERSION_COMPANY_NAME"]}">The Chromium Authors<', xtb)
        # The English mentions Chrome, so the translation keeps "Chrome Web Store".
        self.assertIn(f'<translation id="{new_ids["IDS_STORE"]}">Abre Chrome Web Store en Brumel<', xtb)
        # The English says only "Chromium": the translator's "Chrome" is rebranded too.
        self.assertIn(f'<translation id="{new_ids["IDS_SETTINGS_TITLE"]}">Configuración de Brumel<', xtb)
        self.assertIn("Brumel settings", (app / "settings_chromium_strings.grdp").read_text(encoding="utf-8"))
        # Running again starts from the committed files and writes the same result.
        rebrand.run_plan(rebrand.plan_apply(self.src, fake_ids)[0])
        self.assertEqual((app / "resources" / "chromium_strings_es.xtb").read_text(encoding="utf-8"), xtb)

    def test_revert_restores_committed_files(self):
        rebrand.run_plan(rebrand.plan_apply(self.src, fake_ids)[0])
        rebrand.run_plan(rebrand.plan_revert(self.src))
        status = subprocess.run(["git", "status", "--porcelain"], cwd=self.src, capture_output=True, text=True)
        self.assertEqual(status.stdout.strip(), "")

    def test_main_prints_a_plan_without_execute(self):
        with mock.patch.object(rebrand, "grit_id_reader", return_value=fake_ids), \
                mock.patch("sys.stdout") as out:
            self.assertEqual(rebrand.main(["apply", "--checkout", str(self.src)]), 0)
        self.assertIn("Plan only", "".join(call.args[0] for call in out.write.call_args_list))
        status = subprocess.run(["git", "status", "--porcelain"], cwd=self.src, capture_output=True, text=True)
        self.assertEqual(status.stdout.strip(), "")


if __name__ == "__main__":
    unittest.main()
