from collections import Counter


def stringWithDifferentDifference(words: list[str]) -> str:
    """Find the string whose difference integer array differs from all others.

    Args:
        words: List of equal-length strings of lowercase English letters.

    Returns:
        The string with the unique difference array.
    """
    def diff(w: str) -> tuple[int, ...]:
        return tuple(ord(w[i + 1]) - ord(w[i]) for i in range(len(w) - 1))

    diffs = [diff(w) for w in words]
    counts = Counter(diffs)
    for w, d in zip(words, diffs):
        if counts[d] == 1:
            return w
    return ""
