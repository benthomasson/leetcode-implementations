"""Tests for find-if-path-exists-in-graph solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import mem_sticks_crash


class TestMemSticksCrash(unittest.TestCase):
    # --- Problem examples ---
    def test_example1_cycle_graph(self):
        self.assertTrue(mem_sticks_crash(3, [[0, 1], [1, 2], [2, 0]], 0, 2))

    def test_example2_disconnected(self):
        self.assertFalse(mem_sticks_crash(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))

    # --- Edge cases ---
    def test_source_equals_destination(self):
        self.assertTrue(mem_sticks_crash(1, [], 0, 0))

    def test_source_equals_destination_with_edges(self):
        self.assertTrue(mem_sticks_crash(3, [[0, 1], [1, 2]], 1, 1))

    def test_no_edges_different_nodes(self):
        self.assertFalse(mem_sticks_crash(3, [], 0, 2))

    def test_single_edge_connected(self):
        self.assertTrue(mem_sticks_crash(2, [[0, 1]], 0, 1))

    def test_single_edge_reversed_query(self):
        self.assertTrue(mem_sticks_crash(2, [[0, 1]], 1, 0))

    def test_long_chain(self):
        edges = [[i, i + 1] for i in range(99)]
        self.assertTrue(mem_sticks_crash(100, edges, 0, 99))

    def test_disconnected_components(self):
        self.assertFalse(mem_sticks_crash(4, [[0, 1], [2, 3]], 0, 3))

    def test_large_connected_star(self):
        edges = [[0, i] for i in range(1, 1000)]
        self.assertTrue(mem_sticks_crash(1000, edges, 1, 999))


if __name__ == "__main__":
    unittest.main()
