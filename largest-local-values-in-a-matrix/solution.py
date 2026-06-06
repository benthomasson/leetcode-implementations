"""Largest Local Values in a Matrix."""


def largest_matrix(grid: list[list[int]]) -> list[list[int]]:
    """Find the largest value in every contiguous 3x3 submatrix.

    Args:
        grid: An n x n integer matrix (3 <= n <= 100).

    Returns:
        An (n-2) x (n-2) matrix of local maximums.
    """
    n = len(grid)
    return [
        [
            max(grid[r][c] for r in range(i, i + 3) for c in range(j, j + 3))
            for j in range(n - 2)
        ]
        for i in range(n - 2)
    ]
