"""Tests for Binary Tree Tilt solution."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import TreeNode, findTilt


class TestFindTilt(unittest.TestCase):

    def test_empty_tree(self):
        self.assertEqual(findTilt(None), 0)

    def test_single_node(self):
        self.assertEqual(findTilt(TreeNode(5)), 0)

    def test_example1(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(findTilt(root), 1)

    def test_example2(self):
        root = TreeNode(4,
            TreeNode(2, TreeNode(3), TreeNode(5)),
            TreeNode(9, None, TreeNode(7)))
        self.assertEqual(findTilt(root), 15)

    def test_example3(self):
        root = TreeNode(21,
            TreeNode(7,
                TreeNode(1, TreeNode(3), TreeNode(3)),
                TreeNode(1)),
            TreeNode(14, TreeNode(2), TreeNode(2)))
        self.assertEqual(findTilt(root), 9)

    def test_left_chain(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(findTilt(root), 8)

    def test_right_chain(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(findTilt(root), 8)

    def test_negative_values(self):
        root = TreeNode(0, TreeNode(-3), TreeNode(3))
        self.assertEqual(findTilt(root), 6)

    def test_all_zeros(self):
        root = TreeNode(0, TreeNode(0), TreeNode(0))
        self.assertEqual(findTilt(root), 0)

    def test_balanced_equal_values(self):
        # All nodes value 1, perfectly balanced
        root = TreeNode(1, TreeNode(1), TreeNode(1))
        # Both children: tilt 0, root: |1-1| = 0
        self.assertEqual(findTilt(root), 0)


if __name__ == "__main__":
    unittest.main()
