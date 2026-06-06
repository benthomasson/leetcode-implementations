"""Check Array Formation Through Concatenation."""


def canFormArray(arr: list[int], pieces: list[list[int]]) -> bool:
    """Check if arr can be formed by concatenating pieces in any order.

    Args:
        arr: Target array of distinct integers.
        pieces: Array of integer arrays with distinct integers.

    Returns:
        True if arr can be formed by concatenating pieces in some order.
    """
    lookup = {p[0]: p for p in pieces}
    i = 0
    while i < len(arr):
        piece = lookup.get(arr[i])
        if piece is None:
            return False
        for val in piece:
            if i >= len(arr) or arr[i] != val:
                return False
            i += 1
    return True
