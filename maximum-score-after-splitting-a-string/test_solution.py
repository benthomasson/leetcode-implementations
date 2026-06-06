"""Tests for maximum score after splitting a string."""

import unittest
from solution import max_score_after_splitting


class TestMaxScoreAfterSplitting(unittest.TestCase):
    # Provided examples
    def test_example1(self):
        self.assertEqual(max_score_after_splitting("011101"), 5)

    def test_example2(self):
        self.assertEqual(max_score_after_splitting("00111"), 5)

    def test_example3(self):
        self.assertEqual(max_score_after_splitting("1111"), 3)

    # Length-2 edge cases
    def test_01(self):
        self.assertEqual(max_score_after_splitting("01"), 2)

    def test_10(self):
        self.assertEqual(max_score_after_splitting("10"), 0)

    def test_00(self):
        self.assertEqual(max_score_after_splitting("00"), 1)

    def test_11(self):
        self.assertEqual(max_score_after_splitting("11"), 1)

    # Uniform strings
    def test_all_zeros(self):
        self.assertEqual(max_score_after_splitting("00000"), 4)

    def test_all_ones(self):
        self.assertEqual(max_score_after_splitting("11111"), 4)

    # Best split at last position
    def test_best_split_late(self):
        self.assertEqual(max_score_after_splitting("00001"), 5)


if __name__ == "__main__":
    unittest.main()
