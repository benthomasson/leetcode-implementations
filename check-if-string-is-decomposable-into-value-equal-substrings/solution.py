from itertools import groupby


def num_different_integers(s: str) -> bool:
    """Check if string can be decomposed into value-equal substrings with exactly one length-2.

    Args:
        s: A digit string to decompose.

    Returns:
        True if decomposable into consecutive value-equal substrings where
        exactly one has length 2 and the rest have length 3.
    """
    twos = 0
    for _, group in groupby(s):
        remainder = sum(1 for _ in group) % 3
        if remainder == 1:
            return False
        if remainder == 2:
            twos += 1
    return twos == 1
