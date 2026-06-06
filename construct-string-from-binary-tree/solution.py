"""Construct String from Binary Tree."""
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


def tree2str(root: Optional[TreeNode]) -> str:
    """Construct string from binary tree using preorder traversal.

    Args:
        root: Root node of the binary tree.

    Returns:
        String representation with parentheses, omitting unnecessary empty pairs.
    """
    if not root:
        return ""
    result = str(root.val)
    if root.left or root.right:
        result += f"({tree2str(root.left)})"
    if root.right:
        result += f"({tree2str(root.right)})"
    return result


# --- Tests ---
import unittest


class TestTree2Str(unittest.TestCase):
    def test_example1(self):
        #     1
        #    / \
        #   2   3
        #  /
        # 4
        root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        self.assertEqual(tree2str(root), "1(2(4))(3)")

    def test_example2(self):
        #     1
        #    / \
        #   2   3
        #    \
        #     4
        root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
        self.assertEqual(tree2str(root), "1(2()(4))(3)")

    def test_single_node(self):
        self.assertEqual(tree2str(TreeNode(1)), "1")

    def test_none(self):
        self.assertEqual(tree2str(None), "")

    def test_left_only(self):
        root = TreeNode(1, TreeNode(2))
        self.assertEqual(tree2str(root), "1(2)")

    def test_right_only(self):
        root = TreeNode(1, None, TreeNode(3))
        self.assertEqual(tree2str(root), "1()(3)")

    def test_negative_values(self):
        root = TreeNode(-1, TreeNode(-2), TreeNode(-3))
        self.assertEqual(tree2str(root), "-1(-2)(-3)")

    def test_both_children_leaf(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(tree2str(root), "1(2)(3)")


if __name__ == "__main__":
    unittest.main()
