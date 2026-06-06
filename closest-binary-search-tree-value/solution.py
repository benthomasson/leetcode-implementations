"""Closest Binary Search Tree Value."""

from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """Return the value in the BST closest to target (smallest if tie).

        Args:
            root: Root of the binary search tree.
            target: Target value to find closest to.

        Returns:
            The closest value, preferring the smaller one on ties.
        """
        closest = root.val
        node = root
        while node:
            # Update closest: prefer smaller value on equal distance
            if (abs(node.val - target) < abs(closest - target) or
                    (abs(node.val - target) == abs(closest - target) and node.val < closest)):
                closest = node.val
            node = node.left if target < node.val else node.right
        return closest


# --- Tests ---

def _build(vals: list) -> Optional[TreeNode]:
    """Build a tree from level-order list (None = no node)."""
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while i < len(vals):
        curr = queue.pop(0)
        if i < len(vals) and vals[i] is not None:
            curr.left = TreeNode(vals[i])
            queue.append(curr.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            curr.right = TreeNode(vals[i])
            queue.append(curr.right)
        i += 1
    return root


class TestClosestValue(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        root = _build([4, 2, 5, 1, 3])
        self.assertEqual(self.s.closestValue(root, 3.714286), 4)

    def test_example2(self):
        root = _build([1])
        self.assertEqual(self.s.closestValue(root, 4.428571), 1)

    def test_exact_match(self):
        root = _build([4, 2, 5, 1, 3])
        self.assertEqual(self.s.closestValue(root, 3.0), 3)

    def test_tie_returns_smaller(self):
        # Target 3.0 equidistant from 2 and 4 → return 2
        root = _build([4, 2, 5])
        self.assertEqual(self.s.closestValue(root, 3.0), 2)

    def test_left_only_tree(self):
        root = TreeNode(5, TreeNode(3, TreeNode(1)))
        self.assertEqual(self.s.closestValue(root, 2.0), 1)

    def test_right_only_tree(self):
        root = TreeNode(1, None, TreeNode(3, None, TreeNode(5)))
        self.assertEqual(self.s.closestValue(root, 4.0), 3)

    def test_large_target(self):
        root = _build([4, 2, 5, 1, 3])
        self.assertEqual(self.s.closestValue(root, 100.0), 5)

    def test_negative_target(self):
        root = _build([4, 2, 5, 1, 3])
        self.assertEqual(self.s.closestValue(root, -100.0), 1)


if __name__ == "__main__":
    unittest.main()
