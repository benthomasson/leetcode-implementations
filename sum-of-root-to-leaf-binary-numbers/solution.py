"""Sum of Root To Leaf Binary Numbers (LeetCode 1022).

Given a binary tree where each node has value 0 or 1, compute the sum of
all root-to-leaf paths interpreted as binary numbers (MSB at root).
"""

from __future__ import annotations

from collections import deque
from typing import Optional


class TreeNode:
    """Binary tree node with value 0 or 1."""

    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from a level-order list.

    Args:
        values: Level-order traversal where None represents missing nodes.
            Example: [1, 0, 1, 0, 1, 0, 1]

    Returns:
        Root of the constructed tree, or None if the list is empty.
    """
    if not values:
        return None

    root = TreeNode(values[0])
    queue: deque[TreeNode] = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


class Solution:
    """Solution for Sum of Root To Leaf Binary Numbers."""

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """Return the sum of all root-to-leaf binary numbers.

        Each root-to-leaf path is interpreted as a binary number with the
        most significant bit at the root. The function returns the sum of
        all such numbers across every leaf.

        Args:
            root: Root of the binary tree. Each node's val is 0 or 1.

        Returns:
            Sum of binary numbers represented by all root-to-leaf paths.

        Examples:
            >>> s = Solution()
            >>> s.sumRootToLeaf(build_tree([1, 0, 1, 0, 1, 0, 1]))
            22
            >>> s.sumRootToLeaf(build_tree([0]))
            0
        """
        if root is None:
            return 0

        def dfs(node: TreeNode, current: int) -> int:
            current = (current << 1) | node.val

            if node.left is None and node.right is None:
                return current

            total = 0
            if node.left is not None:
                total += dfs(node.left, current)
            if node.right is not None:
                total += dfs(node.right, current)
            return total

        return dfs(root, 0)
