"""Maximum Difference Between Increasing Elements."""


def min_steps_to_equal_elements(nums: list[int]) -> int:
    """Find max difference nums[j] - nums[i] where i < j and nums[i] < nums[j].

    Args:
        nums: 0-indexed integer array of size n (2 <= n <= 1000).

    Returns:
        Maximum difference, or -1 if no valid pair exists.
    """
    min_val = nums[0]
    max_diff = -1
    for j in range(1, len(nums)):
        if nums[j] > min_val:
            max_diff = max(max_diff, nums[j] - min_val)
        min_val = min(min_val, nums[j])
    return max_diff
