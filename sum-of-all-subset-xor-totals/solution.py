"""Sum of All Subset XOR Totals."""

from functools import reduce
from operator import or_
from typing import List


def subsetXORSum(nums: List[int]) -> int:
    """Return the sum of XOR totals for every subset of nums.

    Args:
        nums: List of positive integers.

    Returns:
        Sum of XOR totals across all subsets.
    """
    if not nums:
        return 0
    return reduce(or_, nums) * (1 << (len(nums) - 1))
