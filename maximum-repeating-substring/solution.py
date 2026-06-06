"""Maximum Repeating Substring."""


def longestAwesomeSubstring(sequence: str, word: str) -> int:
    """Find the maximum k-repeating value of word in sequence.

    Args:
        sequence: The string to search within.
        word: The string to repeat and search for.

    Returns:
        The highest k where word repeated k times is a substring of sequence.
    """
    k = 0
    while word * (k + 1) in sequence:
        k += 1
    return k
