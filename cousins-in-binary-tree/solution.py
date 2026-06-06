"""LeetCode 993: Cousins in Binary Tree."""

from collections import deque
from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        """Determine if two nodes in a binary tree are cousins.

        Cousins share the same depth but have different parents.
        Uses BFS to process nodes level by level.

        Args:
            root: Root of the binary tree.
            x: Value of the first node.
            y: Value of the second node.

        Returns:
            True if x and y are cousins, False otherwise.
        """
        if not root:
            return False

        queue = deque([(root, None)])  # (node, parent)

        while queue:
            level_size = len(queue)
            x_parent = y_parent = None

            for _ in range(level_size):
                node, parent = queue.popleft()

                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent

                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

            if x_parent and y_parent:
                return x_parent != y_parent
            if x_parent or y_parent:
                return False  # Only one found at this level

        return False


def _build_tree(vals: list) -> Optional[TreeNode]:
    """Build a tree from level-order list (None for missing nodes)."""
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


class TestCousins(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1_not_cousins_diff_depth(self):
        root = _build_tree([1, 2, 3, 4])
        self.assertFalse(self.sol.isCousins(root, 4, 3))

    def test_example2_cousins(self):
        root = _build_tree([1, 2, 3, None, 4, None, 5])
        self.assertTrue(self.sol.isCousins(root, 5, 4))

    def test_example3_siblings_not_cousins(self):
        root = _build_tree([1, 2, 3, None, 4])
        self.assertFalse(self.sol.isCousins(root, 2, 3))

    def test_siblings_same_parent(self):
        root = _build_tree([1, 2, 3])
        self.assertFalse(self.sol.isCousins(root, 2, 3))

    def test_two_node_tree(self):
        root = _build_tree([1, 2])
        self.assertFalse(self.sol.isCousins(root, 1, 2))

    def test_deep_cousins(self):
        root = _build_tree([1, 2, 3, 4, None, None, 5])
        self.assertTrue(self.sol.isCousins(root, 4, 5))


if __name__ == "__main__":
    unittest.main()
