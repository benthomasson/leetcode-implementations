"""Find Mode in Binary Search Tree."""
from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


def findMode(root: Optional[TreeNode]) -> List[int]:
    """Find all modes in a BST using in-order traversal.

    Args:
        root: Root of a binary search tree (may contain duplicates).

    Returns:
        List of the most frequently occurring values.
    """
    modes: list[int] = []
    max_count = 0
    cur_count = 0
    prev: Optional[int] = None

    def inorder(node: Optional[TreeNode]) -> None:
        nonlocal modes, max_count, cur_count, prev
        if not node:
            return
        inorder(node.left)
        cur_count = cur_count + 1 if prev == node.val else 1
        prev = node.val
        if cur_count > max_count:
            max_count = cur_count
            modes = [node.val]
        elif cur_count == max_count:
            modes.append(node.val)
        inorder(node.right)

    inorder(root)
    return modes


# --- Tests ---
import unittest


class TestFindMode(unittest.TestCase):
    def test_example1(self):
        #     1
        #      \
        #       2
        #      /
        #     2
        root = TreeNode(1, None, TreeNode(2, TreeNode(2)))
        self.assertEqual(findMode(root), [2])

    def test_example2(self):
        self.assertEqual(findMode(TreeNode(0)), [0])

    def test_all_same(self):
        root = TreeNode(5, TreeNode(5), TreeNode(5))
        self.assertEqual(findMode(root), [5])

    def test_multiple_modes(self):
        #     1
        #    / \
        #   1   2
        #        \
        #         2
        root = TreeNode(1, TreeNode(1), TreeNode(2, None, TreeNode(2)))
        self.assertCountEqual(findMode(root), [1, 2])

    def test_all_unique(self):
        #     2
        #    / \
        #   1   3
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertCountEqual(findMode(root), [1, 2, 3])

    def test_left_skewed(self):
        root = TreeNode(3, TreeNode(2, TreeNode(1)))
        self.assertCountEqual(findMode(root), [1, 2, 3])

    def test_right_skewed(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(2)))
        self.assertEqual(findMode(root), [2])

    def test_negative_values(self):
        root = TreeNode(-1, TreeNode(-1), TreeNode(0))
        self.assertEqual(findMode(root), [-1])


if __name__ == "__main__":
    unittest.main()
