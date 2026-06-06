"""Tests for Subtree of Another Tree - LeetCode 572."""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import Solution, TreeNode, _build


class TestSubtreeOfAnotherTree(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- Problem examples ---
    def test_example1_subtree_exists(self):
        root = _build([3, 4, 5, 1, 2])
        sub = _build([4, 1, 2])
        self.assertTrue(self.sol.isSubtree(root, sub))

    def test_example2_extra_child_makes_it_not_subtree(self):
        root = _build([3, 4, 5, 1, 2, None, None, None, None, 0])
        sub = _build([4, 1, 2])
        self.assertFalse(self.sol.isSubtree(root, sub))

    # --- Edge cases ---
    def test_both_none(self):
        self.assertTrue(self.sol.isSubtree(None, None))

    def test_root_none_sub_exists(self):
        self.assertFalse(self.sol.isSubtree(None, TreeNode(1)))

    def test_sub_none(self):
        self.assertTrue(self.sol.isSubtree(TreeNode(1), None))

    def test_single_node_match(self):
        self.assertTrue(self.sol.isSubtree(TreeNode(5), TreeNode(5)))

    def test_single_node_no_match(self):
        self.assertFalse(self.sol.isSubtree(TreeNode(5), TreeNode(3)))

    # --- Structural cases ---
    def test_identical_trees(self):
        root = _build([1, 2, 3])
        sub = _build([1, 2, 3])
        self.assertTrue(self.sol.isSubtree(root, sub))

    def test_subtree_on_right_side(self):
        root = _build([3, 4, 5, 1, 2])
        sub = _build([5])
        self.assertTrue(self.sol.isSubtree(root, sub))

    def test_same_values_different_structure(self):
        # sub has only left child, root node 1 has both children
        root = _build([1, 2, 3])
        sub = _build([1, 2])
        self.assertFalse(self.sol.isSubtree(root, sub))


if __name__ == "__main__":
    unittest.main()
