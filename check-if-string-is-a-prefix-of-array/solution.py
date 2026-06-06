"""Check if string is a prefix of array."""


def is_prefix_string(s: str, words: list[str]) -> bool:
    """Return True if s equals the concatenation of the first k words.

    Args:
        s: Target string.
        words: List of strings to concatenate.

    Returns:
        True if s is a prefix string of words.
    """
    prefix = ""
    for word in words:
        prefix += word
        if prefix == s:
            return True
        if len(prefix) > len(s):
            return False
    return False
