"""LeetCode: Average Value of Even Numbers That Are Divisible by Three."""


def average_even_divisible_by_three(nums: list[int]) -> int:
    """Return the average of all even integers divisible by 3, rounded down.

    Args:
        nums: List of positive integers.

    Returns:
        Floor average of qualifying elements, or 0 if none exist.
    """
    total = count = 0
    for n in nums:
        if n % 6 == 0:
            total += n
            count += 1
    return total // count if count else 0
