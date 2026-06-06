"""Tests for Maximum Depth of Binary Tree."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import TreeNode, maxDepth


class TestMaxDepth(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(maxDepth(None), 0)

    def test_single_node(self):
        self.assertEqual(maxDepth(TreeNode(1)), 1)

    def test_example1(self):
        # [3,9,20,null,null,15,7] -> 3
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(maxDepth(root), 3)

    def test_example2(self):
        # [1,null,2] -> 2
        root = TreeNode(1, None, TreeNode(2))
        self.assertEqual(maxDepth(root), 2)

    def test_left_skewed(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        self.assertEqual(maxDepth(root), 4)

    def test_right_skewed(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(maxDepth(root), 3)

    def test_balanced_full(self):
        #       1
        #      / \
        #     2   3
        #    / \ / \
        #   4  5 6  7
        root = TreeNode(1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7)))
        self.assertEqual(maxDepth(root), 3)

    def test_negative_values(self):
        root = TreeNode(-100, TreeNode(-50), TreeNode(100))
        self.assertEqual(maxDepth(root), 2)

    def test_deep_chain(self):
        # Build a 100-node left-skewed tree
        root = TreeNode(0)
        current = root
        for i in range(1, 100):
            current.left = TreeNode(i)
            current = current.left
        self.assertEqual(maxDepth(root), 100)


if __name__ == "__main__":
    unittest.main()
