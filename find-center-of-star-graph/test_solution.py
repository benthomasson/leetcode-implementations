"""Tests for Find Center of Star Graph solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestFindCenter(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(self.sol.find_center([[1, 2], [2, 3], [4, 2]]), 2)

    def test_example2(self):
        self.assertEqual(self.sol.find_center([[1, 2], [5, 1], [1, 3], [1, 4]]), 1)

    # --- Edge cases ---
    def test_minimal_3_nodes(self):
        self.assertEqual(self.sol.find_center([[1, 2], [2, 3]]), 2)

    def test_center_at_pos_0_0(self):
        """Center is edges[0][0] and edges[1][0]."""
        self.assertEqual(self.sol.find_center([[5, 1], [5, 2], [5, 3]]), 5)

    def test_center_at_pos_0_1(self):
        """Center is edges[0][1] and edges[1][1]."""
        self.assertEqual(self.sol.find_center([[1, 5], [2, 5], [3, 5]]), 5)

    def test_center_at_mixed_positions(self):
        """Center is edges[0][1] and edges[1][0]."""
        self.assertEqual(self.sol.find_center([[3, 4], [4, 1], [4, 2]]), 4)

    def test_large_node_labels(self):
        self.assertEqual(self.sol.find_center([[100000, 99999], [100000, 1]]), 100000)

    def test_many_edges(self):
        """Star with center=1 and 99 other nodes."""
        edges = [[1, i] for i in range(2, 101)]
        self.assertEqual(self.sol.find_center(edges), 1)


if __name__ == "__main__":
    unittest.main()
