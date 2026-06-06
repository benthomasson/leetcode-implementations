"""Tests for check-if-an-array-is-consecutive."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestIsConsecutive(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- Problem examples ---
    def test_example1(self):
        self.assertTrue(self.s.isConsecutive([1, 3, 4, 2]))

    def test_example2(self):
        self.assertFalse(self.s.isConsecutive([1, 3]))

    def test_example3(self):
        self.assertTrue(self.s.isConsecutive([3, 5, 4]))

    # --- Edge cases ---
    def test_single_element(self):
        self.assertTrue(self.s.isConsecutive([0]))

    def test_duplicates_should_fail(self):
        self.assertFalse(self.s.isConsecutive([1, 1, 2, 3]))

    def test_all_same_elements(self):
        self.assertFalse(self.s.isConsecutive([5, 5, 5]))

    def test_gap_with_correct_range(self):
        # [1,2,4,5] has max-min+1=5 != len=4, so False
        self.assertFalse(self.s.isConsecutive([1, 2, 4, 5]))

    def test_boundary_values(self):
        self.assertTrue(self.s.isConsecutive([99998, 99999, 100000]))

    def test_already_sorted(self):
        self.assertTrue(self.s.isConsecutive([10, 11, 12, 13, 14]))

    def test_reverse_sorted(self):
        self.assertTrue(self.s.isConsecutive([14, 13, 12, 11, 10]))


if __name__ == "__main__":
    unittest.main()
