"""Maximum Depth of Binary Tree - LeetCode #104."""

from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    """Return the maximum depth of a binary tree.

    Args:
        root: Root node of the binary tree.

    Returns:
        Maximum depth (number of nodes on longest root-to-leaf path).
    """
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


class TestMaxDepth(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(maxDepth(None), 0)

    def test_single_node(self):
        self.assertEqual(maxDepth(TreeNode(1)), 1)

    def test_example1(self):
        #     3
        #    / \
        #   9  20
        #      / \
        #     15   7
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(maxDepth(root), 3)

    def test_example2(self):
        #   1
        #    \
        #     2
        root = TreeNode(1, None, TreeNode(2))
        self.assertEqual(maxDepth(root), 2)

    def test_left_skewed(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        self.assertEqual(maxDepth(root), 4)

    def test_right_skewed(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(maxDepth(root), 3)

    def test_balanced(self):
        #       1
        #      / \
        #     2   3
        #    / \
        #   4   5
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertEqual(maxDepth(root), 3)


if __name__ == "__main__":
    unittest.main()
