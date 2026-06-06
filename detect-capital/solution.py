"""Detect Capital - LeetCode Problem."""


def detectCapitalUse(word: str) -> bool:
    """Return True if capitalization usage in word is correct.

    Args:
        word: String of English letters.

    Returns:
        True if all caps, all lower, or only first letter capitalized.
    """
    upper_count = sum(1 for c in word if c.isupper())
    return upper_count == 0 or upper_count == len(word) or (upper_count == 1 and word[0].isupper())
