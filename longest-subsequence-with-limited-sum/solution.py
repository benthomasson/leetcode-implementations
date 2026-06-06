from bisect import bisect_right
from itertools import accumulate
from typing import List


def maxSizeSubsequenceSumQueries(nums: List[int], queries: List[int]) -> List[int]:
    """Find max subsequence sizes with sums <= each query.

    Args:
        nums: Integer array to pick subsequences from.
        queries: Sum limits for each query.

    Returns:
        List where answer[i] is the max subsequence size with sum <= queries[i].
    """
    prefix = list(accumulate(sorted(nums)))
    return [bisect_right(prefix, q) for q in queries]
