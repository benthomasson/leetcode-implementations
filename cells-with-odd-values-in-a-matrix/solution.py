"""LeetCode 1252: Cells with Odd Values in a Matrix."""

import unittest
from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        """Return count of odd-valued cells after applying row/col increments.

        Args:
            m: Number of rows.
            n: Number of columns.
            indices: List of [row, col] pairs to increment.

        Returns:
            Number of cells with odd values.
        """
        row_count = [0] * m
        col_count = [0] * n
        for r, c in indices:
            row_count[r] += 1
            col_count[c] += 1

        odd_rows = sum(x % 2 for x in row_count)
        odd_cols = sum(x % 2 for x in col_count)
        return odd_rows * (n - odd_cols) + (m - odd_rows) * odd_cols


class TestOddCells(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.oddCells(2, 3, [[0, 1], [1, 1]]), 6)

    def test_example2(self):
        self.assertEqual(self.s.oddCells(2, 2, [[1, 1], [0, 0]]), 0)

    def test_single_cell(self):
        # row0=1, col0=1 -> cell=2 (even) -> 0 odd
        self.assertEqual(self.s.oddCells(1, 1, [[0, 0]]), 0)

    def test_single_cell_even(self):
        self.assertEqual(self.s.oddCells(1, 1, [[0, 0], [0, 0]]), 0)

    def test_single_row(self):
        # row0=1(odd), col0=1(odd), col1=0, col2=0
        # cells: [2,1,1] -> 2 odd
        self.assertEqual(self.s.oddCells(1, 3, [[0, 0]]), 2)

    def test_single_col(self):
        # row0=1(odd), col0=1(odd), rows 1,2 even
        # cells: [2],[1],[1] -> 2 odd
        self.assertEqual(self.s.oddCells(3, 1, [[0, 0]]), 2)

    def test_all_rows_and_cols_hit(self):
        # Every row and col incremented once -> all cells = 2 (even)
        self.assertEqual(self.s.oddCells(2, 2, [[0, 0], [1, 1]]), 0)

    def test_repeated_same_index(self):
        # row0=3(odd), col0=3(odd) -> cells (0,1) and (1,0) are odd
        self.assertEqual(self.s.oddCells(2, 2, [[0, 0], [0, 0], [0, 0]]), 2)

    def test_large_indices(self):
        # Stress: 50x50 matrix with 100 increments all on row 0, col 0
        indices = [[0, 0]] * 100
        # row0=100(even), col0=100(even) -> 0 odd cells
        self.assertEqual(self.s.oddCells(50, 50, indices), 0)


if __name__ == "__main__":
    unittest.main()
