def title_to_number(columnTitle: str) -> int:
    """Convert Excel column title to column number.

    Args:
        columnTitle: Uppercase letter string representing an Excel column.

    Returns:
        The corresponding column number (1-indexed).
    """
    result = 0
    for c in columnTitle:
        result = result * 26 + (ord(c) - ord('A') + 1)
    return result
