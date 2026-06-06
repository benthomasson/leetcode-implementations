"""Tests for Convert Binary Number in a Linked List to Integer."""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import ListNode, min_operations, _make_list


class TestMinOperations(unittest.TestCase):
    # Problem examples
    def test_example1_101(self):
        self.assertEqual(min_operations(_make_list([1, 0, 1])), 5)

    def test_example2_single_zero(self):
        self.assertEqual(min_operations(_make_list([0])), 0)

    # Edge cases
    def test_single_one(self):
        self.assertEqual(min_operations(_make_list([1])), 1)

    def test_all_zeros(self):
        self.assertEqual(min_operations(_make_list([0, 0, 0, 0])), 0)

    def test_all_ones_30(self):
        self.assertEqual(min_operations(_make_list([1] * 30)), 2**30 - 1)

    # Additional cases
    def test_1100_is_12(self):
        self.assertEqual(min_operations(_make_list([1, 1, 0, 0])), 12)

    def test_leading_zeros(self):
        self.assertEqual(min_operations(_make_list([0, 0, 1, 0])), 2)

    def test_power_of_two(self):
        # 1000 = 8
        self.assertEqual(min_operations(_make_list([1, 0, 0, 0])), 8)

    def test_two_nodes(self):
        self.assertEqual(min_operations(_make_list([1, 1])), 3)


if __name__ == "__main__":
    unittest.main()
