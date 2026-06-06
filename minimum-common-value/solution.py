"""Minimum Common Value - LeetCode Problem"""


def min_common_number(nums1: list[int], nums2: list[int]) -> int:
    """Find the minimum integer common to both sorted arrays.

    Args:
        nums1: Sorted array of integers in non-decreasing order.
        nums2: Sorted array of integers in non-decreasing order.

    Returns:
        The minimum common integer, or -1 if none exists.
    """
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            return nums1[i]
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return -1
