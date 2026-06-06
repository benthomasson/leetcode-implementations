"""Tests for Minimum Subsequence in Non-Increasing Order."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestMinSubsequence(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.solve = self.s.min_changes_to_divide_string

    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(self.solve([4, 3, 10, 9, 8]), [10, 9])

    def test_example2(self):
        self.assertEqual(self.solve([4, 4, 7, 6, 7]), [7, 7, 6])

    # --- Edge cases ---
    def test_single_element(self):
        self.assertEqual(self.solve([5]), [5])

    def test_two_elements_unequal(self):
        self.assertEqual(self.solve([1, 2]), [2])

    def test_two_elements_equal(self):
        # Equal pair: must take both (sum == remainder isn't strictly greater)
        self.assertEqual(self.solve([5, 5]), [5, 5])

    def test_all_equal_odd_count(self):
        self.assertEqual(self.solve([3, 3, 3]), [3, 3])

    def test_all_ones(self):
        # [1,1,1,1] total=4, need >2, so take 3 ones
        self.assertEqual(self.solve([1, 1, 1, 1]), [1, 1, 1])

    def test_large_dominant(self):
        # One large element dominates
        self.assertEqual(self.solve([100, 1, 1, 1]), [100])

    def test_non_increasing_output_order(self):
        result = self.solve([4, 3, 10, 9, 8])
        self.assertEqual(result, sorted(result, reverse=True))

    def test_input_not_presorted(self):
        # Verify works regardless of input order
        self.assertEqual(self.solve([1, 10, 2, 9]), [10, 9])


if __name__ == "__main__":
    unittest.main()
