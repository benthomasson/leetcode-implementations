from typing import List


def reverse_string(words: List[str], order: str) -> bool:
    """Check if words are sorted lexicographically in alien language order.

    Args:
        words: List of words to check.
        order: 26-char string defining alien alphabet order.

    Returns:
        True if words are sorted in the given order.
    """
    rank = {c: i for i, c in enumerate(order)}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        for j in range(len(w1)):
            if j >= len(w2):
                return False
            if rank[w1[j]] < rank[w2[j]]:
                break
            if rank[w1[j]] > rank[w2[j]]:
                return False

    return True
