"""Tests for Sort Array By Parity (LeetCode 905)."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestSortArrayByParity(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def _check(self, nums):
        original = nums[:]
        result = self.s.sortArrayByParity(nums[:])
        # All evens come before all odds
        evens = [x for x in result if x % 2 == 0]
        odds = [x for x in result if x % 2 == 1]
        self.assertEqual(result, evens + odds, f"Evens not before odds: {result}")
        # Same elements preserved
        self.assertEqual(sorted(result), sorted(original), "Elements changed")

    # Problem examples
    def test_example1(self):
        self._check([3, 1, 2, 4])

    def test_example2(self):
        self._check([0])

    # Edge cases
    def test_single_odd(self):
        self._check([1])

    def test_all_even(self):
        self._check([2, 4, 6, 8])

    def test_all_odd(self):
        self._check([1, 3, 5, 7])

    def test_already_partitioned(self):
        self._check([2, 4, 1, 3])

    def test_reverse_order(self):
        self._check([1, 3, 2, 4])

    def test_boundary_values(self):
        self._check([0, 5000, 4999, 1])

    def test_large_input(self):
        nums = list(range(5000))
        self._check(nums)


if __name__ == "__main__":
    unittest.main()
