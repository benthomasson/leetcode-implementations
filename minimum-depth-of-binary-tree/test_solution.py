"""Tests for minimum depth of binary tree."""

import unittest
from solution import Solution, TreeNode


class TestMinDepth(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.s.minDepth(None), 0)

    def test_single_node(self):
        self.assertEqual(self.s.minDepth(TreeNode(1)), 1)

    def test_example1(self):
        #     3
        #    / \
        #   9  20
        #      / \
        #     15  7
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(self.s.minDepth(root), 2)

    def test_example2_right_skewed(self):
        # 2 -> 3 -> 4 -> 5 -> 6 (all right children)
        root = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
        self.assertEqual(self.s.minDepth(root), 5)

    def test_left_skewed(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        self.assertEqual(self.s.minDepth(root), 4)

    def test_balanced(self):
        #     1
        #    / \
        #   2   3
        #  / \
        # 4   5
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertEqual(self.s.minDepth(root), 2)

    def test_one_child_not_leaf(self):
        # Node with one child should NOT be treated as leaf
        root = TreeNode(1, TreeNode(2))
        self.assertEqual(self.s.minDepth(root), 2)


if __name__ == "__main__":
    unittest.main()
