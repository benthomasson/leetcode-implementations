"""Valid Word Square."""


def valid_word_square(words: list[str]) -> bool:
    """Check if words form a valid word square.

    Args:
        words: List of strings to check.

    Returns:
        True if words form a valid word square.
    """
    for i, word in enumerate(words):
        for j, ch in enumerate(word):
            if j >= len(words) or i >= len(words[j]) or words[j][i] != ch:
                return False
    return True
