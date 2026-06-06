"""Delete Greatest Value in Each Row."""

import unittest
from typing import List


def maxValueAfterOperations(grid: List[List[int]]) -> int:
    """Sort each row, then sum the column-wise maximums.

    Args:
        grid: m x n matrix of positive integers.

    Returns:
        Sum of max deleted elements per operation.
    """
    for row in grid:
        row.sort()
    return sum(max(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0])))


class TestMaxValueAfterOperations(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(maxValueAfterOperations([[1, 2, 4], [3, 3, 1]]), 8)

    def test_example2(self):
        self.assertEqual(maxValueAfterOperations([[10]]), 10)

    def test_single_row(self):
        self.assertEqual(maxValueAfterOperations([[3, 1, 2]]), 6)

    def test_single_column(self):
        self.assertEqual(maxValueAfterOperations([[5], [3], [7]]), 7)

    def test_all_same(self):
        self.assertEqual(maxValueAfterOperations([[2, 2], [2, 2]]), 4)

    def test_descending_rows(self):
        self.assertEqual(maxValueAfterOperations([[9, 5, 1], [8, 6, 2]]), 17)

    def test_large_grid(self):
        grid = [[100] * 50 for _ in range(50)]
        self.assertEqual(maxValueAfterOperations(grid), 100 * 50)


if __name__ == "__main__":
    unittest.main()
