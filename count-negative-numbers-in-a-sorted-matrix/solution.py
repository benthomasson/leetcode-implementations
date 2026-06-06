from typing import List


def balanced_string(grid: List[List[int]]) -> int:
    """Count negative numbers in a sorted matrix using O(n+m) staircase traversal.

    Args:
        grid: Matrix sorted in non-increasing order row-wise and column-wise.

    Returns:
        Number of negative numbers in the matrix.
    """
    m, n = len(grid), len(grid[0])
    count = 0
    row, col = 0, n - 1

    while row < m and col >= 0:
        if grid[row][col] < 0:
            count += m - row
            col -= 1
        else:
            row += 1

    return count
