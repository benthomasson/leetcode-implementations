"""Tests for Two Sum IV - Input is a BST."""

import sys
import os
import unittest
from collections import deque

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import TreeNode, findTarget


def build_tree(vals):
    """Build tree from level-order list."""
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


class TestFindTarget(unittest.TestCase):
    # --- Problem examples ---
    def test_example1_sum_exists(self):
        root = build_tree([5, 3, 6, 2, 4, None, 7])
        self.assertTrue(findTarget(root, 9))  # 2+7 or 3+6 or 4+5

    def test_example2_sum_not_exists(self):
        root = build_tree([5, 3, 6, 2, 4, None, 7])
        self.assertFalse(findTarget(root, 28))

    # --- Edge cases ---
    def test_empty_tree(self):
        self.assertFalse(findTarget(None, 0))

    def test_single_node_cannot_pair(self):
        self.assertFalse(findTarget(TreeNode(5), 10))

    def test_two_nodes_match(self):
        root = TreeNode(2, right=TreeNode(3))
        self.assertTrue(findTarget(root, 5))

    def test_two_nodes_no_match(self):
        root = TreeNode(2, right=TreeNode(3))
        self.assertFalse(findTarget(root, 1))

    def test_negative_values(self):
        root = build_tree([0, -3, 2])
        self.assertTrue(findTarget(root, -1))  # -3 + 2

    def test_target_zero_with_negatives(self):
        root = build_tree([0, -1, 1])
        self.assertTrue(findTarget(root, 0))  # -1 + 1

    def test_root_value_plus_leaf(self):
        root = build_tree([5, 3, 6, 2, 4, None, 7])
        self.assertTrue(findTarget(root, 11))  # 5 + 6 or 4 + 7

    def test_no_double_counting_single_node(self):
        # k = 2*root.val but only one node => should be False
        self.assertFalse(findTarget(TreeNode(4), 8))


if __name__ == "__main__":
    unittest.main()
