"""Binary Tree Inorder Traversal - Iterative stack-based solution."""

from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversalHelper(root: Optional[TreeNode]) -> list[int]:
    """Return the inorder traversal of a binary tree's node values.

    Args:
        root: Root node of the binary tree, or None for empty tree.

    Returns:
        List of node values in inorder (left, root, right) sequence.
    """
    result = []
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result


class TestInorderTraversal(unittest.TestCase):

    def test_example1(self):
        # [1, null, 2, 3] -> [1, 3, 2]
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        self.assertEqual(inorderTraversalHelper(root), [1, 3, 2])

    def test_empty(self):
        self.assertEqual(inorderTraversalHelper(None), [])

    def test_single(self):
        self.assertEqual(inorderTraversalHelper(TreeNode(1)), [1])

    def test_left_chain(self):
        root = TreeNode(3, TreeNode(2, TreeNode(1)))
        self.assertEqual(inorderTraversalHelper(root), [1, 2, 3])

    def test_right_chain(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(inorderTraversalHelper(root), [1, 2, 3])

    def test_balanced(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertEqual(inorderTraversalHelper(root), [1, 2, 3])

    def test_negative_values(self):
        root = TreeNode(0, TreeNode(-100), TreeNode(100))
        self.assertEqual(inorderTraversalHelper(root), [-100, 0, 100])


if __name__ == "__main__":
    unittest.main()
