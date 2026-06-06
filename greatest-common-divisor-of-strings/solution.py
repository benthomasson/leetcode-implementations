"""Greatest Common Divisor of Strings."""

from math import gcd


def gcdOfStrings(str1: str, str2: str) -> str:
    """Return the largest string x that divides both str1 and str2.

    Args:
        str1: First input string.
        str2: Second input string.

    Returns:
        The largest common divisor string, or "" if none exists.
    """
    if str1 + str2 != str2 + str1:
        return ""
    return str1[:gcd(len(str1), len(str2))]
