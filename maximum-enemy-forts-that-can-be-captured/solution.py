"""Maximum Enemy Forts That Can Be Captured."""


def max_captured_forts(forts: list[int]) -> int:
    """Return max enemy forts captured by moving from a 1 to a -1 (or vice versa) over only 0s.

    Args:
        forts: List of -1, 0, or 1 representing fort positions.

    Returns:
        Maximum number of enemy forts that can be captured.
    """
    result = 0
    last_non_zero = -1

    for i, val in enumerate(forts):
        if val != 0:
            if last_non_zero != -1 and forts[last_non_zero] != val:
                result = max(result, i - last_non_zero - 1)
            last_non_zero = i

    return result
