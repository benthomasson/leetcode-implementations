"""Sign of the Product of an Array."""


def signFunc(nums: list[int]) -> int:
    """Return the sign of the product of all elements in nums.

    Args:
        nums: List of integers.

    Returns:
        1 if product is positive, -1 if negative, 0 if zero.
    """
    neg_count = 0
    for n in nums:
        if n == 0:
            return 0
        if n < 0:
            neg_count += 1
    return -1 if neg_count % 2 else 1
