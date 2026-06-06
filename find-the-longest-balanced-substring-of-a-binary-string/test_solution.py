"""Tests for longestBalancedSubstring."""

import sys
sys.path.insert(0, "../implementer")

import pytest
from solution import longestBalancedSubstring


@pytest.mark.parametrize("s, expected", [
    # LeetCode examples
    ("01000111", 6),
    ("00111", 4),
    ("111", 0),
    # Edge cases
    ("0", 0),
    ("1", 0),
    ("01", 2),
    ("10", 0),
    # All same
    ("0000", 0),
    # Alternating
    ("0101", 2),
    # Multiple groups
    ("0011001111", 4),
])
def test_longest_balanced(s, expected):
    assert longestBalancedSubstring(s) == expected
