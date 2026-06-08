"""Find the Difference - LeetCode solution."""

from functools import reduce
from operator import xor


def findTheDifference(s: str, t: str) -> str:
    """Find the extra character added to string t.

    Args:
        s: Original string.
        t: Shuffled string with one extra character.

    Returns:
        The added character.
    """
    return chr(reduce(xor, (ord(c) for c in s + t), 0))
