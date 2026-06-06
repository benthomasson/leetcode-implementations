"""Symmetric Tree - LeetCode Problem."""

from __future__ import annotations
from collections import deque
from typing import Optional


class TreeNode:
    """Binary tree node."""

    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:
    """Check whether a binary tree is a mirror of itself.

    Args:
        root: Root node of the binary tree.

    Returns:
        True if the tree is symmetric around its center.
    """
    if not root:
        return True

    def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val
                and is_mirror(left.left, right.right)
                and is_mirror(left.right, right.left))

    return is_mirror(root.left, root.right)


def isSymmetricIterative(root: Optional[TreeNode]) -> bool:
    """Iterative version using a deque.

    Args:
        root: Root node of the binary tree.

    Returns:
        True if the tree is symmetric around its center.
    """
    if not root:
        return True
    q = deque([(root.left, root.right)])
    while q:
        left, right = q.popleft()
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        q.append((left.left, right.right))
        q.append((left.right, right.left))
    return True


# --- Tests ---
import unittest


def _build_tree(vals: list) -> Optional[TreeNode]:
    """Build a tree from level-order list (None for missing nodes)."""
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


class TestSymmetricTree(unittest.TestCase):
    def test_symmetric(self):
        root = _build_tree([1, 2, 2, 3, 4, 4, 3])
        self.assertTrue(isSymmetric(root))
        self.assertTrue(isSymmetricIterative(root))

    def test_asymmetric(self):
        root = _build_tree([1, 2, 2, None, 3, None, 3])
        self.assertFalse(isSymmetric(root))
        self.assertFalse(isSymmetricIterative(root))

    def test_single_node(self):
        self.assertTrue(isSymmetric(TreeNode(1)))
        self.assertTrue(isSymmetricIterative(TreeNode(1)))

    def test_empty(self):
        self.assertTrue(isSymmetric(None))
        self.assertTrue(isSymmetricIterative(None))

    def test_asymmetric_values(self):
        root = _build_tree([1, 2, 3])
        self.assertFalse(isSymmetric(root))
        self.assertFalse(isSymmetricIterative(root))

    def test_deep_symmetric(self):
        root = _build_tree([1, 2, 2, 3, None, None, 3])
        self.assertTrue(isSymmetric(root))
        self.assertTrue(isSymmetricIterative(root))

    def test_left_only(self):
        root = TreeNode(1, TreeNode(2))
        self.assertFalse(isSymmetric(root))
        self.assertFalse(isSymmetricIterative(root))


if __name__ == "__main__":
    unittest.main()
