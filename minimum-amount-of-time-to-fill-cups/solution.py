def min_seconds(amount: list[int]) -> int:
    """Return minimum seconds to fill all cups.

    Args:
        amount: List of 3 integers representing cups needed for each water type.

    Returns:
        Minimum number of seconds to fill all cups.
    """
    return max(max(amount), (sum(amount) + 1) // 2)
