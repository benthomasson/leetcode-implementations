"""Surface Area of 3D Shapes (LeetCode 892)."""

from typing import List
import unittest


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        """Calculate total surface area of 3D shapes formed by stacked cubes.

        Args:
            grid: n x n grid where grid[i][j] is the height of cubes at (i, j).

        Returns:
            Total exposed surface area.
        """
        n = len(grid)
        area = 0
        for i in range(n):
            for j in range(n):
                v = grid[i][j]
                if v > 0:
                    area += 2 + 4 * v
                if i + 1 < n:
                    area -= 2 * min(v, grid[i + 1][j])
                if j + 1 < n:
                    area -= 2 * min(v, grid[i][j + 1])
        return area


class TestSurfaceArea(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.surfaceArea([[1, 2], [3, 4]]), 34)

    def test_example2(self):
        self.assertEqual(self.s.surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), 32)

    def test_example3(self):
        self.assertEqual(self.s.surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]), 46)

    def test_single_cell_zero(self):
        self.assertEqual(self.s.surfaceArea([[0]]), 0)

    def test_single_cell_one(self):
        self.assertEqual(self.s.surfaceArea([[1]]), 6)

    def test_single_cell_tall(self):
        self.assertEqual(self.s.surfaceArea([[5]]), 22)

    def test_all_zeros(self):
        self.assertEqual(self.s.surfaceArea([[0, 0], [0, 0]]), 0)

    def test_uniform_height(self):
        # 3x3 grid all height 1: each cell contributes 6, minus 2*12 shared faces = 54-24=30
        self.assertEqual(self.s.surfaceArea([[1, 1, 1], [1, 1, 1], [1, 1, 1]]), 30)


if __name__ == "__main__":
    unittest.main()
