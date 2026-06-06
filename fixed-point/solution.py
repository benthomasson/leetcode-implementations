from typing import List


def fixedPoint(arr: List[int]) -> int:
    """Find the smallest fixed point index where arr[i] == i.

    Args:
        arr: Sorted array of distinct integers.

    Returns:
        Smallest index i where arr[i] == i, or -1 if none exists.
    """
    lo, hi = 0, len(arr) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] >= mid:
            if arr[mid] == mid:
                result = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return result
