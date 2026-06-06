"""Tests for LeetCode 1252: Cells with Odd Values in a Matrix."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


def brute_force(m, n, indices):
    """Reference implementation: build the actual matrix and count odds."""
    matrix = [[0] * n for _ in range(m)]
    for r, c in indices:
        for j in range(n):
            matrix[r][j] += 1
        for i in range(m):
            matrix[i][c] += 1
    return sum(cell % 2 for row in matrix for cell in row)


class TestOddCells(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.oddCells(2, 3, [[0, 1], [1, 1]]), 6)

    def test_example2(self):
        self.assertEqual(self.s.oddCells(2, 2, [[1, 1], [0, 0]]), 0)

    def test_single_cell(self):
        self.assertEqual(self.s.oddCells(1, 1, [[0, 0]]), 0)

    def test_single_row(self):
        self.assertEqual(self.s.oddCells(1, 3, [[0, 0]]), 2)

    def test_single_col(self):
        self.assertEqual(self.s.oddCells(3, 1, [[0, 0]]), 2)

    def test_all_even(self):
        self.assertEqual(self.s.oddCells(2, 2, [[0, 0], [1, 1]]), 0)

    def test_repeated_index(self):
        self.assertEqual(self.s.oddCells(2, 2, [[0, 0], [0, 0], [0, 0]]), 2)

    def test_max_size(self):
        indices = [[0, 0]] * 100
        self.assertEqual(self.s.oddCells(50, 50, indices), 0)

    def test_against_brute_force(self):
        """Cross-check optimized solution against brute-force on several inputs."""
        cases = [
            (2, 3, [[0, 1], [1, 1]]),
            (3, 3, [[0, 0], [1, 2], [2, 1]]),
            (4, 5, [[0, 0], [1, 1], [2, 2], [3, 3]]),
            (1, 1, [[0, 0]]),
            (5, 5, [[0, 0], [0, 0], [0, 0]]),
        ]
        for m, n, indices in cases:
            with self.subTest(m=m, n=n, indices=indices):
                self.assertEqual(self.s.oddCells(m, n, indices), brute_force(m, n, indices))


if __name__ == "__main__":
    unittest.main()
