"""Tests for Rank Transform of an Array - LeetCode 1331."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import Solution


class TestArrayRankTransform(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(self.s.arrayRankTransform([40, 10, 20, 30]), [4, 1, 2, 3])

    def test_example2(self):
        self.assertEqual(self.s.arrayRankTransform([100, 100, 100]), [1, 1, 1])

    def test_example3(self):
        self.assertEqual(
            self.s.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]),
            [5, 3, 4, 2, 8, 6, 7, 1, 3],
        )

    # --- Edge cases ---
    def test_empty(self):
        self.assertEqual(self.s.arrayRankTransform([]), [])

    def test_single_element(self):
        self.assertEqual(self.s.arrayRankTransform([42]), [1])

    def test_two_duplicates(self):
        self.assertEqual(self.s.arrayRankTransform([5, 5]), [1, 1])

    def test_negatives(self):
        self.assertEqual(self.s.arrayRankTransform([-5, -10, 0]), [2, 1, 3])

    def test_large_boundary_values(self):
        self.assertEqual(
            self.s.arrayRankTransform([-10**9, 10**9, 0]), [1, 3, 2]
        )

    def test_duplicates_mixed(self):
        self.assertEqual(
            self.s.arrayRankTransform([10, 20, 10, 20, 30]),
            [1, 2, 1, 2, 3],
        )


if __name__ == "__main__":
    unittest.main()
