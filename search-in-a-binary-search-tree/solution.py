"""Search in a Binary Search Tree."""

from __future__ import annotations
import unittest
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Find and return the subtree rooted at the node with the given value.

    Args:
        root: Root of the binary search tree.
        val: Value to search for.

    Returns:
        The subtree rooted at the matching node, or None if not found.
    """
    node = root
    while node:
        if val == node.val:
            return node
        elif val < node.val:
            node = node.left
        else:
            node = node.right
    return None


class TestSearchBST(unittest.TestCase):
    def _build(self, vals) -> Optional[TreeNode]:
        """Build a tree from level-order list."""
        if not vals:
            return None
        root = TreeNode(vals[0])
        queue = deque([root])
        i = 1
        while i < len(vals):
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

    def _to_list(self, root: Optional[TreeNode]) -> list:
        """Convert tree to level-order list."""
        if not root:
            return []
        result, queue = [], [root]
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def test_example1_found(self):
        root = self._build([4, 2, 7, 1, 3])
        result = searchBST(root, 2)
        self.assertEqual(self._to_list(result), [2, 1, 3])

    def test_example2_not_found(self):
        root = self._build([4, 2, 7, 1, 3])
        self.assertIsNone(searchBST(root, 5))

    def test_root_is_target(self):
        root = self._build([4, 2, 7, 1, 3])
        result = searchBST(root, 4)
        self.assertEqual(self._to_list(result), [4, 2, 7, 1, 3])

    def test_single_node_found(self):
        root = TreeNode(1)
        self.assertEqual(searchBST(root, 1), root)

    def test_single_node_not_found(self):
        root = TreeNode(1)
        self.assertIsNone(searchBST(root, 2))

    def test_leaf_node(self):
        root = self._build([4, 2, 7, 1, 3])
        result = searchBST(root, 3)
        self.assertEqual(self._to_list(result), [3])

    def test_none_root(self):
        self.assertIsNone(searchBST(None, 1))


if __name__ == "__main__":
    unittest.main()
