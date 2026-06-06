"""Rotate String - check if s can become goal after some number of shifts."""


def can_transform(s: str, goal: str) -> bool:
    """Check if s can become goal by rotating characters left.

    Args:
        s: Source string.
        goal: Target string.

    Returns:
        True if s can be rotated to match goal.
    """
    return len(s) == len(goal) and goal in s + s
