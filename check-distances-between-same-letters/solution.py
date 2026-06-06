"""Check distances between same letters."""


def well_spaced_string(s: str, distance: list[int]) -> bool:
    """Check if s is a well-spaced string according to distance array.

    Args:
        s: String where each lowercase letter appears exactly twice.
        distance: Length-26 array of required distances between letter pairs.

    Returns:
        True if every letter's pair distance matches the required distance.
    """
    first_seen: dict[str, int] = {}
    for i, c in enumerate(s):
        if c in first_seen:
            if i - first_seen[c] - 1 != distance[ord(c) - ord("a")]:
                return False
        else:
            first_seen[c] = i
    return True
