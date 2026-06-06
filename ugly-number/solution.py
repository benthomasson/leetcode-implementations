def is_ugly(n: int) -> bool:
    """Determine if n is an ugly number (prime factors limited to 2, 3, 5).

    Args:
        n: Integer to check.

    Returns:
        True if n is an ugly number, False otherwise.
    """
    if n <= 0:
        return False
    for p in (2, 3, 5):
        while n % p == 0:
            n //= p
    return n == 1
