# SPDX-License-Identifier: MPL-2.0
# Copyright (c) The Brumel Authors
"""Unit tests for scripts/bench/harness.py (no browser is launched)."""

import json
import sys
import threading
import unittest
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts" / "bench"))

import harness  # noqa: E402


class StatisticsTests(unittest.TestCase):
    def test_summary(self):
        result = harness.summarize([10, 12, 11, 13, 50])
        self.assertEqual(result["n"], 5)
        self.assertEqual(result["median"], 12)
        self.assertLessEqual(result["ci95_low"], result["median"])
        self.assertGreaterEqual(result["ci95_high"], result["median"])
        self.assertEqual(harness.summarize([]), {"n": 0})
        self.assertEqual(harness.summarize([None, 4.0]), {"n": 1, "median": 4.0})

    def test_bootstrap_is_seeded(self):
        values = [1.0, 2.0, 3.0, 4.0, 9.0]
        self.assertEqual(harness.summarize(values, seed=3), harness.summarize(values, seed=3))


class CorpusTests(unittest.TestCase):
    def test_pages_report_load_and_paint(self):
        pages = harness.corpus_pages()
        self.assertEqual(len(pages), 5)
        for body in pages.values():
            self.assertIn("sendBeacon", body)
            self.assertIn("first-contentful-paint", body)
        self.assertEqual(harness.corpus_pages(), pages)  # deterministic

    def test_tab_urls_are_unique(self):
        urls = harness.tab_urls("http://127.0.0.1:1", 12)
        self.assertEqual(len(set(urls)), 12)
        self.assertTrue(all("?tab=" in u for u in urls))


class ProcessParsingTests(unittest.TestCase):
    def test_windows_json(self):
        self.assertEqual(harness.parse_windows_json(""), [])
        one = harness.parse_windows_json('{"pid": 4, "mem": 1048576, "cpu": 1.5}')
        self.assertEqual((one[0].pid, one[0].memory_bytes, one[0].cpu_seconds), (4, 1048576, 1.5))
        many = harness.parse_windows_json('[{"pid": 1, "mem": null, "cpu": null}, {"pid": 2, "mem": 3, "cpu": 0}]')
        self.assertEqual([s.pid for s in many], [1, 2])
        self.assertEqual(many[0].memory_bytes, 0)

    def test_linux_parsers(self):
        self.assertEqual(harness.parse_pss("Rss: 10 kB\nPss: 2048 kB\n"), 2048 * 1024)
        stat = "1234 (chrome --type=x) S " + " ".join(["0"] * 10) + " 300 100 0 0"
        self.assertEqual(harness.parse_proc_stat_cpu(stat, 100), 4.0)


class ServerTests(unittest.TestCase):
    def test_serves_pages_and_records_beacons(self):
        log = harness.BeaconLog()
        server = harness.make_server(harness.corpus_pages(), log)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        try:
            self.assertEqual(server.server_address[0], "127.0.0.1")
            base = f"http://127.0.0.1:{server.server_address[1]}"
            with urllib.request.urlopen(base + "/article.html?tab=0") as response:
                self.assertIn(b"Article", response.read())
            beacon = json.dumps({"tab": "0", "kind": "load", "value": 12.5, "timeOrigin": 1000.0}).encode()
            urllib.request.urlopen(urllib.request.Request(base + "/beacon", data=beacon, method="POST")).close()
            self.assertTrue(log.wait_for_loads(1, timeout=5))
            self.assertEqual(log.snapshot()[0]["value"], 12.5)
            bad = urllib.request.Request(base + "/beacon", data=b'{"value": "x"}', method="POST")
            with self.assertRaises(urllib.error.HTTPError):
                urllib.request.urlopen(bad)
        finally:
            server.shutdown()
            server.server_close()


if __name__ == "__main__":
    unittest.main()
