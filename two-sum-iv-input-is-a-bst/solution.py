"""Two Sum IV - Input is a BST."""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


def findTarget(root: Optional[TreeNode], k: int) -> bool:
    """Check if two nodes in a BST sum to k.

    Args:
        root: Root of the binary search tree.
        k: Target sum.

    Returns:
        True if two distinct nodes sum to k, False otherwise.
    """
    if not root:
        return False
    seen = set()
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if k - node.val in seen:
            return True
        seen.add(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False


# --- Tests ---
import unittest


class TestFindTarget(unittest.TestCase):
    def _build(self, vals):
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

    def test_example1(self):
        root = self._build([5, 3, 6, 2, 4, None, 7])
        self.assertTrue(findTarget(root, 9))

    def test_example2(self):
        root = self._build([5, 3, 6, 2, 4, None, 7])
        self.assertFalse(findTarget(root, 28))

    def test_single_node(self):
        self.assertFalse(findTarget(TreeNode(1), 2))

    def test_two_nodes_true(self):
        root = TreeNode(1, right=TreeNode(2))
        self.assertTrue(findTarget(root, 3))

    def test_two_nodes_false(self):
        root = TreeNode(1, right=TreeNode(2))
        self.assertFalse(findTarget(root, 5))

    def test_negative_values(self):
        root = self._build([0, -3, 2])
        self.assertTrue(findTarget(root, -1))

    def test_empty_tree(self):
        self.assertFalse(findTarget(None, 0))


if __name__ == "__main__":
    unittest.main()
