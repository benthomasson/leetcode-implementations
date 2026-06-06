"""Minimum Distance Between BST Nodes."""

from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode]) -> int:
        """Return the minimum difference between any two nodes in a BST.

        Args:
            root: Root of the BST.

        Returns:
            Minimum absolute difference between any two node values.
        """
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)

        inorder(root)
        return self.min_diff


def build_tree(vals):
    """Build a tree from level-order list."""
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while i < len(vals):
        node = queue.pop(0)
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        root = build_tree([4, 2, 6, 1, 3])
        self.assertEqual(self.sol.searchBST(root), 1)

    def test_example2(self):
        root = build_tree([1, 0, 48, None, None, 12, 49])
        self.assertEqual(self.sol.searchBST(root), 1)

    def test_two_nodes(self):
        root = TreeNode(1, TreeNode(0))
        self.assertEqual(self.sol.searchBST(root), 1)

    def test_large_gap(self):
        root = TreeNode(0, None, TreeNode(100000))
        self.assertEqual(self.sol.searchBST(root), 100000)

    def test_all_consecutive(self):
        # Tree: 2(1, 3)
        root = build_tree([2, 1, 3])
        self.assertEqual(self.sol.searchBST(root), 1)

    def test_skewed_right(self):
        root = TreeNode(1, None, TreeNode(5, None, TreeNode(10)))
        self.assertEqual(self.sol.searchBST(root), 4)


if __name__ == "__main__":
    unittest.main()
