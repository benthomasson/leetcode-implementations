"""Tests for Binary Tree Inorder Traversal."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import TreeNode, inorderTraversalHelper


class TestInorderTraversal(unittest.TestCase):

    def test_example1(self):
        """[1,null,2,3] -> [1,3,2]"""
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        self.assertEqual(inorderTraversalHelper(root), [1, 3, 2])

    def test_example2_empty(self):
        """[] -> []"""
        self.assertEqual(inorderTraversalHelper(None), [])

    def test_example3_single(self):
        """[1] -> [1]"""
        self.assertEqual(inorderTraversalHelper(TreeNode(1)), [1])

    def test_left_skewed(self):
        """Left-only chain: 3->2->1 inorder is [1,2,3]."""
        root = TreeNode(3, TreeNode(2, TreeNode(1)))
        self.assertEqual(inorderTraversalHelper(root), [1, 2, 3])

    def test_right_skewed(self):
        """Right-only chain: 1->2->3 inorder is [1,2,3]."""
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(inorderTraversalHelper(root), [1, 2, 3])

    def test_balanced(self):
        """Balanced tree with root=2, left=1, right=3."""
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertEqual(inorderTraversalHelper(root), [1, 2, 3])

    def test_boundary_values(self):
        """Min/max constraint values: -100 and 100."""
        root = TreeNode(0, TreeNode(-100), TreeNode(100))
        self.assertEqual(inorderTraversalHelper(root), [-100, 0, 100])

    def test_deeper_tree(self):
        """Tree with depth 3:
              4
             / \\
            2   6
           / \\ / \\
          1  3 5  7
        """
        root = TreeNode(4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(6, TreeNode(5), TreeNode(7)))
        self.assertEqual(inorderTraversalHelper(root), [1, 2, 3, 4, 5, 6, 7])


if __name__ == "__main__":
    unittest.main()
