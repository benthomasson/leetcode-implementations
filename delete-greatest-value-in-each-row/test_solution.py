"""Tests for Delete Greatest Value in Each Row."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import maxValueAfterOperations


class TestMaxValueAfterOperations(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(maxValueAfterOperations([[1, 2, 4], [3, 3, 1]]), 8)

    def test_example2(self):
        self.assertEqual(maxValueAfterOperations([[10]]), 10)

    def test_single_row(self):
        # Single row: sum of all elements
        self.assertEqual(maxValueAfterOperations([[3, 1, 2]]), 6)

    def test_single_column(self):
        # Single column: max of the column
        self.assertEqual(maxValueAfterOperations([[5], [3], [7]]), 7)

    def test_all_same(self):
        self.assertEqual(maxValueAfterOperations([[2, 2], [2, 2]]), 4)

    def test_descending_rows(self):
        # Rows already sorted descending
        self.assertEqual(maxValueAfterOperations([[9, 5, 1], [8, 6, 2]]), 17)

    def test_min_values(self):
        # All minimum constraint values
        self.assertEqual(maxValueAfterOperations([[1, 1], [1, 1]]), 2)

    def test_max_constraint_grid(self):
        # 50x50 grid of max values
        grid = [[100] * 50 for _ in range(50)]
        self.assertEqual(maxValueAfterOperations(grid), 5000)

    def test_three_rows(self):
        # 3 rows with varied values
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # Sorted: same. Column maxes: 7, 8, 9 -> 24
        self.assertEqual(maxValueAfterOperations(grid), 24)


if __name__ == "__main__":
    unittest.main()
