"""Invert Binary Tree - LeetCode"""

from __future__ import annotations
import unittest


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    """Invert a binary tree by swapping left and right children recursively.

    Args:
        root: Root node of the binary tree.

    Returns:
        Root of the inverted tree.
    """
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def tree_to_list(root: TreeNode | None) -> list[int | None]:
    """BFS level-order serialization (trailing Nones stripped)."""
    if not root:
        return []
    result: list[int | None] = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def list_to_tree(vals: list[int | None]) -> TreeNode | None:
    """Build tree from level-order list."""
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while i < len(vals):
        node = queue.pop(0)
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


class TestInvertTree(unittest.TestCase):
    def test_example1(self):
        root = list_to_tree([4, 2, 7, 1, 3, 6, 9])
        self.assertEqual(tree_to_list(invert_tree(root)), [4, 7, 2, 9, 6, 3, 1])

    def test_example2(self):
        root = list_to_tree([2, 1, 3])
        self.assertEqual(tree_to_list(invert_tree(root)), [2, 3, 1])

    def test_empty(self):
        self.assertIsNone(invert_tree(None))

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(tree_to_list(invert_tree(root)), [1])

    def test_left_skewed(self):
        root = list_to_tree([1, 2, None, 3])
        self.assertEqual(tree_to_list(invert_tree(root)), [1, None, 2, None, 3])

    def test_right_skewed(self):
        root = list_to_tree([1, None, 2, None, 3])
        self.assertEqual(tree_to_list(invert_tree(root)), [1, 2, None, 3])


if __name__ == "__main__":
    unittest.main()
