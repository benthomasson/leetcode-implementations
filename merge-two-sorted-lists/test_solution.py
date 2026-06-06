"""Tests for Merge Two Sorted Lists."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import ListNode, merge_two_lists, from_list, to_list


class TestMergeTwoLists(unittest.TestCase):
    def check(self, l1: list[int], l2: list[int], expected: list[int]):
        result = merge_two_lists(from_list(l1), from_list(l2))
        self.assertEqual(to_list(result), expected)

    # LeetCode examples
    def test_example1(self):
        self.check([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])

    def test_example2_both_empty(self):
        self.check([], [], [])

    def test_example3_one_empty(self):
        self.check([], [0], [0])

    # Edge cases
    def test_first_list_empty(self):
        self.check([], [1, 2, 3], [1, 2, 3])

    def test_second_list_empty(self):
        self.check([1, 2, 3], [], [1, 2, 3])

    def test_single_elements(self):
        self.check([2], [1], [1, 2])

    def test_all_duplicates(self):
        self.check([1, 1, 1], [1, 1], [1, 1, 1, 1, 1])

    def test_negative_values(self):
        self.check([-3, -1, 2], [-2, 0, 3], [-3, -2, -1, 0, 2, 3])

    def test_boundary_values(self):
        self.check([-100], [100], [-100, 100])

    def test_one_list_entirely_before_other(self):
        self.check([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
