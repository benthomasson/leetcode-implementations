"""Average of Levels in Binary Tree."""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """Return the average value of nodes on each level of a binary tree.

        Args:
            root: Root node of the binary tree.

        Returns:
            List of average values per level.
        """
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            level_sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_sum / level_size)
        return result


# --- Tests ---
import unittest


class TestAverageOfLevels(unittest.TestCase):
    def _solve(self, root):
        return Solution().averageOfLevels(root)

    def test_example1(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(self._solve(root), [3.0, 14.5, 11.0])

    def test_example2(self):
        root = TreeNode(3, TreeNode(9, TreeNode(15), TreeNode(7)), TreeNode(20))
        self.assertEqual(self._solve(root), [3.0, 14.5, 11.0])

    def test_single_node(self):
        self.assertEqual(self._solve(TreeNode(42)), [42.0])

    def test_left_skewed(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(self._solve(root), [1.0, 2.0, 3.0])

    def test_large_negative_values(self):
        big = -(2**31)
        root = TreeNode(big, TreeNode(big), TreeNode(big))
        self.assertAlmostEqual(self._solve(root)[0], float(big))
        self.assertAlmostEqual(self._solve(root)[1], float(big))

    def test_all_same_values(self):
        root = TreeNode(5, TreeNode(5), TreeNode(5))
        self.assertEqual(self._solve(root), [5.0, 5.0])


if __name__ == "__main__":
    unittest.main()
