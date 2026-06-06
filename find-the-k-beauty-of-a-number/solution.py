"""Solution for LeetCode: Find the K-Beauty of a Number."""


def divisor_substrings(num: int, k: int) -> int:
    """Return the k-beauty of num (count of length-k substrings that divide num).

    Args:
        num: The integer to evaluate.
        k: The length of substrings to consider.

    Returns:
        The number of length-k substrings of num that are non-zero divisors of num.
    """
    s = str(num)
    count = 0
    for i in range(len(s) - k + 1):
        sub = int(s[i:i + k])
        if sub != 0 and num % sub == 0:
            count += 1
    return count
