"""Tests for assign cookies solution."""

import pytest
from solution import find_content_children


@pytest.mark.parametrize("g, s, expected", [
    # LeetCode examples
    ([1, 2, 3], [1, 1], 1),
    ([1, 2], [1, 2, 3], 2),
    # Empty cookies
    ([1, 2], [], 0),
    # All satisfied
    ([1, 2, 3], [3, 2, 1], 3),
    # None satisfied
    ([3, 4, 5], [1, 1, 1], 0),
    # Single elements
    ([1], [1], 1),
    ([2], [1], 0),
    # Duplicates
    ([1, 1, 1], [1, 1, 1], 3),
    ([2, 2], [1, 1], 0),
    # Large values near 2^31 - 1
    ([2**31 - 1], [2**31 - 1], 1),
    ([2**31 - 1], [2**31 - 2], 0),
    # More cookies than children
    ([1], [1, 2, 3, 4], 1),
    # More children than cookies
    ([1, 2, 3, 4], [2], 1),
])
def test_find_content_children(g, s, expected):
    assert find_content_children(g, s) == expected
