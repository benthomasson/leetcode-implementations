def find_disappeared_numbers(nums: list[int]) -> list[int]:
    """Find all numbers in [1, n] that don't appear in nums.

    Args:
        nums: List of integers where each is in range [1, n].

    Returns:
        List of missing integers from range [1, n].
    """
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]

    return [i + 1 for i, num in enumerate(nums) if num > 0]
