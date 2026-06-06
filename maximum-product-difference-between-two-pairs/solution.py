"""Maximum Product Difference Between Two Pairs."""


def max_product_difference(nums: list[int]) -> int:
    """Return max product difference between two pairs from nums.

    Args:
        nums: Integer array of length >= 4.

    Returns:
        Maximum (nums[w]*nums[x]) - (nums[y]*nums[z]) over distinct indices.
    """
    nums.sort()
    return nums[-1] * nums[-2] - nums[0] * nums[1]
