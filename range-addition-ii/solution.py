"""LeetCode 598: Range Addition II."""

import unittest
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        """Count maximum integers in matrix after performing all operations.

        Args:
            m: Number of rows.
            n: Number of columns.
            ops: List of [ai, bi] operations incrementing submatrix [0..ai-1][0..bi-1].

        Returns:
            Number of cells containing the maximum value.
        """
        if not ops:
            return m * n
        min_a = min(op[0] for op in ops)
        min_b = min(op[1] for op in ops)
        return min_a * min_b


class TestMaxCount(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.maxCount(3, 3, [[2, 2], [3, 3]]), 4)

    def test_example2(self):
        self.assertEqual(self.s.maxCount(3, 3, [[2, 2], [3, 3], [3, 3], [3, 3],
                                                  [2, 2], [3, 3], [3, 3], [3, 3],
                                                  [2, 2], [3, 3], [3, 3], [3, 3]]), 4)

    def test_empty_ops(self):
        self.assertEqual(self.s.maxCount(3, 3, []), 9)

    def test_single_op(self):
        self.assertEqual(self.s.maxCount(5, 5, [[3, 4]]), 12)

    def test_full_matrix_ops(self):
        self.assertEqual(self.s.maxCount(3, 3, [[3, 3], [3, 3]]), 9)

    def test_one_by_one(self):
        self.assertEqual(self.s.maxCount(4, 4, [[1, 1], [2, 3]]), 1)

    def test_single_row(self):
        self.assertEqual(self.s.maxCount(1, 5, [[1, 3], [1, 2]]), 2)

    def test_single_column(self):
        self.assertEqual(self.s.maxCount(5, 1, [[3, 1], [2, 1]]), 2)


if __name__ == "__main__":
    unittest.main()
