"""Two Out of Three - LeetCode Solution."""


def largest_odd(nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
    """Return distinct values present in at least two of the three arrays.

    Args:
        nums1: First integer array.
        nums2: Second integer array.
        nums3: Third integer array.

    Returns:
        List of distinct values appearing in at least two arrays.
    """
    s1, s2, s3 = set(nums1), set(nums2), set(nums3)
    return list((s1 & s2) | (s1 & s3) | (s2 & s3))
