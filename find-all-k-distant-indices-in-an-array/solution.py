from typing import List


def find_k_distant_indices(nums: List[int], key: int, k: int) -> List[int]:
    """Find all k-distant indices in an array.

    Args:
        nums: 0-indexed integer array.
        key: Target value to match.
        k: Maximum distance threshold.

    Returns:
        Sorted list of all k-distant indices.
    """
    n = len(nums)
    result = set()
    for j, val in enumerate(nums):
        if val == key:
            for i in range(max(0, j - k), min(n, j + k + 1)):
                result.add(i)
    return sorted(result)
