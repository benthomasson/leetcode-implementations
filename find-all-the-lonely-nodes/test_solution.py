"""Tests for Find All The Lonely Nodes (LeetCode 1469)."""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import Solution, TreeNode, build_tree


class TestGetLonelyNodes(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- Problem examples ---
    def test_example1(self):
        root = build_tree([1, 2, 3, None, 4])
        self.assertEqual(sorted(self.sol.getLonelyNodes(root)), [4])

    def test_example2(self):
        root = build_tree([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2])
        self.assertEqual(sorted(self.sol.getLonelyNodes(root)), [2, 6])

    def test_example3(self):
        root = build_tree([11, 99, 88, 77, None, None, 66, 55, None, None, 44, 33, None, None, 22])
        self.assertEqual(sorted(self.sol.getLonelyNodes(root)), [22, 33, 44, 55, 66, 77])

    # --- Edge cases ---
    def test_none_root(self):
        self.assertEqual(self.sol.getLonelyNodes(None), [])

    def test_single_node(self):
        self.assertEqual(self.sol.getLonelyNodes(TreeNode(42)), [])

    def test_full_binary_tree_no_lonely(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.sol.getLonelyNodes(root), [])

    def test_left_only_chain(self):
        root = build_tree([1, 2, None, 3, None, 4, None])
        self.assertEqual(sorted(self.sol.getLonelyNodes(root)), [2, 3, 4])

    def test_right_only_chain(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(sorted(self.sol.getLonelyNodes(root)), [2, 3])

    def test_root_with_one_child(self):
        root = TreeNode(1, TreeNode(2))
        self.assertEqual(self.sol.getLonelyNodes(root), [2])

    def test_large_values(self):
        root = TreeNode(1000000, TreeNode(999999), None)
        self.assertEqual(self.sol.getLonelyNodes(root), [999999])


if __name__ == "__main__":
    unittest.main()
