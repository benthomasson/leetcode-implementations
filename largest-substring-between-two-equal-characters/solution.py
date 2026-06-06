"""Largest Substring Between Two Equal Characters."""


def maxLengthBetweenEqualCharacters(s: str) -> int:
    """Return length of longest substring between two equal characters.

    Args:
        s: Input string of lowercase English letters.

    Returns:
        Length of longest substring between equal chars, or -1 if none.
    """
    first_seen: dict[str, int] = {}
    result = -1
    for i, c in enumerate(s):
        if c in first_seen:
            result = max(result, i - first_seen[c] - 1)
        else:
            first_seen[c] = i
    return result
