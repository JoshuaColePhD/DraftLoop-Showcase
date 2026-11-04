import unittest
from pathlib import Path

from scripts.reanalyze import load_record, metrics, summarize


class ReanalysisTests(unittest.TestCase):
    def test_known_paired_scores(self):
        result = metrics([0, 2, 4, 6], [0, 1, 6, 6])
        self.assertEqual(result["Exact agreement"], 0.5)
        self.assertEqual(
            result["Adjacent agreement (within one point, including exact)"], 0.75
        )
        self.assertAlmostEqual(result["Quadratic weighted kappa"], 1 - 1.25 / 12.75)

    def test_undefined_is_not_zero(self):
        result = metrics([3, 3], [3, 3])
        self.assertIsNone(result["Quadratic weighted kappa"])
        self.assertIsNone(result["Pearson r"])
        with self.assertRaises(ValueError):
            metrics([1], [1, 2])
        with self.assertRaises(ValueError):
            metrics([], [])

    def test_recorded_failure_case_remains_explicit(self):
        record = load_record(
            Path(__file__).resolve().parents[1] / "data" / "recorded-results.json"
        )
        original, fixed = [summarize(record, run) for run in ("original", "fixed")]
        self.assertEqual(original["complete_rubrics"], 0)
        self.assertEqual(fixed["complete_rubrics"], 3)
        for result in (original, fixed):
            self.assertEqual(result["Exact agreement"], 0)
            self.assertEqual(result["Quadratic weighted kappa"], 0)
            self.assertEqual(result["Pearson r"], 0)
            self.assertAlmostEqual(
                result["Adjacent agreement (within one point, including exact)"], 1 / 3
            )


if __name__ == "__main__":
    unittest.main()
