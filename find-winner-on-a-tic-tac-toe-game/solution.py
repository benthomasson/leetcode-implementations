"""Tic-Tac-Toe winner determination."""


def validateBinaryTreeNodes(moves: list[list[int]]) -> str:
    """Determine the winner of a tic-tac-toe game given a sequence of moves.

    Args:
        moves: List of [row, col] pairs representing moves in order (A first).

    Returns:
        "A " if A wins, "B " if B wins, "Draw " if tied, "Pending " if ongoing.
    """
    grid = [[0] * 3 for _ in range(3)]
    wins = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    for i, (r, c) in enumerate(moves):
        player = 1 if i % 2 == 0 else 2
        grid[r][c] = player
        for line in wins:
            if all(grid[lr][lc] == player for lr, lc in line):
                return "A " if player == 1 else "B "

    return "Draw " if len(moves) == 9 else "Pending "
