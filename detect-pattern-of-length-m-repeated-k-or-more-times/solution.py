from typing import List


def is_prefix_of_word(arr: List[int], m: int, k: int) -> bool:
    """Check if any subarray of length m repeats k or more times consecutively.

    Args:
        arr: Array of positive integers.
        m: Length of the pattern to find.
        k: Minimum number of consecutive repetitions.

    Returns:
        True if such a repeating pattern exists, False otherwise.
    """
    n = len(arr)
    for i in range(n - m * k + 1):
        pattern = arr[i:i + m]
        if all(arr[i + j * m:i + j * m + m] == pattern for j in range(1, k)):
            return True
    return False
