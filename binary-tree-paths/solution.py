"""Binary Tree Paths - LeetCode Solution."""

from typing import List, Optional
import unittest


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    """Return all root-to-leaf paths in a binary tree.

    Args:
        root: Root node of the binary tree.

    Returns:
        List of path strings formatted as "1->2->3".
    """
    if not root:
        return []
    results: list[str] = []

    def dfs(node: TreeNode, path: str) -> None:
        if not node.left and not node.right:
            results.append(path)
            return
        if node.left:
            dfs(node.left, path + "->" + str(node.left.val))
        if node.right:
            dfs(node.right, path + "->" + str(node.right.val))

    dfs(root, str(root.val))
    return results


class TestBinaryTreePaths(unittest.TestCase):
    def test_example1(self):
        #     1
        #    / \
        #   2   3
        #    \
        #     5
        root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
        self.assertCountEqual(binary_tree_paths(root), ["1->2->5", "1->3"])

    def test_example2_single_node(self):
        self.assertEqual(binary_tree_paths(TreeNode(1)), ["1"])

    def test_left_skewed(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(binary_tree_paths(root), ["1->2->3"])

    def test_right_skewed(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(binary_tree_paths(root), ["1->2->3"])

    def test_negative_values(self):
        root = TreeNode(-1, TreeNode(-2), TreeNode(-3))
        self.assertCountEqual(binary_tree_paths(root), ["-1->-2", "-1->-3"])

    def test_balanced(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        self.assertCountEqual(
            binary_tree_paths(root),
            ["1->2->4", "1->2->5", "1->3->6", "1->3->7"],
        )

    def test_none_root(self):
        self.assertEqual(binary_tree_paths(None), [])


if __name__ == "__main__":
    unittest.main()
