"""Tests for LeetCode 2236: Root Equals Sum of Children."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution, TreeNode


def make_tree(root_val: int, left_val: int, right_val: int) -> TreeNode:
    return TreeNode(root_val, TreeNode(left_val), TreeNode(right_val))


class TestCheckTree(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- LeetCode examples ---
    def test_example1_true(self):
        self.assertTrue(self.sol.checkTree(make_tree(10, 4, 6)))

    def test_example2_false(self):
        self.assertFalse(self.sol.checkTree(make_tree(5, 3, 1)))

    # --- Edge cases ---
    def test_all_zeros(self):
        self.assertTrue(self.sol.checkTree(make_tree(0, 0, 0)))

    def test_negative_children_sum(self):
        self.assertTrue(self.sol.checkTree(make_tree(-5, -3, -2)))

    def test_mixed_signs(self):
        self.assertTrue(self.sol.checkTree(make_tree(1, -1, 2)))

    def test_boundary_min_max(self):
        self.assertTrue(self.sol.checkTree(make_tree(0, -100, 100)))

    def test_false_with_negatives(self):
        self.assertFalse(self.sol.checkTree(make_tree(0, -1, -2)))

    def test_off_by_one(self):
        self.assertFalse(self.sol.checkTree(make_tree(11, 4, 6)))


if __name__ == "__main__":
    unittest.main()
