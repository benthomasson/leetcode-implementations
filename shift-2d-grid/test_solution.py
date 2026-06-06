"""Tests for Shift 2D Grid."""

import unittest
from solution import Solution


class TestShiftGrid(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.s.shiftGrid(grid, 1), [[9, 1, 2], [3, 4, 5], [6, 7, 8]])

    def test_example2(self):
        grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
        self.assertEqual(
            self.s.shiftGrid(grid, 4),
            [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]],
        )

    def test_example3_full_cycle(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.s.shiftGrid(grid, 9), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_k_zero(self):
        grid = [[1, 2], [3, 4]]
        self.assertEqual(self.s.shiftGrid(grid, 0), [[1, 2], [3, 4]])

    def test_single_element(self):
        self.assertEqual(self.s.shiftGrid([[5]], 3), [[5]])

    def test_single_row(self):
        self.assertEqual(self.s.shiftGrid([[1, 2, 3]], 2), [[2, 3, 1]])

    def test_single_column(self):
        self.assertEqual(self.s.shiftGrid([[1], [2], [3]], 1), [[3], [1], [2]])

    def test_negative_values(self):
        grid = [[-1, -2], [-3, -4]]
        self.assertEqual(self.s.shiftGrid(grid, 1), [[-4, -1], [-2, -3]])


if __name__ == "__main__":
    unittest.main()
