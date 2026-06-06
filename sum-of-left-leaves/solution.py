"""Sum of Left Leaves - LeetCode solution."""

from __future__ import annotations


class TreeNode:
    """Binary tree node."""

    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


def sum_of_left_leaves(root: TreeNode | None) -> int:
    """Return the sum of all left leaves in a binary tree.

    Args:
        root: Root node of the binary tree.

    Returns:
        Sum of values of all left leaf nodes.
    """

    def dfs(node: TreeNode | None, is_left: bool) -> int:
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return node.val if is_left else 0
        return dfs(node.left, True) + dfs(node.right, False)

    return dfs(root, False)
