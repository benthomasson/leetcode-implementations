"""Tests for Range Sum of BST solution."""
import unittest
from solution import TreeNode, range_sum_bst


def _build_tree(values: list) -> TreeNode | None:
    """Build a BST from level-order list (None for missing nodes)."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class TestRangeSumBST(unittest.TestCase):
    """Tests for range_sum_bst."""

    def test_example1(self):
        root = _build_tree([10, 5, 15, 3, 7, None, 18])
        self.assertEqual(range_sum_bst(root, 7, 15), 32)

    def test_example2(self):
        root = _build_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
        self.assertEqual(range_sum_bst(root, 6, 10), 23)

    def test_empty_tree(self):
        self.assertEqual(range_sum_bst(None, 1, 10), 0)

    def test_single_node_in_range(self):
        self.assertEqual(range_sum_bst(TreeNode(5), 1, 10), 5)

    def test_single_node_out_of_range(self):
        self.assertEqual(range_sum_bst(TreeNode(5), 6, 10), 0)

    def test_single_node_equal_low(self):
        self.assertEqual(range_sum_bst(TreeNode(5), 5, 10), 5)

    def test_single_node_equal_high(self):
        self.assertEqual(range_sum_bst(TreeNode(5), 1, 5), 5)

    def test_all_nodes_in_range(self):
        root = _build_tree([5, 3, 7])
        self.assertEqual(range_sum_bst(root, 1, 100), 15)

    def test_no_nodes_in_range(self):
        root = _build_tree([5, 3, 7])
        self.assertEqual(range_sum_bst(root, 20, 30), 0)

    def test_right_skewed_tree(self):
        root = TreeNode(1, None, TreeNode(3, None, TreeNode(5)))
        self.assertEqual(range_sum_bst(root, 2, 4), 3)


if __name__ == "__main__":
    unittest.main()
