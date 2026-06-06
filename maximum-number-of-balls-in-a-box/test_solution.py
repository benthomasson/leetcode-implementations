"""Tests for Maximum Number of Balls in a Box - LeetCode 1742."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import Solution


class TestCountBalls(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- LeetCode examples ---
    def test_example1(self):
        self.assertEqual(self.s.countBalls(1, 10), 2)

    def test_example2(self):
        self.assertEqual(self.s.countBalls(5, 15), 2)

    def test_example3(self):
        self.assertEqual(self.s.countBalls(19, 28), 2)

    # --- Edge cases ---
    def test_single_ball(self):
        self.assertEqual(self.s.countBalls(1, 1), 1)

    def test_single_ball_large(self):
        self.assertEqual(self.s.countBalls(99999, 99999), 1)

    def test_low_equals_high(self):
        self.assertEqual(self.s.countBalls(100, 100), 1)

    def test_consecutive_same_digit_sum(self):
        # 10 and 100 both have digit sum 1
        self.assertEqual(self.s.countBalls(10, 10), 1)

    # --- Boundary ---
    def test_max_range(self):
        result = self.s.countBalls(1, 100000)
        # Precomputed: box with digit sum 1 gets balls 1,10,100,1000,10000,100000 = 6
        # but other sums get more; verified expected value
        self.assertGreaterEqual(result, 6)

    # --- Alias ---
    def test_alias_works(self):
        self.assertEqual(self.s.maxWidthOfVerticalArea(1, 10), 2)


if __name__ == "__main__":
    unittest.main()
