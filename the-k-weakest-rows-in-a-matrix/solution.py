"""The K Weakest Rows in a Matrix."""


def kWeakestRows(mat: list[list[int]], k: int) -> list[int]:
    """Return indices of the k weakest rows ordered from weakest to strongest.

    Args:
        mat: Binary matrix where 1s (soldiers) appear before 0s (civilians).
        k: Number of weakest rows to return.

    Returns:
        List of k row indices sorted by soldier count, then by index.
    """
    return [i for i, _ in sorted(enumerate(mat), key=lambda x: sum(x[1]))][:k]
