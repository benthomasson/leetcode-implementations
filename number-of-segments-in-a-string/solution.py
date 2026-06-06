"""Count the number of segments in a string."""


def count_segments(s: str) -> int:
    """Return the number of segments in the string.

    A segment is a contiguous sequence of non-space characters.

    Args:
        s: Input string containing words separated by spaces.

    Returns:
        The number of segments in the string.
    """
    return len(s.split())
