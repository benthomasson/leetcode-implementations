"""Greatest English Letter in Upper and Lower Case."""


def greatest_letter(s: str) -> str:
    """Return the greatest letter appearing in both cases, or empty string.

    Args:
        s: String of English letters.

    Returns:
        The greatest uppercase letter found in both cases, or "".
    """
    chars = set(s)
    for c in "ZYXWVUTSRQPONMLKJIHGFEDCBA":
        if c in chars and c.lower() in chars:
            return c
    return ""
