"""Subtree of Another Tree - LeetCode 572."""
from __future__ import annotations
import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """Check if subRoot is a subtree of root.

        Args:
            root: Root of the main tree.
            subRoot: Root of the candidate subtree.

        Returns:
            True if subRoot is a subtree of root.
        """
        if not subRoot:
            return True
        if not root:
            return False
        if self._is_same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def _is_same(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self._is_same(s.left, t.left) and self._is_same(s.right, t.right)


def _build(vals: list) -> Optional[TreeNode]:
    """Build a tree from level-order list (None for missing nodes)."""
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


class TestSubtree(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        root = _build([3, 4, 5, 1, 2])
        sub = _build([4, 1, 2])
        self.assertTrue(self.sol.isSubtree(root, sub))

    def test_example2(self):
        root = _build([3, 4, 5, 1, 2, None, None, None, None, 0])
        sub = _build([4, 1, 2])
        self.assertFalse(self.sol.isSubtree(root, sub))

    def test_identical_trees(self):
        root = _build([1, 2, 3])
        sub = _build([1, 2, 3])
        self.assertTrue(self.sol.isSubtree(root, sub))

    def test_single_node_match(self):
        root = _build([1])
        sub = _build([1])
        self.assertTrue(self.sol.isSubtree(root, sub))

    def test_single_node_no_match(self):
        root = _build([1])
        sub = _build([2])
        self.assertFalse(self.sol.isSubtree(root, sub))

    def test_subroot_none(self):
        root = _build([1])
        self.assertTrue(self.sol.isSubtree(root, None))

    def test_root_none(self):
        sub = _build([1])
        self.assertFalse(self.sol.isSubtree(None, sub))

    def test_subtree_at_leaf(self):
        root = _build([1, 2, 3, 4, 5])
        sub = _build([2, 4, 5])
        self.assertTrue(self.sol.isSubtree(root, sub))

    def test_same_values_different_structure(self):
        root = _build([1, 2, 3])
        sub = _build([1, 2])
        self.assertFalse(self.sol.isSubtree(root, sub))


if __name__ == "__main__":
    unittest.main()
