from typing import List


class Solution:
    def regionsBySlashes(self, board: List[List[str]]) -> int:
        """Count pawns the rook can capture in 4 cardinal directions.

        Args:
            board: 8x8 grid with 'R', 'B', 'p', and '.'.

        Returns:
            Number of pawns attackable by the rook.
        """
        rr = rc = -1
        for r in range(8):
            for c in range(8):
                if board[r][c] == "R":
                    rr, rc = r, c
        if rr == -1:
            raise ValueError("No rook found on the board")

        captures = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = rr + dr, rc + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == "B":
                    break
                if board[r][c] == "p":
                    captures += 1
                    break
                r += dr
                c += dc
        return captures
