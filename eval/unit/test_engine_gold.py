import os
import sys
import unittest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

import importlib.util

_spec = importlib.util.spec_from_file_location(
    "engine_accuracy", os.path.join(REPO_ROOT, "eval", "benchmarks", "engine_accuracy.py")
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
evaluate, load_gold = _mod.evaluate, _mod.load_gold


class TestEngineGoldSet(unittest.TestCase):
    """Regression lock on eval/gold/engine_gold.jsonl (REQ-026..REQ-030, REQ-032)."""

    @classmethod
    def setUpClass(cls):
        cls.res = evaluate(load_gold())

    def test_no_lint_false_positives_on_clean_text(self):
        self.assertEqual(self.res["clean"]["lint_false_positives"], [])

    def test_repair_leaves_clean_text_unchanged(self):
        self.assertEqual(self.res["clean"]["repair_alterations"], [])

    def test_detection_recall(self):
        for label, stats in self.res["recall"].items():
            self.assertEqual(stats["misses"], [], f"{label} misses")

    def test_repair_resolution_floor(self):
        floors = {"guru_chandali": 1.0, "honorific": 1.0, "calque": 0.5}
        for label, floor in floors.items():
            self.assertGreaterEqual(self.res["recall"][label]["repair_rate"], floor, label)


if __name__ == "__main__":
    unittest.main()
