"""Balanced Binary Tree - LeetCode"""

from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def getHeight(root: Optional[TreeNode]) -> int:
    """Return tree height if balanced, -1 if unbalanced.

    Args:
        root: Root node of the binary tree.

    Returns:
        Height of tree if balanced, -1 otherwise.
    """
    if root is None:
        return 0
    left = getHeight(root.left)
    if left == -1:
        return -1
    right = getHeight(root.right)
    if right == -1:
        return -1
    if abs(left - right) > 1:
        return -1
    return max(left, right) + 1


def isBalanced(root: Optional[TreeNode]) -> bool:
    """Determine if a binary tree is height-balanced.

    Args:
        root: Root node of the binary tree.

    Returns:
        True if the tree is height-balanced, False otherwise.
    """
    return getHeight(root) != -1


class TestBalancedBinaryTree(unittest.TestCase):
    def test_example1_balanced(self):
        #     3
        #    / \
        #   9  20
        #      / \
        #     15  7
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertTrue(isBalanced(root))

    def test_example2_unbalanced(self):
        #        1
        #       / \
        #      2   2
        #     / \
        #    3   3
        #   / \
        #  4   4
        root = TreeNode(1,
            TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
            TreeNode(2))
        self.assertFalse(isBalanced(root))

    def test_example3_empty(self):
        self.assertTrue(isBalanced(None))

    def test_single_node(self):
        self.assertTrue(isBalanced(TreeNode(1)))

    def test_left_chain(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertFalse(isBalanced(root))

    def test_right_chain(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertFalse(isBalanced(root))

    def test_perfect_tree(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        self.assertTrue(isBalanced(root))

    def test_height_diff_exactly_one(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4))
        self.assertTrue(isBalanced(root))

    def test_getHeight_returns_correct_height(self):
        self.assertEqual(getHeight(None), 0)
        self.assertEqual(getHeight(TreeNode(1)), 1)
        self.assertEqual(getHeight(TreeNode(1, TreeNode(2))), 2)

    def test_getHeight_returns_neg1_for_unbalanced(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(getHeight(root), -1)


if __name__ == "__main__":
    unittest.main()
