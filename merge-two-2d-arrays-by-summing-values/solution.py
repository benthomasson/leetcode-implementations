"""Merge Two 2D Arrays by Summing Values."""


def merge_nums(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    """Merge two sorted 2D arrays by summing values with matching ids.

    Args:
        nums1: Sorted array of [id, value] pairs with unique ids.
        nums2: Sorted array of [id, value] pairs with unique ids.

    Returns:
        Merged array sorted by id, with values summed for matching ids.
    """
    result = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i][0] < nums2[j][0]:
            result.append(nums1[i])
            i += 1
        elif nums1[i][0] > nums2[j][0]:
            result.append(nums2[j])
            j += 1
        else:
            result.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
            i += 1
            j += 1
    while i < len(nums1):
        result.append(nums1[i])
        i += 1
    while j < len(nums2):
        result.append(nums2[j])
        j += 1
    return result
