"""Tests for Find a Corresponding Node in a Clone of a Binary Tree."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import TreeNode, getTargetCopy


def clone(node):
    if not node:
        return None
    c = TreeNode(node.val)
    c.left = clone(node.left)
    c.right = clone(node.right)
    return c


class TestGetTargetCopy(unittest.TestCase):

    # --- LeetCode examples ---

    def test_example1(self):
        """tree=[7,4,3,null,null,6,19], target=3"""
        root = TreeNode(7, TreeNode(4), TreeNode(3, TreeNode(6), TreeNode(19)))
        target = root.right
        cloned = clone(root)
        result = getTargetCopy(root, cloned, target)
        self.assertEqual(result.val, 3)
        self.assertIs(result, cloned.right)

    def test_example2_single_node(self):
        """tree=[7], target=7"""
        root = TreeNode(7)
        cloned = clone(root)
        result = getTargetCopy(root, cloned, root)
        self.assertEqual(result.val, 7)
        self.assertIs(result, cloned)

    def test_example3_right_skewed(self):
        """tree=[8,null,6,null,5,null,4,null,3,null,2,null,1], target=4"""
        root = TreeNode(8)
        cur = root
        for v in [6, 5, 4, 3, 2, 1]:
            cur.right = TreeNode(v)
            cur = cur.right
        target = root.right.right.right  # node 4
        cloned = clone(root)
        result = getTargetCopy(root, cloned, target)
        self.assertEqual(result.val, 4)
        self.assertIs(result, cloned.right.right.right)

    # --- Edge cases ---

    def test_target_is_root(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        cloned = clone(root)
        result = getTargetCopy(root, cloned, root)
        self.assertIs(result, cloned)

    def test_target_is_deepest_leaf(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        target = root.left.left  # node 4, deepest left leaf
        cloned = clone(root)
        result = getTargetCopy(root, cloned, target)
        self.assertEqual(result.val, 4)
        self.assertIs(result, cloned.left.left)

    def test_left_skewed(self):
        root = TreeNode(1)
        cur = root
        for v in [2, 3, 4]:
            cur.left = TreeNode(v)
            cur = cur.left
        target = cur  # deepest node, val 4
        cloned = clone(root)
        result = getTargetCopy(root, cloned, target)
        self.assertEqual(result.val, 4)
        self.assertIs(result, cloned.left.left.left)

    def test_target_in_right_subtree(self):
        """Ensure right subtree is searched when target is not in left."""
        root = TreeNode(1, TreeNode(2), TreeNode(3, None, TreeNode(5)))
        target = root.right.right  # node 5
        cloned = clone(root)
        result = getTargetCopy(root, cloned, target)
        self.assertEqual(result.val, 5)
        self.assertIs(result, cloned.right.right)

    def test_result_is_not_original_node(self):
        """Result must be from cloned tree, not original."""
        root = TreeNode(10, TreeNode(20), TreeNode(30))
        target = root.left
        cloned = clone(root)
        result = getTargetCopy(root, cloned, target)
        self.assertIsNot(result, target)
        self.assertEqual(result.val, target.val)


if __name__ == "__main__":
    unittest.main()
