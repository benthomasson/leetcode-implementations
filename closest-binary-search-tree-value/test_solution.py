"""Tests for Closest Binary Search Tree Value solution."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import Solution, TreeNode, _build


class TestClosestValue(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        root = _build([4, 2, 5, 1, 3])
        self.assertEqual(self.s.closestValue(root, 3.714286), 4)

    def test_example2(self):
        root = _build([1])
        self.assertEqual(self.s.closestValue(root, 4.428571), 1)

    def test_exact_match(self):
        root = _build([4, 2, 5, 1, 3])
        self.assertEqual(self.s.closestValue(root, 3.0), 3)

    def test_tie_returns_smaller(self):
        root = _build([4, 2, 5])
        self.assertEqual(self.s.closestValue(root, 3.0), 2)

    def test_single_node_exact(self):
        root = TreeNode(7)
        self.assertEqual(self.s.closestValue(root, 7.0), 7)

    def test_left_skewed(self):
        root = TreeNode(5, TreeNode(3, TreeNode(1)))
        self.assertEqual(self.s.closestValue(root, 2.0), 1)

    def test_right_skewed(self):
        root = TreeNode(1, None, TreeNode(3, None, TreeNode(5)))
        self.assertEqual(self.s.closestValue(root, 4.0), 3)

    def test_target_beyond_max(self):
        root = _build([4, 2, 5, 1, 3])
        self.assertEqual(self.s.closestValue(root, 100.0), 5)

    def test_target_below_min(self):
        root = _build([4, 2, 5, 1, 3])
        self.assertEqual(self.s.closestValue(root, -100.0), 1)

    def test_large_values(self):
        root = TreeNode(1000000000)
        self.assertEqual(self.s.closestValue(root, -1000000000.0), 1000000000)


if __name__ == "__main__":
    unittest.main()
