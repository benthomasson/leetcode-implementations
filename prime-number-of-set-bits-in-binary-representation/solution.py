"""Prime Number of Set Bits in Binary Representation."""


def is_prime(n: int) -> bool:
    """Check if n is prime. Only needs to handle 0-20."""
    return n in {2, 3, 5, 7, 11, 13, 17, 19}


def countPrimeSetBits(left: int, right: int) -> int:
    """Count numbers in [left, right] with a prime number of set bits.

    Args:
        left: Start of range (inclusive).
        right: End of range (inclusive).

    Returns:
        Count of numbers with prime set-bit count.
    """
    return sum(is_prime(bin(n).count('1')) for n in range(left, right + 1))
