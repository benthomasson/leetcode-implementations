"""Binary Tree Preorder Traversal - LeetCode"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Return preorder traversal of a binary tree iteratively.

        Args:
            root: Root node of the binary tree.

        Returns:
            List of node values in preorder (root, left, right).
        """
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result


# --- Tests ---
import unittest


class TestPreorderTraversal(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        # [1,null,2,3] -> [1,2,3]
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        self.assertEqual(self.sol.preorderTraversal(root), [1, 2, 3])

    def test_empty(self):
        self.assertEqual(self.sol.preorderTraversal(None), [])

    def test_single(self):
        self.assertEqual(self.sol.preorderTraversal(TreeNode(1)), [1])

    def test_left_chain(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(self.sol.preorderTraversal(root), [1, 2, 3])

    def test_right_chain(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(self.sol.preorderTraversal(root), [1, 2, 3])

    def test_balanced(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertEqual(self.sol.preorderTraversal(root), [1, 2, 4, 5, 3])

    def test_negative_values(self):
        root = TreeNode(-1, TreeNode(-2), TreeNode(-3))
        self.assertEqual(self.sol.preorderTraversal(root), [-1, -2, -3])


if __name__ == "__main__":
    unittest.main()
