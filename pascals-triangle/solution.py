"""Pascal's Triangle solution."""


def generate(numRows: int) -> list[list[int]]:
    """Return the first numRows of Pascal's triangle.

    Args:
        numRows: Number of rows to generate (1 <= numRows <= 30).

    Returns:
        List of rows, where each row is a list of integers.
    """
    triangle = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
