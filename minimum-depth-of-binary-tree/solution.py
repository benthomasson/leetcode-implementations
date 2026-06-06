"""Minimum Depth of Binary Tree."""

from __future__ import annotations
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """Find the minimum depth of a binary tree using BFS.

        Args:
            root: Root node of the binary tree.

        Returns:
            Number of nodes along the shortest path from root to nearest leaf.
        """
        if not root:
            return 0

        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return 0  # unreachable
