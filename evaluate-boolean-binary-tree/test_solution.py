"""Tests for Evaluate Boolean Binary Tree solution."""
import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import TreeNode, evalTree, _build_tree


class TestEvalTree(unittest.TestCase):
    # --- LeetCode examples ---
    def test_example1(self):
        """[2,1,3,null,null,0,1] -> True (OR(1, AND(0,1)) = OR(T,F) = T)."""
        root = _build_tree([2, 1, 3, None, None, 0, 1])
        self.assertTrue(evalTree(root))

    def test_example2(self):
        """[0] -> False (single leaf 0)."""
        root = _build_tree([0])
        self.assertFalse(evalTree(root))

    # --- Single leaf nodes ---
    def test_single_true_leaf(self):
        self.assertTrue(evalTree(TreeNode(1)))

    def test_single_false_leaf(self):
        self.assertFalse(evalTree(TreeNode(0)))

    # --- OR truth table ---
    def test_or_ff(self):
        self.assertFalse(evalTree(TreeNode(2, TreeNode(0), TreeNode(0))))

    def test_or_ft(self):
        self.assertTrue(evalTree(TreeNode(2, TreeNode(0), TreeNode(1))))

    def test_or_tt(self):
        self.assertTrue(evalTree(TreeNode(2, TreeNode(1), TreeNode(1))))

    # --- AND truth table ---
    def test_and_tt(self):
        self.assertTrue(evalTree(TreeNode(3, TreeNode(1), TreeNode(1))))

    def test_and_tf(self):
        self.assertFalse(evalTree(TreeNode(3, TreeNode(1), TreeNode(0))))

    def test_and_ff(self):
        self.assertFalse(evalTree(TreeNode(3, TreeNode(0), TreeNode(0))))

    # --- Deeper nesting ---
    def test_nested_three_levels(self):
        # OR(AND(1,0), OR(1,0)) = OR(False, True) = True
        root = TreeNode(2,
            TreeNode(3, TreeNode(1), TreeNode(0)),
            TreeNode(2, TreeNode(1), TreeNode(0)))
        self.assertTrue(evalTree(root))

    def test_all_false_deep(self):
        # AND(OR(0,0), AND(0,0)) = AND(False, False) = False
        root = TreeNode(3,
            TreeNode(2, TreeNode(0), TreeNode(0)),
            TreeNode(3, TreeNode(0), TreeNode(0)))
        self.assertFalse(evalTree(root))


if __name__ == "__main__":
    unittest.main()
