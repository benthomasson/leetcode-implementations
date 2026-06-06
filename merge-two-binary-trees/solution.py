"""Merge Two Binary Trees - LeetCode Solution."""

from __future__ import annotations
from typing import Optional
from collections import deque
import unittest


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


def merge_trees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    """Merge two binary trees by summing overlapping nodes.

    Args:
        root1: Root of the first binary tree.
        root2: Root of the second binary tree.

    Returns:
        Root of the merged binary tree.
    """
    if not root1:
        return root2
    if not root2:
        return root1
    return TreeNode(
        root1.val + root2.val,
        merge_trees(root1.left, root2.left),
        merge_trees(root1.right, root2.right),
    )


def tree_to_list(root: Optional[TreeNode]) -> list:
    """Convert tree to level-order list (with trailing nulls stripped)."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def list_to_tree(vals: list) -> Optional[TreeNode]:
    """Build tree from level-order list."""
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


class TestMergeTrees(unittest.TestCase):
    def check(self, l1, l2, expected):
        result = merge_trees(list_to_tree(l1), list_to_tree(l2))
        self.assertEqual(tree_to_list(result), expected)

    def test_example1(self):
        self.check([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7], [3, 4, 5, 5, 4, None, 7])

    def test_example2(self):
        self.check([1], [1, 2], [2, 2])

    def test_both_none(self):
        self.check([], [], [])

    def test_first_none(self):
        self.check([], [1, 2, 3], [1, 2, 3])

    def test_second_none(self):
        self.check([1, 2, 3], [], [1, 2, 3])

    def test_single_nodes(self):
        self.check([5], [3], [8])

    def test_negative_values(self):
        self.check([1, -3], [-1, 3], [0, 0])

    def test_deep_unbalanced(self):
        self.check([1, 2], [1, None, 3], [2, 2, 3])


if __name__ == "__main__":
    unittest.main()
