"""Find Subsequence of Length K With the Largest Sum."""

from typing import List


def count_patterns_in_word(nums: List[int], k: int) -> List[int]:
    """Return a subsequence of length k with the largest sum, preserving original order.

    Args:
        nums: Integer array.
        k: Length of the desired subsequence.

    Returns:
        A length-k subsequence with the largest possible sum.
    """
    # Pair each element with its index, pick the k largest by value
    indexed = sorted(enumerate(nums), key=lambda x: x[1], reverse=True)[:k]
    # Restore original order by sorting by index
    indexed.sort(key=lambda x: x[0])
    return [val for _, val in indexed]
