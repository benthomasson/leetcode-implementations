"""Remove digit from number to maximize result."""


def max_number_after_remove_digit(number: str, digit: str) -> str:
    """Remove one occurrence of digit from number to maximize the result.

    Args:
        number: String representing a positive integer (digits '1'-'9').
        digit: Single character digit to remove.

    Returns:
        The maximized number string after removing exactly one occurrence.
    """
    last = -1
    for i, ch in enumerate(number):
        if ch == digit:
            last = i
            if i + 1 < len(number) and number[i + 1] > digit:
                return number[:i] + number[i + 1:]
    return number[:last] + number[last + 1:]
