"""Maximize Sum of Array After K Negations."""


def largest_sum_after_k_negations(nums: list[int], k: int) -> int:
    """Return the largest possible sum after negating elements exactly k times.

    Args:
        nums: Integer array.
        k: Number of negations to apply.

    Returns:
        Maximum possible sum of the array.
    """
    nums.sort()
    i = 0
    while k > 0 and i < len(nums) and nums[i] < 0:
        nums[i] = -nums[i]
        i += 1
        k -= 1
    total = sum(nums)
    if k % 2 == 1:
        total -= 2 * min(nums)
    return total


# Alias per task requirement
is_univalued = largest_sum_after_k_negations
