"""Find All The Lonely Nodes - LeetCode 1469."""
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        """Return values of all lonely nodes (only children) in a binary tree.

        Args:
            root: Root of the binary tree.

        Returns:
            List of lonely node values in any order.
        """
        result = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            if node.left and not node.right:
                result.append(node.left.val)
            elif node.right and not node.left:
                result.append(node.right.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result


# --- Tests ---
import unittest
from collections import deque


def build_tree(vals: list) -> Optional[TreeNode]:
    """Build a binary tree from level-order list (None for missing nodes)."""
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    while i < len(vals):
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


class TestGetLonelyNodes(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        root = build_tree([1, 2, 3, None, 4])
        self.assertEqual(sorted(self.sol.getLonelyNodes(root)), [4])

    def test_example2(self):
        root = build_tree([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2])
        self.assertEqual(sorted(self.sol.getLonelyNodes(root)), [2, 6])

    def test_example3(self):
        root = build_tree([11, 99, 88, 77, None, None, 66, 55, None, None, 44, 33, None, None, 22])
        self.assertEqual(sorted(self.sol.getLonelyNodes(root)), [22, 33, 44, 55, 66, 77])

    def test_single_node(self):
        self.assertEqual(self.sol.getLonelyNodes(TreeNode(1)), [])

    def test_none(self):
        self.assertEqual(self.sol.getLonelyNodes(None), [])

    def test_full_binary_tree(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.sol.getLonelyNodes(root), [])

    def test_left_chain(self):
        root = build_tree([1, 2, None, 3, None, 4, None])
        self.assertEqual(sorted(self.sol.getLonelyNodes(root)), [2, 3, 4])

    def test_right_chain(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(sorted(self.sol.getLonelyNodes(root)), [2, 3])


if __name__ == "__main__":
    unittest.main()
