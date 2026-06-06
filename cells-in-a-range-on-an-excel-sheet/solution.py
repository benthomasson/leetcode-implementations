"""Solution for LeetCode: Cells in a Range on an Excel Sheet."""


def cell_range(s: str) -> list[str]:
    """Return all cells in the range specified by s, sorted by column then row.

    Args:
        s: Range string in format "C1:C2" where C is a column letter and 1/2 are row digits.

    Returns:
        List of cell strings in non-decreasing order by column, then by row.
    """
    c1, r1, c2, r2 = s[0], int(s[1]), s[3], int(s[4])
    return [
        f"{chr(c)}{r}"
        for c in range(ord(c1), ord(c2) + 1)
        for r in range(r1, r2 + 1)
    ]
