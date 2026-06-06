"""Find a Corresponding Node of a Binary Tree in a Clone of That Tree."""

from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    """Find the corresponding node in cloned tree matching target in original.

    Args:
        original: Root of the original binary tree.
        cloned: Root of the cloned binary tree.
        target: Reference to a node in the original tree.

    Returns:
        Reference to the corresponding node in the cloned tree.
    """
    if original is target:
        return cloned
    if original is None:
        return None
    left = getTargetCopy(original.left, cloned.left, target)
    if left:
        return left
    return getTargetCopy(original.right, cloned.right, target)


# --- Tests ---

class TestGetTargetCopy(unittest.TestCase):

    def _clone(self, node):
        if not node:
            return None
        c = TreeNode(node.val)
        c.left = self._clone(node.left)
        c.right = self._clone(node.right)
        return c

    def test_example1(self):
        #       7
        #      / \
        #     4   3
        #        / \
        #       6  19
        root = TreeNode(7, TreeNode(4), TreeNode(3, TreeNode(6), TreeNode(19)))
        target = root.right  # node 3
        cloned = self._clone(root)
        result = getTargetCopy(root, cloned, target)
        self.assertEqual(result.val, 3)
        self.assertIs(result, cloned.right)

    def test_example2_single_node(self):
        root = TreeNode(7)
        cloned = self._clone(root)
        result = getTargetCopy(root, cloned, root)
        self.assertEqual(result.val, 7)
        self.assertIs(result, cloned)

    def test_example3_right_skewed(self):
        # 8 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 (all right children)
        root = TreeNode(8)
        cur = root
        for v in [6, 5, 4, 3, 2, 1]:
            cur.right = TreeNode(v)
            cur = cur.right
        target = root.right.right.right  # node 4
        cloned = self._clone(root)
        result = getTargetCopy(root, cloned, target)
        self.assertEqual(result.val, 4)
        self.assertIs(result, cloned.right.right.right)

    def test_target_is_root(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        cloned = self._clone(root)
        result = getTargetCopy(root, cloned, root)
        self.assertIs(result, cloned)

    def test_target_is_leaf(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        target = root.left.right  # node 5
        cloned = self._clone(root)
        result = getTargetCopy(root, cloned, target)
        self.assertEqual(result.val, 5)
        self.assertIs(result, cloned.left.right)

    def test_left_skewed(self):
        root = TreeNode(1)
        cur = root
        for v in [2, 3, 4]:
            cur.left = TreeNode(v)
            cur = cur.left
        target = cur  # deepest node, val 4
        cloned = self._clone(root)
        result = getTargetCopy(root, cloned, target)
        self.assertEqual(result.val, 4)
        self.assertIs(result, cloned.left.left.left)


if __name__ == "__main__":
    unittest.main()
