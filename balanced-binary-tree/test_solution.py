"""Tests for Balanced Binary Tree solution."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import TreeNode, getHeight, isBalanced


class TestBalancedBinaryTree(unittest.TestCase):
    # --- LeetCode examples ---
    def test_example1(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertTrue(isBalanced(root))

    def test_example2(self):
        root = TreeNode(1,
            TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
            TreeNode(2))
        self.assertFalse(isBalanced(root))

    def test_example3_empty(self):
        self.assertTrue(isBalanced(None))

    # --- Edge cases ---
    def test_single_node(self):
        self.assertTrue(isBalanced(TreeNode(42)))

    def test_left_chain_unbalanced(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertFalse(isBalanced(root))

    def test_right_chain_unbalanced(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertFalse(isBalanced(root))

    def test_balanced_with_height_diff_one(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4))
        self.assertTrue(isBalanced(root))

    # --- getHeight directly ---
    def test_getHeight_empty(self):
        self.assertEqual(getHeight(None), 0)

    def test_getHeight_balanced(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(getHeight(root), 2)

    def test_getHeight_unbalanced_returns_neg1(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(getHeight(root), -1)


if __name__ == "__main__":
    unittest.main()
