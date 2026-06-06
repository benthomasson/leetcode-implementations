"""Tests for Minimum Distance Between BST Nodes."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import Solution, TreeNode, build_tree


class TestMinDistBST(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- Problem examples ---
    def test_example1(self):
        root = build_tree([4, 2, 6, 1, 3])
        self.assertEqual(self.sol.minDiffInBST(root), 1)

    def test_example2(self):
        root = build_tree([1, 0, 48, None, None, 12, 49])
        self.assertEqual(self.sol.minDiffInBST(root), 1)

    # --- Edge cases ---
    def test_two_nodes_min(self):
        root = TreeNode(1, TreeNode(0))
        self.assertEqual(self.sol.minDiffInBST(root), 1)

    def test_two_nodes_large_gap(self):
        root = TreeNode(0, None, TreeNode(100000))
        self.assertEqual(self.sol.minDiffInBST(root), 100000)

    def test_left_skewed(self):
        # 10 -> 5 -> 1
        root = TreeNode(10, TreeNode(5, TreeNode(1)))
        self.assertEqual(self.sol.minDiffInBST(root), 4)

    def test_right_skewed(self):
        # 1 -> 5 -> 10
        root = TreeNode(1, None, TreeNode(5, None, TreeNode(10)))
        self.assertEqual(self.sol.minDiffInBST(root), 4)

    def test_min_diff_not_parent_child(self):
        # In-order: 1, 3, 4, 6 -> min diff is 1 (between 3 and 4)
        root = build_tree([4, 3, 6, 1])
        self.assertEqual(self.sol.minDiffInBST(root), 1)

    def test_consecutive_values(self):
        root = build_tree([2, 1, 3])
        self.assertEqual(self.sol.minDiffInBST(root), 1)

    def test_reusability(self):
        """Ensure solution works correctly when called multiple times."""
        root1 = build_tree([4, 2, 6, 1, 3])
        root2 = TreeNode(0, None, TreeNode(100000))
        self.assertEqual(self.sol.minDiffInBST(root1), 1)
        self.assertEqual(self.sol.minDiffInBST(root2), 100000)


if __name__ == "__main__":
    unittest.main()
