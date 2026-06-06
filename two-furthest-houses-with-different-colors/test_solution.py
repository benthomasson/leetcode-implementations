"""Tests for Two Furthest Houses With Different Colors."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestMaxCompatibilitySum(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(self.s.maxDistance([1, 1, 1, 6, 1, 1, 1]), 3)

    def test_example2(self):
        self.assertEqual(self.s.maxDistance([1, 8, 3, 8, 3]), 4)

    def test_example3(self):
        self.assertEqual(self.s.maxDistance([0, 1]), 1)

    # --- Edge cases ---
    def test_two_different(self):
        self.assertEqual(self.s.maxDistance([99, 0]), 1)

    def test_different_endpoints_long(self):
        self.assertEqual(self.s.maxDistance([1, 1, 1, 1, 2]), 4)

    def test_all_same_except_first(self):
        self.assertEqual(self.s.maxDistance([5, 3, 3, 3, 3]), 4)

    def test_same_endpoints_diff_middle(self):
        self.assertEqual(self.s.maxDistance([1, 2, 1]), 1)

    def test_max_length(self):
        # 100 houses, differ only at endpoints
        colors = [1] * 100
        colors[-1] = 2
        self.assertEqual(self.s.maxDistance(colors), 99)

    def test_all_different(self):
        self.assertEqual(self.s.maxDistance([1, 2, 3, 4, 5]), 4)

    def test_same_endpoints_diff_near_start(self):
        # Optimal pair is (1, 4) → distance 3
        self.assertEqual(self.s.maxDistance([1, 2, 1, 1, 1]), 3)


if __name__ == "__main__":
    unittest.main()
