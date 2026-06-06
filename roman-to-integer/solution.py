"""Roman numeral to integer conversion."""


def roman_to_int(s: str) -> int:
    """Convert a roman numeral string to an integer.

    Args:
        s: A valid roman numeral string (1-3999).

    Returns:
        The integer value of the roman numeral.
    """
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            result -= values[s[i]]
        else:
            result += values[s[i]]
    return result
