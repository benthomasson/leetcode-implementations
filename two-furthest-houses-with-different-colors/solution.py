"""Two Furthest Houses With Different Colors."""

import unittest
from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        """Return max distance between two houses with different colors.

        Args:
            colors: List of house colors (0-indexed).

        Returns:
            Maximum absolute index difference between two differently-colored houses.
        """
        n = len(colors)
        result = 0

        # Check from the start: find furthest house != colors[0]
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                result = max(result, i)
                break

        # Check from the end: find furthest house != colors[-1]
        for i in range(n):
            if colors[i] != colors[-1]:
                result = max(result, n - 1 - i)
                break

        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.maxDistance([1, 1, 1, 6, 1, 1, 1]), 3)

    def test_example2(self):
        self.assertEqual(self.s.maxDistance([1, 8, 3, 8, 3]), 4)

    def test_example3(self):
        self.assertEqual(self.s.maxDistance([0, 1]), 1)

    def test_different_endpoints(self):
        self.assertEqual(self.s.maxDistance([1, 1, 1, 1, 2]), 4)

    def test_all_same_except_first(self):
        self.assertEqual(self.s.maxDistance([5, 3, 3, 3, 3]), 4)

    def test_alternating(self):
        self.assertEqual(self.s.maxDistance([1, 2, 1, 2, 1]), 4)

    def test_same_endpoints_diff_middle(self):
        self.assertEqual(self.s.maxDistance([1, 2, 1]), 1)


if __name__ == "__main__":
    unittest.main()
