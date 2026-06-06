from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """Return the sum of both diagonals of a square matrix, counting center once.

        Args:
            mat: Square matrix of integers.

        Returns:
            Sum of primary and secondary diagonal elements.
        """
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i] + mat[i][n - 1 - i]
        if n % 2:
            total -= mat[n // 2][n // 2]
        return total
