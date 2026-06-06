import unittest
from solution import TreeNode, find_second_minimum_value


class TestFindSecondMinimumValue(unittest.TestCase):

    def test_example1(self):
        #     2
        #    / \
        #   2   5
        #      / \
        #     5   7
        root = TreeNode(2, TreeNode(2), TreeNode(5, TreeNode(5), TreeNode(7)))
        self.assertEqual(find_second_minimum_value(root), 5)

    def test_example2_all_same(self):
        root = TreeNode(2, TreeNode(2), TreeNode(2))
        self.assertEqual(find_second_minimum_value(root), -1)

    def test_single_node(self):
        self.assertEqual(find_second_minimum_value(TreeNode(1)), -1)

    def test_second_min_in_left(self):
        #     1
        #    / \
        #   1   3
        #  / \
        # 1   2
        root = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(2)), TreeNode(3))
        self.assertEqual(find_second_minimum_value(root), 2)

    def test_second_min_deep(self):
        #       1
        #      / \
        #     1   1
        #    / \
        #   1   1
        #  / \
        # 1   5
        root = TreeNode(1,
            TreeNode(1,
                TreeNode(1, TreeNode(1), TreeNode(5)),
                TreeNode(1)),
            TreeNode(1))
        self.assertEqual(find_second_minimum_value(root), 5)

    def test_large_values(self):
        big = 2**31 - 1
        root = TreeNode(1, TreeNode(1), TreeNode(big))
        self.assertEqual(find_second_minimum_value(root), big)

    def test_none_root(self):
        self.assertEqual(find_second_minimum_value(None), -1)

    def test_pick_smaller_candidate(self):
        #     1
        #    / \
        #   1   3
        #  / \
        # 1   2
        # Should pick 2 over 3
        root = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(2)), TreeNode(3))
        self.assertEqual(find_second_minimum_value(root), 2)


if __name__ == "__main__":
    unittest.main()
