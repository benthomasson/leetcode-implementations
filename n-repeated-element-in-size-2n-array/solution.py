"""N-Repeated Element in Size 2N Array."""


def isLongPressedName(nums: list[int]) -> int:
    """Find the element repeated n times in a size 2n array.

    Args:
        nums: Integer array of length 2n containing n+1 unique elements,
            where one element is repeated n times.

    Returns:
        The element that is repeated n times.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
