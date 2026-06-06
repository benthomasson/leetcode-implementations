"""Leaf-Similar Trees - LeetCode Problem."""

from __future__ import annotations
import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """Return True if both trees have the same leaf value sequence.

        Args:
            root1: Root of the first binary tree.
            root2: Root of the second binary tree.

        Returns:
            True if leaf sequences are identical, False otherwise.
        """
        def get_leaves(node: Optional[TreeNode]) -> list[int]:
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return get_leaves(node.left) + get_leaves(node.right)

        return get_leaves(root1) == get_leaves(root2)


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from level-order list representation."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class TestLeafSimilar(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        r1 = build_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
        r2 = build_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
        self.assertTrue(self.sol.leafSimilar(r1, r2))

    def test_example2(self):
        r1 = build_tree([1, 2, 3])
        r2 = build_tree([1, 3, 2])
        self.assertFalse(self.sol.leafSimilar(r1, r2))

    def test_single_node_equal(self):
        r1 = TreeNode(5)
        r2 = TreeNode(5)
        self.assertTrue(self.sol.leafSimilar(r1, r2))

    def test_single_node_unequal(self):
        r1 = TreeNode(1)
        r2 = TreeNode(2)
        self.assertFalse(self.sol.leafSimilar(r1, r2))

    def test_different_depths_same_leaves(self):
        # Tree 1: root=1, left=2 (leaf)
        # Tree 2: root=3, left=4, left.left=2 (leaf)
        r1 = TreeNode(1, TreeNode(2))
        r2 = TreeNode(3, TreeNode(4, TreeNode(2)))
        self.assertTrue(self.sol.leafSimilar(r1, r2))

    def test_one_leaf_vs_multiple(self):
        r1 = TreeNode(1)
        r2 = TreeNode(1, TreeNode(1), TreeNode(2))
        self.assertFalse(self.sol.leafSimilar(r1, r2))


if __name__ == "__main__":
    unittest.main()
