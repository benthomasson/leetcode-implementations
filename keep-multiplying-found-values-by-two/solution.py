"""Keep Multiplying Found Values by Two."""


def find_final_value(nums: list[int], original: int) -> int:
    """Find final value after repeatedly doubling when found in nums.

    Args:
        nums: Array of integers to search.
        original: Starting value to search for and double.

    Returns:
        Final value after all doublings.
    """
    num_set = set(nums)
    while original in num_set:
        original *= 2
    return original
