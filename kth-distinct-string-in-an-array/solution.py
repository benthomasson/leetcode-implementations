from collections import Counter


def kth_distinct(arr: list[str], k: int) -> str:
    """Return the kth distinct string in arr, or "" if fewer than k exist.

    Args:
        arr: List of strings.
        k: 1-indexed position of the desired distinct string.

    Returns:
        The kth distinct string, or "" if not enough distinct strings.
    """
    counts = Counter(arr)
    for s in arr:
        if counts[s] == 1:
            k -= 1
            if k == 0:
                return s
    return ""
