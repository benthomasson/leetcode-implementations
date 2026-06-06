"""Robot Return to Origin - LeetCode Solution."""


def judgeCircle(moves: str) -> bool:
    """Determine if a robot returns to the origin after executing moves.

    Args:
        moves: String of 'U', 'D', 'L', 'R' moves.

    Returns:
        True if the robot ends at (0, 0), False otherwise.
    """
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
