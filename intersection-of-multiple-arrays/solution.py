from typing import List


def intersection(nums: List[List[int]]) -> List[int]:
    """Find integers present in every sub-array, returned sorted.

    Args:
        nums: 2D list of distinct positive integers.

    Returns:
        Sorted list of integers common to all sub-arrays.
    """
    result = set(nums[0])
    for arr in nums[1:]:
        result &= set(arr)
    return sorted(result)
