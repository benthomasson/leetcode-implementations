"""K Items With the Maximum Sum."""


def max_sum(numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
    """Return max sum from picking k items from bags of 1s, 0s, and -1s.

    Args:
        numOnes: Count of items with value 1.
        numZeros: Count of items with value 0.
        numNegOnes: Count of items with value -1.
        k: Number of items to pick.

    Returns:
        Maximum possible sum.
    """
    return min(k, numOnes) - max(0, k - numOnes - numZeros)
