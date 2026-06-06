"""Tests for Search in a Binary Search Tree."""

import sys
import unittest
from typing import Optional

sys.path.insert(0, "../implementer")
from solution import TreeNode, searchBST


def build(vals) -> Optional[TreeNode]:
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


def to_list(root: Optional[TreeNode]) -> list:
    """Convert tree to level-order list."""
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


class TestSearchBST(unittest.TestCase):
    # --- Problem examples ---
    def test_example1_found(self):
        root = build([4, 2, 7, 1, 3])
        self.assertEqual(to_list(searchBST(root, 2)), [2, 1, 3])

    def test_example2_not_found(self):
        root = build([4, 2, 7, 1, 3])
        self.assertIsNone(searchBST(root, 5))

    # --- Edge cases ---
    def test_none_root(self):
        self.assertIsNone(searchBST(None, 1))

    def test_single_node_found(self):
        root = TreeNode(1)
        self.assertIs(searchBST(root, 1), root)

    def test_single_node_not_found(self):
        self.assertIsNone(searchBST(TreeNode(1), 2))

    def test_root_is_target(self):
        root = build([4, 2, 7, 1, 3])
        self.assertEqual(to_list(searchBST(root, 4)), [4, 2, 7, 1, 3])

    def test_leaf_node(self):
        root = build([4, 2, 7, 1, 3])
        self.assertEqual(to_list(searchBST(root, 1)), [1])

    def test_right_subtree(self):
        root = build([4, 2, 7, 1, 3])
        self.assertEqual(to_list(searchBST(root, 7)), [7])

    # --- Returns same node object (subtree reference) ---
    def test_returns_original_node(self):
        root = build([4, 2, 7, 1, 3])
        result = searchBST(root, 2)
        self.assertIs(result, root.left)


if __name__ == "__main__":
    unittest.main()
