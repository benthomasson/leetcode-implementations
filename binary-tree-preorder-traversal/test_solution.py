"""Tests for Binary Tree Preorder Traversal."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution, TreeNode


class TestPreorderTraversal(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- LeetCode examples ---
    def test_example1(self):
        # [1,null,2,3] -> [1,2,3]
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        self.assertEqual(self.sol.preorderTraversal(root), [1, 2, 3])

    def test_example2_empty(self):
        self.assertEqual(self.sol.preorderTraversal(None), [])

    def test_example3_single(self):
        self.assertEqual(self.sol.preorderTraversal(TreeNode(1)), [1])

    # --- Edge cases ---
    def test_left_only_chain(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(self.sol.preorderTraversal(root), [1, 2, 3])

    def test_right_only_chain(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(self.sol.preorderTraversal(root), [1, 2, 3])

    def test_complete_tree(self):
        #       1
        #      / \
        #     2   3
        #    / \
        #   4   5
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertEqual(self.sol.preorderTraversal(root), [1, 2, 4, 5, 3])

    def test_negative_values(self):
        root = TreeNode(-100, TreeNode(0), TreeNode(100))
        self.assertEqual(self.sol.preorderTraversal(root), [-100, 0, 100])

    def test_val_zero(self):
        root = TreeNode(0)
        self.assertEqual(self.sol.preorderTraversal(root), [0])


if __name__ == "__main__":
    unittest.main()
