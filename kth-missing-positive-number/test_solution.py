"""Tests for Kth Missing Positive Number solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestKthMissingPositive(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(self.sol.findKthPositive([2, 3, 4, 7, 11], 5), 9)

    def test_example2(self):
        self.assertEqual(self.sol.findKthPositive([1, 2, 3, 4], 2), 6)

    # --- Edge cases ---
    def test_single_element_missing_before(self):
        self.assertEqual(self.sol.findKthPositive([2], 1), 1)

    def test_single_element_missing_after(self):
        self.assertEqual(self.sol.findKthPositive([1], 1), 2)

    def test_no_gaps_in_array(self):
        self.assertEqual(self.sol.findKthPositive([1, 2, 3, 4, 5], 3), 8)

    def test_all_missing_before_array(self):
        self.assertEqual(self.sol.findKthPositive([10, 11, 12], 5), 5)

    def test_large_k(self):
        self.assertEqual(self.sol.findKthPositive([1, 2, 3], 100), 103)

    def test_k_equals_1_gap_at_start(self):
        self.assertEqual(self.sol.findKthPositive([3], 1), 1)

    def test_sparse_array(self):
        # arr = [2, 10], missing = [1,3,4,5,6,7,8,9,11,...], k=4 -> 5
        self.assertEqual(self.sol.findKthPositive([2, 10], 4), 5)


if __name__ == "__main__":
    unittest.main()
