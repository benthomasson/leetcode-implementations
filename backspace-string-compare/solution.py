"""Backspace String Compare - O(n) time, O(1) space two-pointer solution."""


def backspaceCompare(s: str, t: str) -> bool:
    """Return True if s and t are equal after processing '#' as backspace.

    Args:
        s: First string containing lowercase letters and '#' characters.
        t: Second string containing lowercase letters and '#' characters.

    Returns:
        True if both strings are equal after applying backspaces.
    """
    i, j = len(s) - 1, len(t) - 1

    while True:
        i = _next_valid(s, i)
        j = _next_valid(t, j)

        if i < 0 and j < 0:
            return True
        if i < 0 or j < 0:
            return False
        if s[i] != t[j]:
            return False

        i -= 1
        j -= 1


def _next_valid(string: str, index: int) -> int:
    """Walk backward past backspaced characters, returning the next valid index."""
    skip = 0
    while index >= 0:
        if string[index] == '#':
            skip += 1
            index -= 1
        elif skip > 0:
            skip -= 1
            index -= 1
        else:
            break
    return index
