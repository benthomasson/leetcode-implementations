"""Tests for Minimum Absolute Difference in BST."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import Solution, TreeNode, build_tree


class TestMinAbsDiff(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- LeetCode examples ---

    def test_example1(self):
        root = build_tree([4, 2, 6, 1, 3])
        self.assertEqual(self.sol.getMinimumDifference(root), 1)

    def test_example2(self):
        root = build_tree([1, 0, 48, None, None, 12, 49])
        self.assertEqual(self.sol.getMinimumDifference(root), 1)

    # --- Edge cases ---

    def test_two_nodes_min_case(self):
        root = TreeNode(1, right=TreeNode(5))
        self.assertEqual(self.sol.getMinimumDifference(root), 4)

    def test_two_nodes_adjacent_values(self):
        root = TreeNode(0, right=TreeNode(1))
        self.assertEqual(self.sol.getMinimumDifference(root), 1)

    def test_skewed_left(self):
        # 10 <- 7 <- 3 <- 1
        root = TreeNode(10, left=TreeNode(7, left=TreeNode(3, left=TreeNode(1))))
        self.assertEqual(self.sol.getMinimumDifference(root), 2)  # 3-1=2? No, 7-3=4, 10-7=3, 3-1=2 => min=2

    def test_skewed_right(self):
        root = TreeNode(1, right=TreeNode(3, right=TreeNode(7, right=TreeNode(10))))
        self.assertEqual(self.sol.getMinimumDifference(root), 2)

    def test_all_same_diff(self):
        # BST: 2,4,6 — all diffs are 2
        root = TreeNode(4, left=TreeNode(2), right=TreeNode(6))
        self.assertEqual(self.sol.getMinimumDifference(root), 2)

    def test_large_values(self):
        root = TreeNode(100000, left=TreeNode(0), right=TreeNode(100001))
        self.assertEqual(self.sol.getMinimumDifference(root), 1)

    def test_reuse_instance(self):
        """Ensure calling multiple times on same Solution instance works."""
        root1 = build_tree([4, 2, 6, 1, 3])
        root2 = TreeNode(10, left=TreeNode(1))
        self.assertEqual(self.sol.getMinimumDifference(root1), 1)
        self.assertEqual(self.sol.getMinimumDifference(root2), 9)


if __name__ == '__main__':
    unittest.main()
