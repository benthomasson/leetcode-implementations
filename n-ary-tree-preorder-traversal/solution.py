"""N-ary Tree Preorder Traversal - LeetCode Solution."""

from typing import List, Optional


class Node:
    """N-ary tree node."""

    def __init__(self, val: int = 0, children: Optional[List["Node"]] = None):
        self.val = val
        self.children = children if children is not None else []


def preorder(root: Optional[Node]) -> List[int]:
    """Return the preorder traversal of an n-ary tree iteratively.

    Args:
        root: Root node of the n-ary tree.

    Returns:
        List of node values in preorder.
    """
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        # Push children in reverse so leftmost is processed first
        stack.extend(reversed(node.children))
    return result
