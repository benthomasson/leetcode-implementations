"""Tests for Check if Array is Sorted and Rotated."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import Solution


class TestCheck(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # LeetCode examples
    def test_example1_rotated(self):
        self.assertTrue(self.s.check([3, 4, 5, 1, 2]))

    def test_example2_not_sorted(self):
        self.assertFalse(self.s.check([2, 1, 3, 4]))

    def test_example3_already_sorted(self):
        self.assertTrue(self.s.check([1, 2, 3]))

    # Edge cases
    def test_single_element(self):
        self.assertTrue(self.s.check([1]))

    def test_all_equal(self):
        self.assertTrue(self.s.check([2, 2, 2]))

    def test_two_elements_rotated(self):
        self.assertTrue(self.s.check([2, 1]))

    def test_duplicates_at_break(self):
        self.assertTrue(self.s.check([2, 2, 1, 2]))

    def test_multiple_breaks_false(self):
        self.assertFalse(self.s.check([3, 1, 2, 1]))

    def test_descending_order(self):
        self.assertFalse(self.s.check([5, 4, 3, 2, 1]))

    def test_rotated_by_one(self):
        self.assertTrue(self.s.check([5, 1, 2, 3, 4]))


if __name__ == "__main__":
    unittest.main()
