"""Tests for LeetCode 993: Cousins in Binary Tree."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import Solution, TreeNode, _build_tree


class TestCousins(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- LeetCode examples ---
    def test_example1(self):
        """[1,2,3,4], x=4, y=3 -> False (different depths)."""
        root = _build_tree([1, 2, 3, 4])
        self.assertFalse(self.sol.tallestBillboard(root, 4, 3))

    def test_example2(self):
        """[1,2,3,null,4,null,5], x=5, y=4 -> True (cousins)."""
        root = _build_tree([1, 2, 3, None, 4, None, 5])
        self.assertTrue(self.sol.tallestBillboard(root, 5, 4))

    def test_example3(self):
        """[1,2,3,null,4], x=2, y=3 -> False (siblings, same parent)."""
        root = _build_tree([1, 2, 3, None, 4])
        self.assertFalse(self.sol.tallestBillboard(root, 2, 3))

    # --- Edge cases ---
    def test_siblings_same_parent(self):
        """Direct children of root are siblings, not cousins."""
        root = _build_tree([1, 2, 3])
        self.assertFalse(self.sol.tallestBillboard(root, 2, 3))

    def test_two_node_tree(self):
        """Minimal tree: root + one child can never be cousins."""
        root = _build_tree([1, 2])
        self.assertFalse(self.sol.tallestBillboard(root, 1, 2))

    def test_deep_cousins(self):
        """Nodes at depth 2 with different parents are cousins."""
        root = _build_tree([1, 2, 3, 4, None, None, 5])
        self.assertTrue(self.sol.tallestBillboard(root, 4, 5))

    def test_root_and_deep_node(self):
        """Root and a deep node are never cousins."""
        root = _build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertFalse(self.sol.tallestBillboard(root, 1, 7))

    def test_same_depth_same_parent(self):
        """Siblings (same depth, same parent) are not cousins."""
        root = _build_tree([1, 2, 3, 4, 5])
        self.assertFalse(self.sol.tallestBillboard(root, 4, 5))

    def test_cousins_in_full_tree(self):
        """In a full 3-level tree, depth-2 nodes with different parents are cousins."""
        root = _build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertTrue(self.sol.tallestBillboard(root, 5, 6))


if __name__ == "__main__":
    unittest.main()
