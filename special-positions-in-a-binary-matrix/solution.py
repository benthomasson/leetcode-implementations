"""Special Positions in a Binary Matrix."""


class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        """Count special positions where mat[i][j]==1 and row/col have no other 1s.

        Args:
            mat: Binary matrix of 0s and 1s.

        Returns:
            Number of special positions.
        """
        m, n = len(mat), len(mat[0])
        row_sums = [sum(row) for row in mat]
        col_sums = [sum(mat[i][j] for i in range(m)) for j in range(n)]
        return sum(
            1
            for i in range(m)
            for j in range(n)
            if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1
        )
