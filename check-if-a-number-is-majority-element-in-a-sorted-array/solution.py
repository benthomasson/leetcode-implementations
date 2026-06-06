from bisect import bisect_left


def is_majority_element(nums: list[int], target: int) -> bool:
    """Check if target appears more than len(nums) / 2 times in sorted nums.

    Args:
        nums: Integer array sorted in non-decreasing order.
        target: The element to check.

    Returns:
        True if target is a majority element, False otherwise.
    """
    n = len(nums)
    first = bisect_left(nums, target)
    return first + n // 2 < n and nums[first + n // 2] == target
