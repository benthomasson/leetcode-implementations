from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    """Find index of target in sorted array, or where it would be inserted.

    Args:
        nums: Sorted array of distinct integers.
        target: Value to find or insert.

    Returns:
        Index of target, or insertion index to maintain sorted order.
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
