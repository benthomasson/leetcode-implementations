"""Tests for Remove Linked List Elements - LeetCode #203."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import remove_elements, from_list, to_list


class TestRemoveElements(unittest.TestCase):

    def check(self, vals, val, expected):
        result = to_list(remove_elements(from_list(vals), val))
        self.assertEqual(result, expected)

    # Problem examples
    def test_example1(self):
        self.check([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5])

    def test_example2_empty(self):
        self.check([], 1, [])

    def test_example3_all_match(self):
        self.check([7, 7, 7, 7], 7, [])

    # Edge cases
    def test_single_node_match(self):
        self.check([1], 1, [])

    def test_single_node_no_match(self):
        self.check([1], 2, [1])

    def test_head_removal(self):
        self.check([5, 5, 1, 2], 5, [1, 2])

    def test_tail_removal(self):
        self.check([1, 2, 3, 3], 3, [1, 2])

    def test_consecutive_middle(self):
        self.check([1, 2, 2, 2, 3], 2, [1, 3])

    def test_no_matches(self):
        self.check([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5])

    def test_val_zero(self):
        """val=0 is valid per constraints (0 <= val <= 50)."""
        self.check([], 0, [])


if __name__ == "__main__":
    unittest.main()
