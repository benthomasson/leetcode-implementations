def length_of_last_word(s: str) -> int:
    """Return the length of the last word in the string.

    Args:
        s: A string of words separated by spaces.

    Returns:
        Length of the last word.
    """
    return len(s.rstrip().split()[-1])
