from collections import Counter
from typing import List


def findLHS(nums: List[int]) -> int:
    """Return the length of the longest harmonious subsequence.

    Args:
        nums: List of integers.

    Returns:
        Length of longest subsequence where max - min == 1, or 0 if none.
    """
    count = Counter(nums)
    result = 0
    for k in count:
        if k + 1 in count:
            result = max(result, count[k] + count[k + 1])
    return result
