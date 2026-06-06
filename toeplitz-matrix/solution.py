from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """Check if a matrix is Toeplitz (all top-left to bottom-right diagonals have equal elements).

        Args:
            matrix: m x n matrix where 1 <= m, n <= 20.

        Returns:
            True if every diagonal has the same elements.
        """
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True
