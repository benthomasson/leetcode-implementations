"""Separate the Digits in an Array."""


def separate_digits(nums: list[int]) -> list[int]:
    """Separate each integer in nums into its individual digits.

    Args:
        nums: List of positive integers.

    Returns:
        List of individual digits in the same order.
    """
    return [int(d) for num in nums for d in str(num)]
