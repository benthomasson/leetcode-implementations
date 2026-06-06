"""Tests for LeetCode 897: Increasing Order Search Tree."""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import Solution, TreeNode, build_tree, tree_to_list


class TestIncreasingBST(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def _collect_vals(self, root):
        """Collect values from right-skewed tree."""
        vals = []
        while root:
            self.assertIsNone(root.left, f"Node {root.val} has a left child")
            vals.append(root.val)
            root = root.right
        return vals

    # --- Problem examples ---

    def test_example1(self):
        root = build_tree([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])
        result = self.sol.increasingBST(root)
        self.assertEqual(self._collect_vals(result), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_example2(self):
        root = build_tree([5, 1, 7])
        result = self.sol.increasingBST(root)
        self.assertEqual(self._collect_vals(result), [1, 5, 7])

    # --- Edge cases ---

    def test_single_node(self):
        root = TreeNode(42)
        result = self.sol.increasingBST(root)
        self.assertEqual(self._collect_vals(result), [42])

    def test_two_nodes_left(self):
        root = TreeNode(2, TreeNode(1))
        result = self.sol.increasingBST(root)
        self.assertEqual(self._collect_vals(result), [1, 2])

    def test_two_nodes_right(self):
        root = TreeNode(1, None, TreeNode(2))
        result = self.sol.increasingBST(root)
        self.assertEqual(self._collect_vals(result), [1, 2])

    def test_left_chain(self):
        root = build_tree([3, 2, None, 1])
        result = self.sol.increasingBST(root)
        self.assertEqual(self._collect_vals(result), [1, 2, 3])

    def test_right_chain_unchanged(self):
        root = build_tree([1, None, 2, None, 3])
        result = self.sol.increasingBST(root)
        self.assertEqual(self._collect_vals(result), [1, 2, 3])

    def test_duplicate_values(self):
        # BST with equal values going right
        root = TreeNode(1, None, TreeNode(1, None, TreeNode(1)))
        result = self.sol.increasingBST(root)
        self.assertEqual(self._collect_vals(result), [1, 1, 1])

    def test_val_zero(self):
        root = TreeNode(1, TreeNode(0))
        result = self.sol.increasingBST(root)
        self.assertEqual(self._collect_vals(result), [0, 1])


if __name__ == "__main__":
    unittest.main()
