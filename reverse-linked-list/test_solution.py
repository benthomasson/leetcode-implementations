"""Tests for Reverse Linked List - LeetCode #206."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import (
    ListNode,
    reverse_list,
    reverse_list_recursive,
    to_linked_list,
    to_list,
)


class TestReverseList(unittest.TestCase):

    def _run_both(self, input_vals, expected):
        for fn in (reverse_list, reverse_list_recursive):
            with self.subTest(fn=fn.__name__):
                head = to_linked_list(input_vals)
                result = to_list(fn(head))
                self.assertEqual(result, expected)

    # --- Problem examples ---

    def test_example1(self):
        self._run_both([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])

    def test_example2(self):
        self._run_both([1, 2], [2, 1])

    def test_example3_empty(self):
        self._run_both([], [])

    # --- Edge cases ---

    def test_single_node(self):
        self._run_both([1], [1])

    def test_negative_values(self):
        self._run_both([-5000, 0, 5000], [5000, 0, -5000])

    def test_duplicates(self):
        self._run_both([1, 1, 1], [1, 1, 1])

    def test_boundary_values(self):
        self._run_both([-5000, 5000], [5000, -5000])

    # --- Structural checks ---

    def test_iterative_returns_last_node_as_head(self):
        head = to_linked_list([10, 20, 30])
        new_head = reverse_list(head)
        self.assertEqual(new_head.val, 30)

    def test_recursive_returns_last_node_as_head(self):
        head = to_linked_list([10, 20, 30])
        new_head = reverse_list_recursive(head)
        self.assertEqual(new_head.val, 30)


if __name__ == "__main__":
    unittest.main()
