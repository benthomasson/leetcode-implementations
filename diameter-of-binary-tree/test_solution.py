"""Tests for diameter_of_binary_tree."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import TreeNode, diameter_of_binary_tree


class TestDiameterOfBinaryTree(unittest.TestCase):

    def test_example1(self):
        """[1,2,3,4,5] -> 3"""
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertEqual(diameter_of_binary_tree(root), 3)

    def test_example2(self):
        """[1,2] -> 1"""
        root = TreeNode(1, TreeNode(2))
        self.assertEqual(diameter_of_binary_tree(root), 1)

    def test_single_node(self):
        self.assertEqual(diameter_of_binary_tree(TreeNode(42)), 0)

    def test_right_skewed(self):
        # 1 -> 2 -> 3 -> 4 (all right children)
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
        self.assertEqual(diameter_of_binary_tree(root), 3)

    def test_diameter_not_through_root(self):
        #         1
        #        /
        #       2
        #      / \
        #     3   4
        #    /     \
        #   5       6
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(5)), TreeNode(4, None, TreeNode(6))))
        self.assertEqual(diameter_of_binary_tree(root), 4)

    def test_perfect_tree_depth2(self):
        #       1
        #      / \
        #     2   3
        #    / \ / \
        #   4  5 6  7
        root = TreeNode(1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7)))
        self.assertEqual(diameter_of_binary_tree(root), 4)

    def test_two_nodes_right(self):
        root = TreeNode(1, None, TreeNode(2))
        self.assertEqual(diameter_of_binary_tree(root), 1)

    def test_zigzag(self):
        # 1 -> left 2 -> right 3 -> left 4
        root = TreeNode(1, TreeNode(2, None, TreeNode(3, TreeNode(4))))
        self.assertEqual(diameter_of_binary_tree(root), 3)


if __name__ == "__main__":
    unittest.main()
