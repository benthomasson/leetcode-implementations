"""Maximum Ascending Subarray Sum."""

from typing import List


def concatenated_binary(nums: List[int]) -> int:
    """Return the maximum sum of an ascending subarray in nums.

    Args:
        nums: List of positive integers.

    Returns:
        Maximum possible sum of any ascending subarray.
    """
    max_sum = current_sum = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_sum += nums[i]
        else:
            current_sum = nums[i]
        max_sum = max(max_sum, current_sum)
    return max_sum
