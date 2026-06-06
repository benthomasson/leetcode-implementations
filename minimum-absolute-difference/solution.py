from typing import List


def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
    """Find all pairs with minimum absolute difference.

    Args:
        arr: Array of distinct integers.

    Returns:
        Pairs [a, b] with a < b and b - a equal to the min absolute difference.
    """
    arr.sort()
    min_diff = min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))
    return [[arr[i], arr[i + 1]] for i in range(len(arr) - 1) if arr[i + 1] - arr[i] == min_diff]
