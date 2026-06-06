def min_moves(nums: list[int]) -> int:
    """Count elements with both a strictly smaller and strictly greater element in nums.

    Args:
        nums: List of integers.

    Returns:
        Number of elements strictly between the min and max values.
    """
    min_val = min(nums)
    max_val = max(nums)
    return sum(1 for x in nums if min_val < x < max_val)
