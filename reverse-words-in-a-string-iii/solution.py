"""Reverse Words in a String III."""


def reverse_words_in_string(s: str) -> str:
    """Reverse characters in each word while preserving word order.

    Args:
        s: A string of words separated by single spaces.

    Returns:
        String with each word's characters reversed.
    """
    return " ".join(word[::-1] for word in s.split(" "))
