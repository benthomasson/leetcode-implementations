from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right


def find_second_minimum_value(root: Optional[TreeNode]) -> int:
    """Find the second minimum value in a special binary tree.

    Args:
        root: Root of a special binary tree where each node's value equals
            the minimum of its children's values.

    Returns:
        The second minimum value, or -1 if none exists.
    """
    if not root:
        return -1

    min_val = root.val
    candidate = -1

    def dfs(node: Optional[TreeNode]) -> None:
        nonlocal candidate
        if not node:
            return
        if node.val > min_val:
            if candidate == -1 or node.val < candidate:
                candidate = node.val
            return  # prune: children are >= node.val
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return candidate
