"""Smallest Index With Equal Value."""


def smallest_index(nums: list[int]) -> int:
    """Return the smallest index i where i mod 10 == nums[i], or -1.

    Args:
        nums: 0-indexed integer array with values 0-9.

    Returns:
        Smallest valid index, or -1 if none exists.
    """
    for i, val in enumerate(nums):
        if i % 10 == val:
            return i
    return -1
