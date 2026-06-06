"""Distribute Candies - LeetCode"""


def maxNumberOfCandies(candyType: list[int]) -> int:
    """Return max number of different candy types Alice can eat (n/2 candies).

    Args:
        candyType: List of candy types where candyType[i] is the type of ith candy.

    Returns:
        Maximum number of different types she can eat.
    """
    return min(len(candyType) // 2, len(set(candyType)))
