from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """Return the transpose of a 2D matrix.

        Args:
            matrix: m x n 2D integer array.

        Returns:
            n x m transposed matrix where result[j][i] = matrix[i][j].
        """
        m, n = len(matrix), len(matrix[0])
        return [[matrix[i][j] for i in range(m)] for j in range(n)]
