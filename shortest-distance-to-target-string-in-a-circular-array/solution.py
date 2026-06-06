"""Shortest Distance to Target String in a Circular Array."""


def shortest_distance(words: list[str], target: str, startIndex: int) -> int:
    """Find shortest distance to target in a circular array.

    Args:
        words: Circular array of strings.
        target: Target string to find.
        startIndex: Starting position in the array.

    Returns:
        Shortest distance to target, or -1 if not found.
    """
    n = len(words)
    result = n  # impossibly large sentinel
    for i in range(n):
        if words[i] == target:
            dist = abs(i - startIndex)
            result = min(result, dist, n - dist)
    return result if result < n else -1
