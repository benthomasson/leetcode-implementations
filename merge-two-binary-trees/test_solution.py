"""Tests for Merge Two Binary Trees solution."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import merge_trees, list_to_tree, tree_to_list


class TestMergeTrees(unittest.TestCase):
    def check(self, l1, l2, expected):
        result = merge_trees(list_to_tree(l1), list_to_tree(l2))
        self.assertEqual(tree_to_list(result), expected)

    # LeetCode examples
    def test_example1(self):
        self.check([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7], [3, 4, 5, 5, 4, None, 7])

    def test_example2(self):
        self.check([1], [1, 2], [2, 2])

    # Edge cases
    def test_both_empty(self):
        self.check([], [], [])

    def test_first_empty(self):
        self.check([], [1, 2, 3], [1, 2, 3])

    def test_second_empty(self):
        self.check([1, 2, 3], [], [1, 2, 3])

    def test_single_nodes(self):
        self.check([5], [3], [8])

    def test_negative_values(self):
        self.check([1, -3], [-1, 3], [0, 0])

    def test_unbalanced(self):
        self.check([1, 2], [1, None, 3], [2, 2, 3])

    # Non-mutation check
    def test_does_not_mutate_inputs(self):
        t1 = list_to_tree([1, 2, 3])
        t2 = list_to_tree([4, 5, 6])
        merge_trees(t1, t2)
        self.assertEqual(tree_to_list(t1), [1, 2, 3])
        self.assertEqual(tree_to_list(t2), [4, 5, 6])


if __name__ == "__main__":
    unittest.main()
