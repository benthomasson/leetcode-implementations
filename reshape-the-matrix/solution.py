"""Reshape the Matrix - LeetCode Solution."""


class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        """Reshape matrix to r x c if possible, otherwise return original.

        Args:
            mat: Original m x n matrix.
            r: Target number of rows.
            c: Target number of columns.

        Returns:
            Reshaped r x c matrix, or original if reshape is impossible.
        """
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        flat = [val for row in mat for val in row]
        return [flat[i * c:(i + 1) * c] for i in range(r)]
