from collections import Counter


def firstUniqChar(s: str) -> int:
    """Find the first non-repeating character in a string and return its index.

    Args:
        s: A string of lowercase English letters.

    Returns:
        Index of the first non-repeating character, or -1 if none exists.
    """
    counts = Counter(s)
    for i, c in enumerate(s):
        if counts[c] == 1:
            return i
    return -1
