"""LeetCode 897: Increasing Order Search Tree."""
from __future__ import annotations
from typing import Optional
import unittest
from collections import deque


class TreeNode:
    """Binary tree node."""
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Rearrange BST into right-skewed tree in in-order.

        Args:
            root: Root of the binary search tree.

        Returns:
            Root of the rearranged tree with only right children.
        """
        dummy = TreeNode(0)
        self.current = dummy

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder(node.left)
            node.left = None
            self.current.right = node
            self.current = node
            inorder(node.right)

        inorder(root)
        return dummy.right


# --- Helper ---

def build_tree(vals: list) -> Optional[TreeNode]:
    """Build a tree from level-order list (None for missing nodes)."""
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


def tree_to_list(root: Optional[TreeNode]) -> list:
    """Convert right-skewed tree to list [val, None, val, None, ...]."""
    result = []
    while root:
        result.append(root.val)
        if root.right:
            result.append(None)
        root = root.right
    return result


# --- Tests ---

class TestIncreasingBST(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        root = build_tree([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])
        result = self.sol.increasingBST(root)
        self.assertEqual(tree_to_list(result), [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])

    def test_example2(self):
        root = build_tree([5, 1, 7])
        result = self.sol.increasingBST(root)
        self.assertEqual(tree_to_list(result), [1, None, 5, None, 7])

    def test_single_node(self):
        root = TreeNode(42)
        result = self.sol.increasingBST(root)
        self.assertEqual(result.val, 42)
        self.assertIsNone(result.left)
        self.assertIsNone(result.right)

    def test_left_chain(self):
        root = build_tree([3, 2, None, 1])
        result = self.sol.increasingBST(root)
        self.assertEqual(tree_to_list(result), [1, None, 2, None, 3])

    def test_right_chain(self):
        root = build_tree([1, None, 2, None, 3])
        result = self.sol.increasingBST(root)
        self.assertEqual(tree_to_list(result), [1, None, 2, None, 3])

    def test_two_nodes_left(self):
        root = TreeNode(2, TreeNode(1))
        result = self.sol.increasingBST(root)
        self.assertEqual(tree_to_list(result), [1, None, 2])

    def test_two_nodes_right(self):
        root = TreeNode(1, None, TreeNode(2))
        result = self.sol.increasingBST(root)
        self.assertEqual(tree_to_list(result), [1, None, 2])

    def test_no_left_children_in_result(self):
        root = build_tree([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])
        result = self.sol.increasingBST(root)
        node = result
        while node:
            self.assertIsNone(node.left)
            node = node.right


if __name__ == "__main__":
    unittest.main()
