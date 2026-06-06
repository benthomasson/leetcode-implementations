"""Tests for sorted_array_to_bst."""

from __future__ import annotations
import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import TreeNode, sorted_array_to_bst


# -- helpers --

def height(node: TreeNode | None) -> int:
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))


def is_balanced(node: TreeNode | None) -> bool:
    if not node:
        return True
    return (abs(height(node.left) - height(node.right)) <= 1
            and is_balanced(node.left) and is_balanced(node.right))


def is_bst(node: TreeNode | None, lo=float('-inf'), hi=float('inf')) -> bool:
    if not node:
        return True
    if not (lo < node.val < hi):
        return False
    return is_bst(node.left, lo, node.val) and is_bst(node.right, node.val, hi)


def inorder(node: TreeNode | None) -> list[int]:
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


class TestSortedArrayToBST(unittest.TestCase):

    def _check(self, nums: list[int]) -> None:
        root = sorted_array_to_bst(nums)
        self.assertTrue(is_bst(root), "Not a valid BST")
        self.assertTrue(is_balanced(root), "Not height-balanced")
        self.assertEqual(inorder(root), nums, "Inorder traversal doesn't match input")

    # -- problem examples --

    def test_example1(self):
        self._check([-10, -3, 0, 5, 9])

    def test_example2(self):
        self._check([1, 3])

    # -- edge cases --

    def test_single_element(self):
        root = sorted_array_to_bst([0])
        self.assertEqual(root.val, 0)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_two_elements(self):
        self._check([1, 2])

    def test_odd_length(self):
        self._check([1, 2, 3, 4, 5])

    def test_even_length(self):
        self._check([1, 2, 3, 4])

    def test_all_negatives(self):
        self._check([-100, -50, -10, -1])

    def test_large_input(self):
        self._check(list(range(10000)))


if __name__ == "__main__":
    unittest.main()
