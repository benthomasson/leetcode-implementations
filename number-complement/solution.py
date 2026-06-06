"""Number Complement - LeetCode 476."""


def find_complement(num: int) -> int:
    """Return the complement of num by flipping all bits.

    Args:
        num: Integer where 1 <= num < 2^31.

    Returns:
        The bitwise complement of num (no leading zeros).
    """
    mask = (1 << num.bit_length()) - 1
    return num ^ mask
