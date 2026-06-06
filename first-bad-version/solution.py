"""First Bad Version - Binary search solution."""

from typing import Callable


def first_bad_version(n: int, isBadVersion: Callable[[int], bool]) -> int:
    """Find the first bad version using binary search.

    Args:
        n: Total number of versions (1 to n).
        isBadVersion: API that returns True if a version is bad.

    Returns:
        The first bad version number.
    """
    left, right = 1, n
    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left
