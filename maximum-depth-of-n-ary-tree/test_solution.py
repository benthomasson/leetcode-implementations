"""Tests for Maximum Depth of N-ary Tree."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Node, max_depth


class TestMaxDepth(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(max_depth(None), 0)

    def test_single_node(self):
        self.assertEqual(max_depth(Node(1)), 1)

    def test_example1(self):
        # [1,null,3,2,4,null,5,6] -> depth 3
        n5, n6 = Node(5), Node(6)
        n3 = Node(3, [n5, n6])
        root = Node(1, [n3, Node(2), Node(4)])
        self.assertEqual(max_depth(root), 3)

    def test_example2(self):
        # depth 5
        n14 = Node(14)
        n11 = Node(11, [n14])
        n7 = Node(7, [n11])
        n3 = Node(3, [Node(6), n7])
        n4 = Node(4, [Node(8, [Node(12)])])
        n5 = Node(5, [Node(9, [Node(13)]), Node(10)])
        root = Node(1, [Node(2), n3, n4, n5])
        self.assertEqual(max_depth(root), 5)

    def test_linear_chain(self):
        # 1 -> 2 -> 3 -> 4, depth 4
        root = Node(1, [Node(2, [Node(3, [Node(4)])])])
        self.assertEqual(max_depth(root), 4)

    def test_wide_tree(self):
        # Root with 5 leaf children -> depth 2
        root = Node(1, [Node(i) for i in range(2, 7)])
        self.assertEqual(max_depth(root), 2)

    def test_unbalanced(self):
        # Left branch deeper than right
        root = Node(1, [Node(2, [Node(3)]), Node(4)])
        self.assertEqual(max_depth(root), 3)

    def test_node_with_empty_children_list(self):
        root = Node(1, [])
        self.assertEqual(max_depth(root), 1)


if __name__ == "__main__":
    unittest.main()
