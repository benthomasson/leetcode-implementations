"""Valid Perfect Square - LeetCode"""


def is_perfect_square(num: int) -> bool:
    """Check if num is a perfect square without using sqrt.

    Args:
        num: Positive integer (1 <= num <= 2^31 - 1).

    Returns:
        True if num is a perfect square, False otherwise.
    """
    if num == 0:
        return True
    lo, hi = 1, num
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        sq = mid * mid
        if sq == num:
            return True
        elif sq < num:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
