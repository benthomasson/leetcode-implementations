from typing import List


def sumEvenGrandparent(arr: List[int]) -> List[int]:
    """Transform array by adjusting local minima/maxima until stable.

    Args:
        arr: Initial array of integers.

    Returns:
        The final stable array after all transformations.
    """
    arr = arr[:]
    while True:
        new = arr[:]
        for i in range(1, len(arr) - 1):
            if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                new[i] += 1
            elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                new[i] -= 1
        if new == arr:
            return arr
        arr = new
