"""Element Appearing More Than 25% in Sorted Array."""


def find_special_integer(arr: list[int]) -> int:
    """Find the element appearing more than 25% of the time in a sorted array.

    Args:
        arr: Sorted integer array with exactly one element appearing >25%.

    Returns:
        The integer that appears more than 25% of the time.
    """
    quarter = len(arr) // 4
    for i in range(len(arr) - quarter):
        if arr[i] == arr[i + quarter]:
            return arr[i]
    return arr[-1]
