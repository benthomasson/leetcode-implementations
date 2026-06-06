"""LeetCode 1260: Shift 2D Grid."""

from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """Shift all elements in a 2D grid k times to the right.

        Args:
            grid: m x n 2D grid of integers.
            k: Number of shift operations.

        Returns:
            The grid after k shifts.
        """
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total
        if k == 0:
            return grid

        flat = [grid[i][j] for i in range(m) for j in range(n)]
        flat = flat[-k:] + flat[:-k]
        return [flat[i * n:(i + 1) * n] for i in range(m)]
