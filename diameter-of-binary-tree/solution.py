"""Diameter of Binary Tree - LeetCode"""

from __future__ import annotations
from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    """Return the diameter (longest path length in edges) of a binary tree.

    Args:
        root: Root node of the binary tree.

    Returns:
        Number of edges on the longest path between any two nodes.
    """
    diameter = 0

    def height(node: Optional[TreeNode]) -> int:
        nonlocal diameter
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)

    height(root)
    return diameter


# --- Tests ---

class TestDiameterOfBinaryTree(unittest.TestCase):

    def test_example1(self):
        #       1
        #      / \
        #     2   3
        #    / \
        #   4   5
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertEqual(diameter_of_binary_tree(root), 3)

    def test_example2(self):
        root = TreeNode(1, TreeNode(2))
        self.assertEqual(diameter_of_binary_tree(root), 1)

    def test_single_node(self):
        self.assertEqual(diameter_of_binary_tree(TreeNode(1)), 0)

    def test_left_skewed(self):
        # 1 -> 2 -> 3 -> 4
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
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

    def test_balanced(self):
        #       1
        #      / \
        #     2   3
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(diameter_of_binary_tree(root), 2)


if __name__ == "__main__":
    unittest.main()
