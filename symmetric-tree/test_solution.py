"""Tests for Symmetric Tree solution."""

import sys
import unittest
from collections import deque
from typing import Optional

sys.path.insert(0, "../implementer")
from solution import TreeNode, isSymmetric, isSymmetricIterative


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
    """Test both recursive and iterative solutions."""

    def _check(self, root, expected):
        self.assertEqual(isSymmetric(root), expected)
        self.assertEqual(isSymmetricIterative(root), expected)

    def test_example1_symmetric(self):
        self._check(_build_tree([1, 2, 2, 3, 4, 4, 3]), True)

    def test_example2_asymmetric_structure(self):
        self._check(_build_tree([1, 2, 2, None, 3, None, 3]), False)

    def test_single_node(self):
        self._check(TreeNode(1), True)

    def test_empty_tree(self):
        self._check(None, True)

    def test_asymmetric_values(self):
        self._check(_build_tree([1, 2, 3]), False)

    def test_two_level_symmetric(self):
        self._check(_build_tree([1, 2, 2]), True)

    def test_left_only_child(self):
        self._check(TreeNode(1, TreeNode(2)), False)

    def test_negative_values_symmetric(self):
        self._check(_build_tree([1, -2, -2, 3, -4, -4, 3]), True)

    def test_all_same_values(self):
        self._check(_build_tree([1, 1, 1, 1, 1, 1, 1]), True)

    def test_deep_symmetric_with_gaps(self):
        self._check(_build_tree([1, 2, 2, 3, None, None, 3]), True)


if __name__ == "__main__":
    unittest.main()
