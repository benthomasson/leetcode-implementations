"""Repeated Substring Pattern - LeetCode solution."""


def can_construct(s: str) -> bool:
    """Check if s can be constructed by repeating a substring.

    Args:
        s: Input string of lowercase English letters.

    Returns:
        True if s is made of repeated copies of a substring.
    """
    return s in (s + s)[1:-1]
