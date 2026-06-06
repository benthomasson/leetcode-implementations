from collections import Counter


def can_equal_frequency(word: str) -> bool:
    """Check if removing one letter makes all remaining letter frequencies equal.

    Args:
        word: A string of lowercase English letters (length 2-100).

    Returns:
        True if removing exactly one letter equalizes all frequencies.
    """
    for i in range(len(word)):
        counts = Counter(word[:i] + word[i + 1:])
        if len(set(counts.values())) == 1:
            return True
    return False
