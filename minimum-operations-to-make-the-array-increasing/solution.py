"""Minimum Operations to Make the Array Increasing."""


def min_operations(nums: list[int]) -> int:
    """Return minimum increments to make nums strictly increasing.

    Args:
        nums: Integer array to make strictly increasing.

    Returns:
        Minimum number of increment operations needed.
    """
    ops = 0
    prev = nums[0]
    for i in range(1, len(nums)):
        if nums[i] <= prev:
            prev += 1
            ops += prev - nums[i]
        else:
            prev = nums[i]
    return ops
