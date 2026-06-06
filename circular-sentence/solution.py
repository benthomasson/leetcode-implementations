"""Circular Sentence - LeetCode Problem."""


def is_circular(sentence: str) -> bool:
    """Check if a sentence is circular.

    Args:
        sentence: A string of space-separated words.

    Returns:
        True if the sentence is circular, False otherwise.
    """
    if sentence[0] != sentence[-1]:
        return False
    for i, ch in enumerate(sentence):
        if ch == ' ' and sentence[i - 1] != sentence[i + 1]:
            return False
    return True
