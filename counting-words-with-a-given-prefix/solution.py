"""Count words with a given prefix."""

from typing import List


def count_prefixes(words: List[str], pref: str) -> int:
    """Return the number of strings in words that start with pref.

    Args:
        words: List of lowercase English letter strings.
        pref: Prefix to search for.

    Returns:
        Count of words starting with pref.
    """
    return sum(w.startswith(pref) for w in words)
