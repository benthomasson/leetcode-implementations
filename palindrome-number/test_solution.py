"""Tests for palindrome number solution."""

import pytest
from solution import is_palindrome


@pytest.mark.parametrize("x, expected", [
    # Single digits
    (0, True),
    (5, True),
    (9, True),
    # Multi-digit palindromes (odd length)
    (121, True),
    (12321, True),
    # Multi-digit palindromes (even length)
    (1221, True),
    (11, True),
    # Negative numbers
    (-121, False),
    (-1, False),
    # Trailing zeros
    (10, False),
    (100, False),
    # Non-palindromes
    (123, False),
    (12, False),
    # Large values
    (2**31 - 1, False),  # 2147483647
    (1000000001, True),
])
def test_is_palindrome(x, expected):
    assert is_palindrome(x) == expected
