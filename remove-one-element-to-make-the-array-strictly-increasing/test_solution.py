"""Tests for canBeIncreasing."""

import pytest
from solution import canBeIncreasing


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Provided examples
        ([1, 2, 10, 5, 7], True),
        ([2, 3, 1, 2], False),
        ([1, 1, 1], False),
        # Already strictly increasing
        ([1, 2, 3, 4, 5], True),
        # Length 2 — always True
        ([2, 1], True),
        ([1, 2], True),
        # Remove first element
        ([5, 1, 2, 3], True),
        # Remove last element
        ([1, 2, 3, 2], True),
        # All equal
        ([3, 3, 3, 3], False),
        # Descending
        ([5, 4, 3, 2, 1], False),
        # Two separate violations
        ([1, 3, 2, 4, 3], False),
        # Duplicate at start
        ([1, 1, 2, 3], True),
        # Duplicate at end
        ([1, 2, 3, 3], True),
        # Remove middle resolves
        ([1, 4, 2, 3], True),
    ],
)
def test_canBeIncreasing(nums, expected):
    assert canBeIncreasing(nums) == expected
