# eval/unit/test_before_after_benchmark.py
import unittest
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from eval.benchmarks.benchmark_evaluator import evaluate_text, SAMPLE_BASELINES

class TestBeforeAfterBenchmark(unittest.TestCase):

    def test_all_10_benchmark_cases(self):
        for cid in sorted(SAMPLE_BASELINES.keys()):
            case = SAMPLE_BASELINES[cid]
            res_before = evaluate_text(case["before_sample"], cid)
            res_after = evaluate_text(case["after_sample"], cid)

            # Raw AI baseline must fall short of professional threshold (< 70)
            self.assertLess(res_before["score"], 70, f"Case {cid} before score unexpectedly high")
            # Bhashabid coprocessor output must reach publication quality (>= 90)
            self.assertGreaterEqual(res_after["score"], 90, f"Case {cid} after score failed threshold")
            self.assertEqual(res_after["guru_chandali_count"], 0, f"Case {cid} has Guru-chandali")
            self.assertEqual(res_after["corrupted_decimals"], 0, f"Case {cid} has corrupted decimals")

if __name__ == "__main__":
    unittest.main()
