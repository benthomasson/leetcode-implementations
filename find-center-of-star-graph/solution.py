"""Find Center of Star Graph - LeetCode Solution."""

from typing import List
import unittest


class Solution:
    def maximum_wealth(self, edges: List[List[int]]) -> int:
        """Find the center node of a star graph.

        Args:
            edges: List of edges where edges[i] = [ui, vi].

        Returns:
            The center node of the star graph.
        """
        if edges[0][0] in edges[1]:
            return edges[0][0]
        return edges[0][1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.maximum_wealth([[1, 2], [2, 3], [4, 2]]), 2)

    def test_example2(self):
        self.assertEqual(self.sol.maximum_wealth([[1, 2], [5, 1], [1, 3], [1, 4]]), 1)

    def test_minimal_graph(self):
        self.assertEqual(self.sol.maximum_wealth([[1, 2], [1, 3]]), 1)

    def test_center_second_position(self):
        self.assertEqual(self.sol.maximum_wealth([[3, 2], [1, 2]]), 2)

    def test_center_mixed_positions(self):
        self.assertEqual(self.sol.maximum_wealth([[5, 3], [3, 1], [3, 2], [3, 4]]), 3)


if __name__ == "__main__":
    unittest.main()
