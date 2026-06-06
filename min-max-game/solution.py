from typing import List


def min_steps(nums: List[int]) -> int:
    """Return the last number remaining after repeatedly applying min/max pairing.

    Args:
        nums: Integer array whose length is a power of 2.

    Returns:
        The single remaining element.
    """
    while len(nums) > 1:
        new_nums = []
        for i in range(len(nums) // 2):
            a, b = nums[2 * i], nums[2 * i + 1]
            new_nums.append(min(a, b) if i % 2 == 0 else max(a, b))
        nums = new_nums
    return nums[0]
