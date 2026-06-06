"""LeetCode 2236: Root Equals Sum of Children."""

from __future__ import annotations
import unittest
from typing import Optional


class TreeNode:
    """Binary tree node."""

    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        """Check if root value equals the sum of its two children.

        Args:
            root: Root of a binary tree with exactly 3 nodes.

        Returns:
            True if root.val == left.val + right.val, False otherwise.
        """
        return root.val == root.left.val + root.right.val


class TestCheckTree(unittest.TestCase):
    def _make_tree(self, root_val: int, left_val: int, right_val: int) -> TreeNode:
        return TreeNode(root_val, TreeNode(left_val), TreeNode(right_val))

    def test_example1_true(self):
        self.assertTrue(Solution().checkTree(self._make_tree(10, 4, 6)))

    def test_example2_false(self):
        self.assertFalse(Solution().checkTree(self._make_tree(5, 3, 1)))

    def test_all_zeros(self):
        self.assertTrue(Solution().checkTree(self._make_tree(0, 0, 0)))

    def test_negative_children(self):
        self.assertTrue(Solution().checkTree(self._make_tree(-5, -3, -2)))

    def test_mixed_signs(self):
        self.assertTrue(Solution().checkTree(self._make_tree(1, -1, 2)))

    def test_boundary_values(self):
        self.assertTrue(Solution().checkTree(self._make_tree(0, -100, 100)))

    def test_false_with_negatives(self):
        self.assertFalse(Solution().checkTree(self._make_tree(0, -1, -2)))


if __name__ == "__main__":
    unittest.main()
