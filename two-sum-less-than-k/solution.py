def max_sum_under_k(nums: list[int], k: int) -> int:
    """Find the maximum pair sum strictly less than k.

    Args:
        nums: List of positive integers.
        k: Upper bound (exclusive) for the pair sum.

    Returns:
        Maximum sum of two distinct-index elements less than k, or -1 if none exists.
    """
    nums.sort()
    left, right = 0, len(nums) - 1
    result = -1
    while left < right:
        s = nums[left] + nums[right]
        if s < k:
            result = max(result, s)
            left += 1
        else:
            right -= 1
    return result
