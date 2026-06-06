from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """Calculate the perimeter of the island in the grid.

        Args:
            grid: 2D grid where 1 is land and 0 is water.

        Returns:
            The perimeter of the island.
        """
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2
        return perimeter
