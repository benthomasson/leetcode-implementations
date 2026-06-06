"""Tests for Find Mode in Binary Search Tree."""
import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import TreeNode, findMode


class TestFindMode(unittest.TestCase):
    def test_example1(self):
        """[1,null,2,2] -> [2]"""
        root = TreeNode(1, None, TreeNode(2, TreeNode(2)))
        self.assertEqual(findMode(root), [2])

    def test_example2(self):
        """[0] -> [0]"""
        self.assertEqual(findMode(TreeNode(0)), [0])

    def test_single_node_negative(self):
        self.assertEqual(findMode(TreeNode(-100000)), [-100000])

    def test_all_same(self):
        root = TreeNode(5, TreeNode(5), TreeNode(5))
        self.assertEqual(findMode(root), [5])

    def test_multiple_modes(self):
        # 1 appears twice, 2 appears twice
        root = TreeNode(1, TreeNode(1), TreeNode(2, None, TreeNode(2)))
        self.assertCountEqual(findMode(root), [1, 2])

    def test_all_unique(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertCountEqual(findMode(root), [1, 2, 3])

    def test_right_skewed_with_mode(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(2)))
        self.assertEqual(findMode(root), [2])

    def test_deeper_tree(self):
        #       3
        #      / \
        #     2   3
        #    /
        #   2
        root = TreeNode(3, TreeNode(2, TreeNode(2)), TreeNode(3))
        self.assertCountEqual(findMode(root), [2, 3])

    def test_negative_values(self):
        root = TreeNode(-1, TreeNode(-1), TreeNode(0))
        self.assertEqual(findMode(root), [-1])


if __name__ == "__main__":
    unittest.main()
