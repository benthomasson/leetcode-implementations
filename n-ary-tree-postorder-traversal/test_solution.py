"""Tests for N-ary Tree Postorder Traversal."""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import Node, postorder


class TestPostorder(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(postorder(None), [])

    def test_single_node(self):
        self.assertEqual(postorder(Node(1)), [1])

    def test_example1(self):
        # [1,null,3,2,4,null,5,6] -> [5,6,3,2,4,1]
        root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
        self.assertEqual(postorder(root), [5, 6, 3, 2, 4, 1])

    def test_example2(self):
        # [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
        root = Node(1, [
            Node(2),
            Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]),
            Node(4, [Node(8, [Node(12)])]),
            Node(5, [Node(9, [Node(13)]), Node(10)]),
        ])
        self.assertEqual(postorder(root), [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1])

    def test_deep_chain(self):
        # 1 -> 2 -> 3 -> 4
        root = Node(1, [Node(2, [Node(3, [Node(4)])])])
        self.assertEqual(postorder(root), [4, 3, 2, 1])

    def test_wide_tree(self):
        root = Node(0, [Node(i) for i in range(1, 6)])
        self.assertEqual(postorder(root), [1, 2, 3, 4, 5, 0])

    def test_node_val_zero(self):
        self.assertEqual(postorder(Node(0)), [0])

    def test_duplicate_values(self):
        root = Node(1, [Node(1), Node(1)])
        self.assertEqual(postorder(root), [1, 1, 1])


if __name__ == "__main__":
    unittest.main()
