"""Tests for N-ary Tree Preorder Traversal."""

import unittest
from solution import Node, preorder


class TestPreorder(unittest.TestCase):

    def test_empty_tree(self):
        self.assertEqual(preorder(None), [])

    def test_single_node(self):
        self.assertEqual(preorder(Node(1)), [1])

    def test_example1(self):
        # root = [1,null,3,2,4,null,5,6]
        root = Node(1, [
            Node(3, [Node(5), Node(6)]),
            Node(2),
            Node(4),
        ])
        self.assertEqual(preorder(root), [1, 3, 5, 6, 2, 4])

    def test_example2(self):
        # root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
        root = Node(1, [
            Node(2),
            Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]),
            Node(4, [Node(8, [Node(12)])]),
            Node(5, [Node(9, [Node(13)]), Node(10)]),
        ])
        self.assertEqual(preorder(root), [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10])

    def test_deep_chain(self):
        # Linear chain: 1 -> 2 -> 3
        root = Node(1, [Node(2, [Node(3)])])
        self.assertEqual(preorder(root), [1, 2, 3])

    def test_wide_tree(self):
        # Root with many children, no grandchildren
        root = Node(0, [Node(i) for i in range(1, 6)])
        self.assertEqual(preorder(root), [0, 1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
