"""Maximum Depth of N-ary Tree."""

from typing import List, Optional


class Node:
    """N-ary tree node."""

    def __init__(self, val: int = 0, children: Optional[List["Node"]] = None):
        self.val = val
        self.children = children if children is not None else []


def max_depth(root: Optional[Node]) -> int:
    """Find the maximum depth of an n-ary tree.

    Args:
        root: Root node of the n-ary tree, or None for empty tree.

    Returns:
        Maximum depth (number of nodes on longest root-to-leaf path).
    """
    if root is None:
        return 0
    if not root.children:
        return 1
    return 1 + max(max_depth(child) for child in root.children)


# --- Tests ---
import unittest


class TestMaxDepth(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(max_depth(None), 0)

    def test_single_node(self):
        self.assertEqual(max_depth(Node(1)), 1)

    def test_example1(self):
        # [1,null,3,2,4,null,5,6] -> depth 3
        n5 = Node(5)
        n6 = Node(6)
        n3 = Node(3, [n5, n6])
        n2 = Node(2)
        n4 = Node(4)
        root = Node(1, [n3, n2, n4])
        self.assertEqual(max_depth(root), 3)

    def test_example2(self):
        # depth 5
        n14 = Node(14)
        n11 = Node(11, [n14])
        n12 = Node(12)
        n13 = Node(13)
        n6 = Node(6)
        n7 = Node(7, [n11])
        n8 = Node(8, [n12])
        n9 = Node(9, [n13])
        n10 = Node(10)
        n2 = Node(2)
        n3 = Node(3, [n6, n7])
        n4 = Node(4, [n8])
        n5 = Node(5, [n9, n10])
        root = Node(1, [n2, n3, n4, n5])
        self.assertEqual(max_depth(root), 5)

    def test_linear_chain(self):
        # 1 -> 2 -> 3 -> 4, depth 4
        n4 = Node(4)
        n3 = Node(3, [n4])
        n2 = Node(2, [n3])
        root = Node(1, [n2])
        self.assertEqual(max_depth(root), 4)

    def test_wide_tree(self):
        # Root with 5 children, no grandchildren -> depth 2
        root = Node(1, [Node(i) for i in range(2, 7)])
        self.assertEqual(max_depth(root), 2)


if __name__ == "__main__":
    unittest.main()
