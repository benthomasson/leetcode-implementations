def equal_sum_subarrays(nums: list[int]) -> bool:
    """Determine if two length-2 subarrays with equal sum exist.

    Args:
        nums: A 0-indexed integer array with length >= 2.

    Returns:
        True if two subarrays of length 2 starting at different indices
        have the same sum, False otherwise.
    """
    seen = set()
    for i in range(len(nums) - 1):
        s = nums[i] + nums[i + 1]
        if s in seen:
            return True
        seen.add(s)
    return False
