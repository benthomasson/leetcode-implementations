"""Tests for Delete N Nodes After M Nodes of a Linked List."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

import unittest
from solution import deleteNodes, list_to_linked, linked_to_list


class TestDeleteNodes(unittest.TestCase):
    def check(self, vals, m, n, expected):
        head = list_to_linked(vals)
        result = deleteNodes(head, m, n)
        self.assertEqual(linked_to_list(result), expected)

    # --- Problem examples ---
    def test_example1(self):
        self.check([1,2,3,4,5,6,7,8,9,10,11,12,13], 2, 3, [1,2,6,7,11,12])

    def test_example2(self):
        self.check([1,2,3,4,5,6,7,8,9,10,11], 1, 3, [1,5,9])

    # --- Edge cases ---
    def test_single_node(self):
        self.check([1], 1, 1, [1])

    def test_m_larger_than_list(self):
        self.check([1,2,3], 5, 2, [1,2,3])

    def test_n_larger_than_remaining(self):
        self.check([1,2,3,4,5], 2, 10, [1,2])

    def test_alternating_m1_n1(self):
        self.check([1,2,3,4,5,6], 1, 1, [1,3,5])

    def test_keep_all_m_equals_len(self):
        self.check([1,2,3], 3, 1, [1,2,3])

    def test_delete_all_but_first(self):
        self.check([1,2,3,4,5], 1, 100, [1])

    def test_two_nodes_m1_n1(self):
        self.check([1,2], 1, 1, [1])

    def test_exact_multiple(self):
        # 9 nodes, m=3 n=3: keep 1,2,3 skip 4,5,6 keep 7,8,9
        self.check([1,2,3,4,5,6,7,8,9], 3, 3, [1,2,3,7,8,9])


if __name__ == "__main__":
    unittest.main()
