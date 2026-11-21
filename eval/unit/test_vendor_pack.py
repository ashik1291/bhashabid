import os
import re
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "eval", "vendor_test"))
import score  # noqa: E402
from tasks import TASKS  # noqa: E402


class VendorPackTests(unittest.TestCase):
    def test_ids_unique_and_checks_callable(self):
        ids = [t["id"] for t in TASKS]
        self.assertEqual(len(ids), len(set(ids)))
        for t in TASKS:
            self.assertTrue(t["check"] is None or callable(t["check"]))
            self.assertTrue(t["prompt"].strip())

    def test_checks_do_not_crash_on_garbage(self):
        for t in TASKS:
            if t["check"]:
                self.assertIn(score.run_check(t, "hello"), (True, False))

    def test_parser_and_known_good(self):
        path = os.path.join(ROOT, "eval", "vendor_test", "results", "_t.md")
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write("## V01\n\n২৫,০০,০০০ টাকা, পঁচিশ লাখ টাকা মাত্র।\n\n## V02\n\n")
            outs = score.parse(path)
        finally:
            os.remove(path)
        self.assertEqual(list(outs), ["V01"])
        self.assertTrue(score.score(outs, False)["core"] == 1)


if __name__ == "__main__":
    unittest.main()
