"""Tests for Univalued Binary Tree (LeetCode #965)."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import Solution, TreeNode


class TestIsUnivalTree(unittest.TestCase):
    def setUp(self):
        self.solve = Solution().isUnivalTree

    # --- LeetCode examples ---
    def test_example1_all_ones(self):
        # [1,1,1,1,1,null,1]
        root = TreeNode(1,
            TreeNode(1, TreeNode(1), TreeNode(1)),
            TreeNode(1, None, TreeNode(1)))
        self.assertTrue(self.solve(root))

    def test_example2_mismatch(self):
        # [2,2,2,5,2]
        root = TreeNode(2,
            TreeNode(2, TreeNode(5), TreeNode(2)),
            TreeNode(2))
        self.assertFalse(self.solve(root))

    # --- Edge cases ---
    def test_single_node(self):
        self.assertTrue(self.solve(TreeNode(0)))

    def test_none_root(self):
        self.assertTrue(self.solve(None))

    def test_mismatch_only_at_deepest_leaf(self):
        root = TreeNode(5,
            TreeNode(5, TreeNode(5, TreeNode(99))),
            TreeNode(5))
        self.assertFalse(self.solve(root))

    def test_mismatch_at_root_right(self):
        self.assertFalse(self.solve(TreeNode(1, None, TreeNode(2))))

    def test_all_zeros(self):
        root = TreeNode(0, TreeNode(0), TreeNode(0))
        self.assertTrue(self.solve(root))

    def test_value_99_boundary(self):
        root = TreeNode(99, TreeNode(99), TreeNode(99))
        self.assertTrue(self.solve(root))


if __name__ == "__main__":
    unittest.main()
