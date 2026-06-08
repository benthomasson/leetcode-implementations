"""Evaluate Boolean Binary Tree."""
from __future__ import annotations

import unittest
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


def evalTree(root: Optional[TreeNode]) -> bool:
    """Evaluate a full binary tree with boolean operations.

    Args:
        root: Root of a full binary tree where leaves are 0/1 (False/True)
            and internal nodes are 2 (OR) or 3 (AND).

    Returns:
        The boolean result of evaluating the tree.
    """
    if root.left is None:
        return bool(root.val)
    left = evalTree(root.left)
    right = evalTree(root.right)
    if root.val == 2:
        return left or right
    return left and right


def _build_tree(vals: list) -> Optional[TreeNode]:
    """Build a binary tree from a level-order list."""
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    while i < len(vals):
        node = queue.popleft()
        if vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


class TestEvalTree(unittest.TestCase):
    def test_example1(self):
        root = _build_tree([2, 1, 3, None, None, 0, 1])
        self.assertTrue(evalTree(root))

    def test_example2(self):
        root = _build_tree([0])
        self.assertFalse(evalTree(root))

    def test_single_true(self):
        self.assertTrue(evalTree(TreeNode(1)))

    def test_and_true_true(self):
        root = TreeNode(3, TreeNode(1), TreeNode(1))
        self.assertTrue(evalTree(root))

    def test_and_true_false(self):
        root = TreeNode(3, TreeNode(1), TreeNode(0))
        self.assertFalse(evalTree(root))

    def test_or_false_false(self):
        root = TreeNode(2, TreeNode(0), TreeNode(0))
        self.assertFalse(evalTree(root))

    def test_or_false_true(self):
        root = TreeNode(2, TreeNode(0), TreeNode(1))
        self.assertTrue(evalTree(root))

    def test_nested(self):
        # OR(AND(1,0), OR(1,0)) = OR(False, True) = True
        root = TreeNode(2,
            TreeNode(3, TreeNode(1), TreeNode(0)),
            TreeNode(2, TreeNode(1), TreeNode(0)))
        self.assertTrue(evalTree(root))

    def test_all_and_chain(self):
        # AND(AND(1,1), 1) = AND(True, True) = True
        root = TreeNode(3, TreeNode(3, TreeNode(1), TreeNode(1)), TreeNode(1))
        self.assertTrue(evalTree(root))


if __name__ == "__main__":
    unittest.main()
