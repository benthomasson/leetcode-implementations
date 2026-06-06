import unittest
from solution import TreeNode, is_same_tree


class TestIsSameTree(unittest.TestCase):
    def test_both_empty(self):
        self.assertTrue(is_same_tree(None, None))

    def test_identical_trees(self):
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertTrue(is_same_tree(p, q))

    def test_different_structure(self):
        p = TreeNode(1, TreeNode(2))
        q = TreeNode(1, None, TreeNode(2))
        self.assertFalse(is_same_tree(p, q))

    def test_different_values(self):
        p = TreeNode(1, TreeNode(2), TreeNode(1))
        q = TreeNode(1, TreeNode(1), TreeNode(2))
        self.assertFalse(is_same_tree(p, q))

    def test_one_empty(self):
        self.assertFalse(is_same_tree(TreeNode(1), None))
        self.assertFalse(is_same_tree(None, TreeNode(1)))

    def test_single_equal_nodes(self):
        self.assertTrue(is_same_tree(TreeNode(1), TreeNode(1)))

    def test_single_different_nodes(self):
        self.assertFalse(is_same_tree(TreeNode(1), TreeNode(2)))

    def test_negative_values(self):
        p = TreeNode(-1, TreeNode(-2))
        q = TreeNode(-1, TreeNode(-2))
        self.assertTrue(is_same_tree(p, q))

    def test_deep_tree(self):
        p = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        q = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        self.assertTrue(is_same_tree(p, q))

    def test_deep_tree_difference_at_leaf(self):
        p = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        q = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(5))))
        self.assertFalse(is_same_tree(p, q))


if __name__ == "__main__":
    unittest.main()
