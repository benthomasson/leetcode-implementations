"""Solution for can-make-arithmetic-progression-from-sequence."""


def can_construct(arr: list[int]) -> bool:
    """Determine if arr can be rearranged to form an arithmetic progression.

    Args:
        arr: List of integers (length >= 2).

    Returns:
        True if the array can form an arithmetic progression, False otherwise.
    """
    arr.sort()
    diff = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != diff:
            return False
    return True
