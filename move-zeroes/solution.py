"""Move Zeroes - LeetCode Problem."""


def moveZeroes(nums: list[int]) -> None:
    """Move all zeros to end of array in-place, preserving non-zero order.

    Args:
        nums: List of integers to modify in-place.
    """
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1
