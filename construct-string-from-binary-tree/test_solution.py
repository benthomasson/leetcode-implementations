"""Tests for Construct String from Binary Tree."""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import TreeNode, tree2str


class TestTree2Str(unittest.TestCase):
    # --- Problem examples ---
    def test_example1(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        self.assertEqual(tree2str(root), "1(2(4))(3)")

    def test_example2(self):
        root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
        self.assertEqual(tree2str(root), "1(2()(4))(3)")

    # --- Edge cases ---
    def test_none_root(self):
        self.assertEqual(tree2str(None), "")

    def test_single_node(self):
        self.assertEqual(tree2str(TreeNode(42)), "42")

    def test_left_child_only(self):
        self.assertEqual(tree2str(TreeNode(1, TreeNode(2))), "1(2)")

    def test_right_child_only(self):
        """Right-only requires empty () for missing left to preserve mapping."""
        self.assertEqual(tree2str(TreeNode(1, None, TreeNode(3))), "1()(3)")

    def test_negative_values(self):
        root = TreeNode(-1, TreeNode(-2), TreeNode(-3))
        self.assertEqual(tree2str(root), "-1(-2)(-3)")

    def test_zero_value(self):
        self.assertEqual(tree2str(TreeNode(0, TreeNode(0))), "0(0)")

    def test_deep_left_chain(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(tree2str(root), "1(2(3))")

    def test_boundary_values(self):
        root = TreeNode(-1000, None, TreeNode(1000))
        self.assertEqual(tree2str(root), "-1000()(1000)")


if __name__ == "__main__":
    unittest.main()
