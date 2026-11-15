# eval/unit/test_before_after_benchmark.py
import unittest
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from eval.benchmarks.benchmark_evaluator import evaluate_text, SAMPLE_BASELINES

class TestBeforeAfterBenchmark(unittest.TestCase):

    def test_realistic_benchmark_cases(self):
        for cid in sorted(SAMPLE_BASELINES.keys()):
            case = SAMPLE_BASELINES[cid]
            res_before = evaluate_text(case["before_sample"], cid)
            res_after = evaluate_text(case["after_sample"], cid)

            # Raw frontier LLM baseline demonstrates fluent general Bengali but falls short of statutory standards (< 90)
            self.assertLess(res_before["score"], 90, f"Case {cid} raw LLM unexpectedly scored at statutory grade")
            # Bhashabid coprocessor elevates output to publication/statutory grade (>= 90)
            self.assertGreaterEqual(res_after["score"], 90, f"Case {cid} coprocessor failed 90-point statutory grade")
            self.assertGreater(res_after["score"], res_before["score"], f"Case {cid} coprocessor did not improve baseline")

if __name__ == "__main__":
    unittest.main()
