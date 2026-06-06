from collections import Counter


def count_similar_pairs(words: list[str]) -> int:
    """Count pairs of words that consist of the same set of characters.

    Args:
        words: List of lowercase English letter strings.

    Returns:
        Number of pairs (i, j) where i < j and words[i], words[j] are similar.
    """
    counts = Counter(frozenset(w) for w in words)
    return sum(n * (n - 1) // 2 for n in counts.values())
