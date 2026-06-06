"""Tests for LeetCode 598: Range Addition II."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestMaxCount(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(self.s.maxCount(3, 3, [[2, 2], [3, 3]]), 4)

    def test_example2(self):
        self.assertEqual(self.s.maxCount(3, 3, [[2, 2], [3, 3], [3, 3], [3, 3],
                                                  [2, 2], [3, 3], [3, 3], [3, 3],
                                                  [2, 2], [3, 3], [3, 3], [3, 3]]), 4)

    def test_example3_empty_ops(self):
        self.assertEqual(self.s.maxCount(3, 3, []), 9)

    # --- Edge cases ---
    def test_single_op(self):
        self.assertEqual(self.s.maxCount(5, 5, [[3, 4]]), 12)

    def test_all_ops_cover_full_matrix(self):
        self.assertEqual(self.s.maxCount(3, 3, [[3, 3], [3, 3]]), 9)

    def test_min_result_1x1(self):
        self.assertEqual(self.s.maxCount(4, 4, [[1, 1], [2, 3]]), 1)

    def test_single_row_matrix(self):
        self.assertEqual(self.s.maxCount(1, 5, [[1, 3], [1, 2]]), 2)

    def test_single_column_matrix(self):
        self.assertEqual(self.s.maxCount(5, 1, [[3, 1], [2, 1]]), 2)

    def test_large_matrix_empty_ops(self):
        self.assertEqual(self.s.maxCount(40000, 40000, []), 1_600_000_000)

    def test_brute_force_verification(self):
        """Verify against brute-force on a small matrix."""
        m, n = 4, 5
        ops = [[2, 3], [3, 2], [4, 5]]
        # Brute force
        matrix = [[0] * n for _ in range(m)]
        for a, b in ops:
            for x in range(a):
                for y in range(b):
                    matrix[x][y] += 1
        max_val = max(max(row) for row in matrix)
        expected = sum(cell == max_val for row in matrix for cell in row)
        self.assertEqual(self.s.maxCount(m, n, ops), expected)


if __name__ == "__main__":
    unittest.main()
