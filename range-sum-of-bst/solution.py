"""Range Sum of BST - LeetCode 938."""
from __future__ import annotations
import unittest
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


def range_sum_bst(root: Optional[TreeNode], low: int, high: int) -> int:
    """Return the sum of all BST node values in [low, high].

    Args:
        root: Root of the binary search tree.
        low: Lower bound (inclusive).
        high: Upper bound (inclusive).

    Returns:
        Sum of node values within the range.
    """
    if not root:
        return 0
    if root.val < low:
        return range_sum_bst(root.right, low, high)
    if root.val > high:
        return range_sum_bst(root.left, low, high)
    return root.val + range_sum_bst(root.left, low, high) + range_sum_bst(root.right, low, high)


# --- Tests ---

def _build_tree(values: list) -> Optional[TreeNode]:
    """Build a tree from level-order list (None for missing nodes)."""
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


class TestRangeSumBST(unittest.TestCase):

    def test_example1(self):
        root = _build_tree([10, 5, 15, 3, 7, None, 18])
        self.assertEqual(range_sum_bst(root, 7, 15), 32)

    def test_example2(self):
        root = _build_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
        self.assertEqual(range_sum_bst(root, 6, 10), 23)

    def test_single_node_in_range(self):
        self.assertEqual(range_sum_bst(TreeNode(5), 1, 10), 5)

    def test_single_node_out_of_range(self):
        self.assertEqual(range_sum_bst(TreeNode(5), 6, 10), 0)

    def test_all_in_range(self):
        root = _build_tree([5, 3, 7])
        self.assertEqual(range_sum_bst(root, 1, 100), 15)

    def test_none_in_range(self):
        root = _build_tree([5, 3, 7])
        self.assertEqual(range_sum_bst(root, 20, 30), 0)

    def test_empty_tree(self):
        self.assertEqual(range_sum_bst(None, 1, 10), 0)

    def test_left_skewed(self):
        root = TreeNode(5, TreeNode(3, TreeNode(1)))
        self.assertEqual(range_sum_bst(root, 1, 3), 4)

    def test_boundary_values(self):
        root = _build_tree([10, 5, 15, 3, 7, None, 18])
        self.assertEqual(range_sum_bst(root, 5, 10), 22)  # 5 + 7 + 10


if __name__ == "__main__":
    unittest.main()
