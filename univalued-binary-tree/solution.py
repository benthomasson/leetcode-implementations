"""Univalued Binary Tree - LeetCode #965."""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        """Return True if every node in the binary tree has the same value.

        Args:
            root: Root of the binary tree.

        Returns:
            True if tree is uni-valued, False otherwise.
        """
        if not root:
            return True
        target = root.val

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            return node.val == target and dfs(node.left) and dfs(node.right)

        return dfs(root)


# --- Tests ---
import unittest


class TestIsUnivalTree(unittest.TestCase):
    def _solve(self, root):
        return Solution().isUnivalTree(root)

    def test_single_node(self):
        self.assertTrue(self._solve(TreeNode(1)))

    def test_all_same(self):
        #     1
        #    / \
        #   1   1
        #  / \   \
        # 1   1   1
        root = TreeNode(1,
            TreeNode(1, TreeNode(1), TreeNode(1)),
            TreeNode(1, None, TreeNode(1)))
        self.assertTrue(self._solve(root))

    def test_mismatch_right_child(self):
        #     2
        #    / \
        #   2   2
        #  / \
        # 5   2
        root = TreeNode(2,
            TreeNode(2, TreeNode(5), TreeNode(2)),
            TreeNode(2))
        self.assertFalse(self._solve(root))

    def test_mismatch_deep_leaf(self):
        root = TreeNode(1,
            TreeNode(1, TreeNode(1, TreeNode(2))),
            TreeNode(1))
        self.assertFalse(self._solve(root))

    def test_two_nodes_same(self):
        self.assertTrue(self._solve(TreeNode(0, TreeNode(0))))

    def test_two_nodes_different(self):
        self.assertFalse(self._solve(TreeNode(0, TreeNode(1))))

    def test_none_root(self):
        self.assertTrue(self._solve(None))

    def test_mismatch_at_right_subtree_leaf(self):
        root = TreeNode(3, TreeNode(3), TreeNode(3, None, TreeNode(7)))
        self.assertFalse(self._solve(root))


if __name__ == "__main__":
    unittest.main()
