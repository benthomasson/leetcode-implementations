"""Subtract the Product and Sum of Digits of an Integer."""


def subtract_product_and_sum(n: int) -> int:
    """Return the difference between the product and sum of digits of n.

    Args:
        n: A positive integer (1 <= n <= 10^5).

    Returns:
        Product of digits minus sum of digits.
    """
    if n == 0:
        return 0
    product = 1
    total = 0
    while n > 0:
        digit = n % 10
        product *= digit
        total += digit
        n //= 10
    return product - total
