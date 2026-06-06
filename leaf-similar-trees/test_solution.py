"""Tests for Leaf-Similar Trees solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution, TreeNode, build_tree


class TestLeafSimilar(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- LeetCode examples ---

    def test_example1_same_leaves_different_structure(self):
        r1 = build_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
        r2 = build_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
        self.assertTrue(self.sol.leafSimilar(r1, r2))

    def test_example2_different_leaves(self):
        r1 = build_tree([1, 2, 3])
        r2 = build_tree([1, 3, 2])
        self.assertFalse(self.sol.leafSimilar(r1, r2))

    # --- Edge cases ---

    def test_single_node_equal(self):
        self.assertTrue(self.sol.leafSimilar(TreeNode(0), TreeNode(0)))

    def test_single_node_unequal(self):
        self.assertFalse(self.sol.leafSimilar(TreeNode(0), TreeNode(200)))

    def test_identical_trees(self):
        r1 = build_tree([1, 2, 3])
        r2 = build_tree([1, 2, 3])
        self.assertTrue(self.sol.leafSimilar(r1, r2))

    def test_different_depth_same_leaves(self):
        # r1: single leaf 5
        # r2: deep chain ending in leaf 5
        r1 = TreeNode(5)
        r2 = TreeNode(1, TreeNode(2, TreeNode(5)))
        self.assertTrue(self.sol.leafSimilar(r1, r2))

    def test_same_leaves_different_count(self):
        # r1 leaves: [1]  r2 leaves: [1, 1]
        r1 = TreeNode(1)
        r2 = TreeNode(0, TreeNode(1), TreeNode(1))
        self.assertFalse(self.sol.leafSimilar(r1, r2))

    def test_all_left_skewed(self):
        # Both left-skewed, leaf at bottom
        r1 = TreeNode(1, TreeNode(2, TreeNode(3)))
        r2 = TreeNode(4, TreeNode(5, TreeNode(3)))
        self.assertTrue(self.sol.leafSimilar(r1, r2))

    def test_multiple_leaves_order_matters(self):
        # r1 leaves: [1, 2]  r2 leaves: [2, 1]
        r1 = TreeNode(0, TreeNode(1), TreeNode(2))
        r2 = TreeNode(0, TreeNode(2), TreeNode(1))
        self.assertFalse(self.sol.leafSimilar(r1, r2))

    def test_boundary_values(self):
        # Min and max constraint values
        r1 = TreeNode(0, TreeNode(0), TreeNode(200))
        r2 = TreeNode(100, TreeNode(0), TreeNode(200))
        self.assertTrue(self.sol.leafSimilar(r1, r2))


if __name__ == "__main__":
    unittest.main()
