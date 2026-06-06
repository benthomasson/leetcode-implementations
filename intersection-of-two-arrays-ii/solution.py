from collections import Counter


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    """Return the intersection of two arrays, preserving duplicate counts.

    Args:
        nums1: First integer array.
        nums2: Second integer array.

    Returns:
        List of common elements, each appearing min(count1, count2) times.
    """
    counts = Counter(nums1)
    result = []
    for num in nums2:
        if counts[num] > 0:
            result.append(num)
            counts[num] -= 1
    return result
