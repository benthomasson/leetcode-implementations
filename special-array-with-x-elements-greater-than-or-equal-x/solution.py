"""Special Array with X Elements Greater Than or Equal X."""


def specialArray(nums: list[int]) -> int:
    """Find x such that exactly x numbers in nums are >= x, or return -1."""
    nums.sort(reverse=True)
    n = len(nums)
    for x in range(1, n + 1):
        if nums[x - 1] >= x and (x == n or nums[x] < x):
            return x
    return -1
