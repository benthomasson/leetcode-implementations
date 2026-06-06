from collections import Counter


def redistribute_characters_to_make_all_strings_equal(words: list[str]) -> bool:
    """Determine if characters can be redistributed to make all strings equal.

    Args:
        words: List of lowercase English letter strings.

    Returns:
        True if all strings can be made equal, False otherwise.
    """
    n = len(words)
    counts = Counter()
    for w in words:
        counts.update(w)
    return all(c % n == 0 for c in counts.values())
