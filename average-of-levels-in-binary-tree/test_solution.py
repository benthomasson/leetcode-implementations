"""Tests for Average of Levels in Binary Tree."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution, TreeNode


class TestAverageOfLevels(unittest.TestCase):
    def setUp(self):
        self.solve = Solution().averageOfLevels

    # --- Problem examples ---
    def test_example1(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(self.solve(root), [3.0, 14.5, 11.0])

    def test_example2(self):
        root = TreeNode(3, TreeNode(9, TreeNode(15), TreeNode(7)), TreeNode(20))
        self.assertEqual(self.solve(root), [3.0, 14.5, 11.0])

    # --- Edge cases ---
    def test_single_node(self):
        self.assertEqual(self.solve(TreeNode(0)), [0.0])

    def test_single_node_negative(self):
        self.assertEqual(self.solve(TreeNode(-1)), [-1.0])

    def test_left_skewed(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(self.solve(root), [1.0, 2.0, 3.0])

    def test_right_skewed(self):
        root = TreeNode(10, None, TreeNode(20, None, TreeNode(30)))
        self.assertEqual(self.solve(root), [10.0, 20.0, 30.0])

    def test_large_values(self):
        big = 2**31 - 1
        neg = -(2**31)
        root = TreeNode(big, TreeNode(neg), TreeNode(neg))
        self.assertAlmostEqual(self.solve(root)[0], float(big))
        self.assertAlmostEqual(self.solve(root)[1], float(neg))

    def test_mixed_positive_negative(self):
        root = TreeNode(0, TreeNode(-10), TreeNode(10))
        result = self.solve(root)
        self.assertEqual(result, [0.0, 0.0])


if __name__ == "__main__":
    unittest.main()
