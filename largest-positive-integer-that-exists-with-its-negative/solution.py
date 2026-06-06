"""Solution for LeetCode: Largest Positive Integer That Exists With Its Negative."""


def find_K(nums: list[int]) -> int:
    """Find the largest positive integer k such that -k also exists in the array.

    Given an integer array that does not contain zeros, finds the largest
    positive integer k where both k and -k are present in the array.

    Args:
        nums: A list of non-zero integers with length between 1 and 1000,
            where each value is in the range [-1000, 1000].

    Returns:
        The largest positive integer k such that -k exists in nums,
        or -1 if no such integer exists.

    Examples:
        >>> find_K([-1, 2, -3, 3])
        3
        >>> find_K([-1, 10, 6, 7, -7, 1])
        7
        >>> find_K([-10, 8, 6, 7, -2, -3])
        -1
    """
    num_set = set(nums)
    result = -1
    for num in num_set:
        if num > 0 and -num in num_set:
            result = max(result, num)
    return result
