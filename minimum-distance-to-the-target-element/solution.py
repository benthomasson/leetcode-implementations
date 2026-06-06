"""Minimum Distance to the Target Element."""


def get_min_distance(nums: list[int], target: int, start: int) -> int:
    """Find minimum absolute distance from start to any index where nums[i] == target.

    Args:
        nums: Integer array (0-indexed).
        target: Target value to find.
        start: Starting index to measure distance from.

    Returns:
        Minimum abs(i - start) where nums[i] == target.
    """
    return min(abs(i - start) for i, v in enumerate(nums) if v == target)
