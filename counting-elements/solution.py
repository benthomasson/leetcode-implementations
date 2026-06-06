def count_elements(arr: list[int]) -> int:
    """Count elements x where x + 1 is also in arr.

    Args:
        arr: List of integers.

    Returns:
        Count of elements whose successor exists in the array.
    """
    s = set(arr)
    return sum(1 for x in arr if x + 1 in s)
