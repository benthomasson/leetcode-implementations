"""Tests for Path Sum solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import TreeNode, hasPathSum


class TestPathSum(unittest.TestCase):
    # --- LeetCode examples ---

    def test_example1_target_22(self):
        root = TreeNode(5,
            TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
            TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
        self.assertTrue(hasPathSum(root, 22))

    def test_example2_no_path(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertFalse(hasPathSum(root, 5))

    def test_example3_empty_tree(self):
        self.assertFalse(hasPathSum(None, 0))

    # --- Edge cases ---

    def test_single_node_match(self):
        self.assertTrue(hasPathSum(TreeNode(5), 5))

    def test_single_node_no_match(self):
        self.assertFalse(hasPathSum(TreeNode(5), 1))

    def test_negative_values(self):
        root = TreeNode(-2, None, TreeNode(-3))
        self.assertTrue(hasPathSum(root, -5))

    def test_non_leaf_sum_should_not_match(self):
        # targetSum equals root value, but root is not a leaf
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertFalse(hasPathSum(root, 1))

    def test_right_only_path(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertTrue(hasPathSum(root, 6))
        self.assertFalse(hasPathSum(root, 3))

    def test_example1_wrong_target(self):
        root = TreeNode(5,
            TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
            TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
        self.assertFalse(hasPathSum(root, 99))

    def test_all_negative_path(self):
        root = TreeNode(-1, TreeNode(-2, TreeNode(-3)))
        self.assertTrue(hasPathSum(root, -6))


if __name__ == "__main__":
    unittest.main()
