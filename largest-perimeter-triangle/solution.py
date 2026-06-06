def min_area_rect(nums: list[int]) -> int:
    """Return the largest perimeter of a triangle formable from nums, or 0.

    Args:
        nums: List of side lengths.

    Returns:
        Largest valid triangle perimeter, or 0 if none exists.
    """
    nums.sort(reverse=True)
    for i in range(len(nums) - 2):
        if nums[i] < nums[i + 1] + nums[i + 2]:
            return nums[i] + nums[i + 1] + nums[i + 2]
    return 0
