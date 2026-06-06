"""Tests for Remove Duplicates from Sorted List."""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import ListNode, delete_duplicates, from_list, to_list


class TestDeleteDuplicates(unittest.TestCase):
    def check(self, input_vals, expected):
        self.assertEqual(to_list(delete_duplicates(from_list(input_vals))), expected)

    # Problem examples
    def test_example1(self):
        self.check([1, 1, 2], [1, 2])

    def test_example2(self):
        self.check([1, 1, 2, 3, 3], [1, 2, 3])

    # Edge cases
    def test_empty(self):
        self.check([], [])

    def test_single_node(self):
        self.check([1], [1])

    def test_no_duplicates(self):
        self.check([1, 2, 3], [1, 2, 3])

    def test_all_same(self):
        self.check([5, 5, 5, 5], [5])

    def test_two_nodes_duplicate(self):
        self.check([1, 1], [1])

    def test_negative_values(self):
        self.check([-3, -3, -1, 0, 0, 1], [-3, -1, 0, 1])

    # Mutation: verify original head node is returned
    def test_returns_same_head(self):
        head = from_list([1, 1, 2])
        result = delete_duplicates(head)
        self.assertIs(result, head)

    # Boundary: max constraint size
    def test_large_300_nodes(self):
        vals = []
        for v in range(-100, 101):
            vals.extend([v] * 3)  # 603 > 300 but tests algorithmic correctness
        self.check(vals, list(range(-100, 101)))


if __name__ == "__main__":
    unittest.main()
