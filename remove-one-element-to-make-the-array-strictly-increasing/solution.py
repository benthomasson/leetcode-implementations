"""Remove One Element to Make the Array Strictly Increasing."""


def canBeIncreasing(nums: list[int]) -> bool:
    """Return True if removing exactly one element can make nums strictly increasing.

    Args:
        nums: List of integers (length >= 2).

    Returns:
        True if the array can be made strictly increasing by removing one element.
    """

    def is_increasing_skip(skip: int) -> bool:
        prev = -1
        for i, v in enumerate(nums):
            if i == skip:
                continue
            if v <= prev:
                return False
            prev = v
        return True

    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            return is_increasing_skip(i) or is_increasing_skip(i - 1)

    # Already strictly increasing — removing any one element still works.
    return True
