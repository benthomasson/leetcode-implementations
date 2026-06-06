"""Convert Sorted Array to Binary Search Tree."""

from __future__ import annotations
import unittest


class TreeNode:
    """Binary tree node."""

    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(nums: list[int]) -> TreeNode | None:
    """Convert a sorted array to a height-balanced BST.

    Args:
        nums: Integer array sorted in ascending order.

    Returns:
        Root of the height-balanced BST, or None if empty.
    """

    def helper(left: int, right: int) -> TreeNode | None:
        if left > right:
            return None
        mid = (left + right) // 2
        return TreeNode(nums[mid], helper(left, mid - 1), helper(mid + 1, right))

    return helper(0, len(nums) - 1)


# --- Tests ---

class TestSortedArrayToBST(unittest.TestCase):

    def _is_bst(self, node: TreeNode | None, lo: float = float('-inf'), hi: float = float('inf')) -> bool:
        if not node:
            return True
        if not (lo < node.val < hi):
            return False
        return self._is_bst(node.left, lo, node.val) and self._is_bst(node.right, node.val, hi)

    def _height(self, node: TreeNode | None) -> int:
        if not node:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def _is_balanced(self, node: TreeNode | None) -> bool:
        if not node:
            return True
        return (abs(self._height(node.left) - self._height(node.right)) <= 1
                and self._is_balanced(node.left) and self._is_balanced(node.right))

    def _inorder(self, node: TreeNode | None) -> list[int]:
        if not node:
            return []
        return self._inorder(node.left) + [node.val] + self._inorder(node.right)

    def _assert_valid(self, nums: list[int]) -> None:
        root = sorted_array_to_bst(nums)
        self.assertTrue(self._is_bst(root))
        self.assertTrue(self._is_balanced(root))
        self.assertEqual(self._inorder(root), nums)

    def test_example1(self):
        self._assert_valid([-10, -3, 0, 5, 9])

    def test_example2(self):
        self._assert_valid([1, 3])

    def test_single(self):
        root = sorted_array_to_bst([42])
        self.assertEqual(root.val, 42)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_three_elements(self):
        self._assert_valid([1, 2, 3])

    def test_even_length(self):
        self._assert_valid([1, 2, 3, 4])

    def test_negatives(self):
        self._assert_valid([-5, -4, -3, -2, -1])

    def test_large(self):
        self._assert_valid(list(range(10000)))


if __name__ == "__main__":
    unittest.main()
