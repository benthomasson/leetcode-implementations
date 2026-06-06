"""Matrix Cells in Distance Order - LeetCode 1030."""

from collections import deque


class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> list[list[int]]:
        """Return all matrix cells sorted by Manhattan distance from (rCenter, cCenter).

        Args:
            rows: Number of rows in the matrix.
            cols: Number of columns in the matrix.
            rCenter: Row coordinate of the center cell.
            cCenter: Column coordinate of the center cell.

        Returns:
            List of [row, col] coordinates sorted by ascending Manhattan distance.
        """
        result = []
        visited = [[False] * cols for _ in range(rows)]
        queue = deque([(rCenter, cCenter)])
        visited[rCenter][cCenter] = True

        while queue:
            r, c = queue.popleft()
            result.append([r, c])
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

        return result
