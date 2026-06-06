"""Tests for Sum of Left Leaves."""

import unittest
from solution import TreeNode, sum_of_left_leaves


class TestSumOfLeftLeaves(unittest.TestCase):

    def test_example1(self):
        #       3
        #      / \
        #     9  20
        #       /  \
        #      15   7
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(sum_of_left_leaves(root), 24)

    def test_example2_single_node(self):
        self.assertEqual(sum_of_left_leaves(TreeNode(1)), 0)

    def test_none_root(self):
        self.assertEqual(sum_of_left_leaves(None), 0)

    def test_left_only_chain(self):
        #     1
        #    /
        #   2
        #  /
        # 3
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(sum_of_left_leaves(root), 3)

    def test_right_only_tree(self):
        #  1
        #   \
        #    2
        #     \
        #      3
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(sum_of_left_leaves(root), 0)

    def test_all_left_leaves(self):
        #       1
        #      / \
        #     2   3
        #    /   /
        #   4   5
        root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5)))
        self.assertEqual(sum_of_left_leaves(root), 9)  # 4 + 5

    def test_negative_values(self):
        root = TreeNode(1, TreeNode(-10), TreeNode(5))
        self.assertEqual(sum_of_left_leaves(root), -10)


if __name__ == "__main__":
    unittest.main()
