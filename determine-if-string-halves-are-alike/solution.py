"""Determine if string halves are alike."""


def determine_if_string_halves_are_alike(s: str) -> bool:
    """Check if both halves of a string have the same number of vowels.

    Args:
        s: Even-length string of uppercase and lowercase letters.

    Returns:
        True if both halves have equal vowel counts.
    """
    vowels = set("aeiouAEIOU")
    mid = len(s) // 2
    return sum(c in vowels for c in s[:mid]) == sum(c in vowels for c in s[mid:])
