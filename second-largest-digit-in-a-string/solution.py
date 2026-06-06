"""Second Largest Digit in a String."""


def second_highest(s: str) -> int:
    """Return the second largest digit in s, or -1 if it doesn't exist.

    Args:
        s: Alphanumeric string of lowercase letters and/or digits.

    Returns:
        The second largest unique digit, or -1.
    """
    digits = {int(c) for c in s if c.isdigit()}
    if len(digits) < 2:
        return -1
    digits.remove(max(digits))
    return max(digits)
