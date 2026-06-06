"""Next Greater Element I - LeetCode 496."""


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    """Find the next greater element for each nums1[i] in nums2.

    Args:
        nums1: Subset of nums2 to query.
        nums2: Source array to search for next greater elements.

    Returns:
        List where ans[i] is the next greater element of nums1[i] in nums2, or -1.
    """
    next_greater: dict[int, int] = {}
    stack: list[int] = []

    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)

    return [next_greater.get(num, -1) for num in nums1]
