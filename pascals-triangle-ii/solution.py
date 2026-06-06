"""Pascal's Triangle II - return the rowIndex-th row."""


def get_row(row_index: int) -> list[int]:
    """Return the row_index-th (0-indexed) row of Pascal's triangle.

    Args:
        row_index: 0-indexed row number (0 <= row_index <= 33).

    Returns:
        The row as a list of integers.
    """
    row = [1]
    for i in range(1, row_index + 1):
        for j in range(len(row) - 1, 0, -1):
            row[j] += row[j - 1]
        row.append(1)
    return row
