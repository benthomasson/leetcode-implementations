def pillowHolder(n: int, time: int) -> int:
    """Return the index of the person holding the pillow after `time` seconds.

    Args:
        n: Number of people in line (1-indexed).
        time: Number of seconds elapsed.

    Returns:
        1-indexed position of the pillow holder.
    """
    if n == 1:
        return 1
    cycle = n - 1
    full_passes = time // cycle
    remainder = time % cycle
    if full_passes % 2 == 0:
        return 1 + remainder
    else:
        return n - remainder
