"""Difference Between Element Sum and Digit Sum of an Array."""


def difference_between_element_and_digit_sum(nums: list[int]) -> int:
    """Return absolute difference between element sum and digit sum of nums.

    Args:
        nums: List of positive integers.

    Returns:
        Absolute difference between the element sum and digit sum.
    """
    element_sum = 0
    digit_sum = 0
    for num in nums:
        element_sum += num
        while num > 0:
            digit_sum += num % 10
            num //= 10
    return abs(element_sum - digit_sum)
