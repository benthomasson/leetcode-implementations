"""Remove Element - LeetCode Problem."""


def removeElement(nums: list[int], val: int) -> int:
    """Remove all occurrences of val in nums in-place.

    Args:
        nums: Integer array to modify in-place.
        val: Value to remove.

    Returns:
        Number of elements not equal to val.
    """
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
