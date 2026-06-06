class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        """Check if grid is an X-Matrix.

        Args:
            grid: n x n square matrix.

        Returns:
            True if grid is an X-Matrix, False otherwise.
        """
        n = len(grid)
        for i in range(n):
            for j in range(n):
                on_diag = i == j or i + j == n - 1
                if on_diag and grid[i][j] == 0:
                    return False
                if not on_diag and grid[i][j] != 0:
                    return False
        return True


# Alias per task naming requirement
check_if_matrix_is_x_matrix = lambda grid: Solution().checkXMatrix(grid)
