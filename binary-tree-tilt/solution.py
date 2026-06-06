"""Binary Tree Tilt - LeetCode Solution."""

from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


def findTilt(root: Optional[TreeNode]) -> int:
    """Return the sum of every node's tilt in a binary tree.

    Args:
        root: Root of the binary tree.

    Returns:
        Sum of all node tilts.
    """
    total_tilt = 0

    def subtree_sum(node: Optional[TreeNode]) -> int:
        nonlocal total_tilt
        if not node:
            return 0
        left = subtree_sum(node.left)
        right = subtree_sum(node.right)
        total_tilt += abs(left - right)
        return node.val + left + right

    subtree_sum(root)
    return total_tilt
