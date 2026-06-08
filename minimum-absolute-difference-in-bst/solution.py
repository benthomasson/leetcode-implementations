"""Minimum Absolute Difference in BST."""

from typing import Optional
import unittest
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """Return the minimum absolute difference between any two nodes in a BST.

        Args:
            root: Root of a binary search tree with at least 2 nodes.

        Returns:
            Minimum absolute difference between any two node values.
        """
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)

        inorder(root)
        return int(self.min_diff)


# --- Tests ---

def build_tree(values: list) -> Optional[TreeNode]:
    """Build a binary tree from level-order list (None for missing nodes)."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class TestMinAbsDiff(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        root = build_tree([4, 2, 6, 1, 3])
        self.assertEqual(self.sol.getMinimumDifference(root), 1)

    def test_example2(self):
        root = build_tree([1, 0, 48, None, None, 12, 49])
        self.assertEqual(self.sol.getMinimumDifference(root), 1)

    def test_two_nodes(self):
        root = TreeNode(1, right=TreeNode(5))
        self.assertEqual(self.sol.getMinimumDifference(root), 4)

    def test_skewed_right(self):
        # 1 -> 3 -> 7 -> 10
        root = TreeNode(1, right=TreeNode(3, right=TreeNode(7, right=TreeNode(10))))
        self.assertEqual(self.sol.getMinimumDifference(root), 2)

    def test_large_gap_one_small(self):
        # BST: 0, 100000, 100001 — min diff is 1
        root = TreeNode(100000, left=TreeNode(0), right=TreeNode(100001))
        self.assertEqual(self.sol.getMinimumDifference(root), 1)

    def test_consecutive_values(self):
        # BST with consecutive integers: 1,2,3
        root = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
        self.assertEqual(self.sol.getMinimumDifference(root), 1)


if __name__ == '__main__':
    unittest.main()
