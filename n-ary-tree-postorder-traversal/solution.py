"""N-ary Tree Postorder Traversal."""
from typing import List, Optional


class Node:
    def __init__(self, val: int = 0, children: Optional[List["Node"]] = None):
        self.val = val
        self.children = children if children is not None else []


def postorder(root: Optional[Node]) -> List[int]:
    """Return postorder traversal of an n-ary tree.

    Args:
        root: Root node of the n-ary tree.

    Returns:
        List of node values in postorder.
    """
    if not root:
        return []
    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.val)
        stack.extend(node.children)
    return result[::-1]


# --- Tests ---
import unittest


class TestPostorder(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(postorder(None), [])

    def test_single(self):
        self.assertEqual(postorder(Node(1)), [1])

    def test_example1(self):
        # [1,null,3,2,4,null,5,6]
        n5, n6 = Node(5), Node(6)
        n3 = Node(3, [n5, n6])
        n2, n4 = Node(2), Node(4)
        root = Node(1, [n3, n2, n4])
        self.assertEqual(postorder(root), [5, 6, 3, 2, 4, 1])

    def test_example2(self):
        # [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
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
        self.assertEqual(postorder(root), [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1])

    def test_deep_chain(self):
        # Linear chain: 1 -> 2 -> 3
        n3 = Node(3)
        n2 = Node(2, [n3])
        root = Node(1, [n2])
        self.assertEqual(postorder(root), [3, 2, 1])

    def test_wide_tree(self):
        # Root with many children
        children = [Node(i) for i in range(2, 7)]
        root = Node(1, children)
        self.assertEqual(postorder(root), [2, 3, 4, 5, 6, 1])


if __name__ == "__main__":
    unittest.main()
