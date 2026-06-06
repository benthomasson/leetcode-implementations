"""Path Sum - LeetCode Problem."""

from __future__ import annotations

import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    """Return True if tree has a root-to-leaf path summing to targetSum.

    Args:
        root: Root of the binary tree.
        targetSum: Target sum to find along a root-to-leaf path.

    Returns:
        True if such a path exists, False otherwise.
    """
    if root is None:
        return False
    if root.left is None and root.right is None:
        return root.val == targetSum
    remainder = targetSum - root.val
    return hasPathSum(root.left, remainder) or hasPathSum(root.right, remainder)


# --- Tests ---

class TestPathSum(unittest.TestCase):
    def test_example1(self):
        #       5
        #      / \
        #     4   8
        #    /   / \
        #   11  13  4
        #  / \       \
        # 7   2       1
        root = TreeNode(5,
            TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
            TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
        self.assertTrue(hasPathSum(root, 22))

    def test_example2(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertFalse(hasPathSum(root, 5))

    def test_empty_tree(self):
        self.assertFalse(hasPathSum(None, 0))

    def test_single_node_match(self):
        self.assertTrue(hasPathSum(TreeNode(5), 5))

    def test_single_node_no_match(self):
        self.assertFalse(hasPathSum(TreeNode(5), 1))

    def test_negative_values(self):
        root = TreeNode(-2, None, TreeNode(-3))
        self.assertTrue(hasPathSum(root, -5))

    def test_left_only_path(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertTrue(hasPathSum(root, 6))
        self.assertFalse(hasPathSum(root, 3))

    def test_zero_target(self):
        root = TreeNode(0, TreeNode(0))
        self.assertTrue(hasPathSum(root, 0))

    def test_non_leaf_sum_match(self):
        # Sum matches at non-leaf node — should return False
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertFalse(hasPathSum(root, 1))


if __name__ == "__main__":
    unittest.main()
