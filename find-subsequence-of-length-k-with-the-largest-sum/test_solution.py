"""Tests for Find Subsequence of Length K With the Largest Sum."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import count_patterns_in_word


def _is_valid_subsequence(nums, result, k):
    """Check result is a valid length-k subsequence with max sum."""
    assert len(result) == k
    # Check it's a valid subsequence (elements appear in order)
    it = iter(nums)
    for val in result:
        while True:
            n = next(it)
            if n == val:
                break
    # Check sum is maximal: sort nums descending, top-k sum should match
    expected_sum = sum(sorted(nums, reverse=True)[:k])
    assert sum(result) == expected_sum


# --- Examples from problem ---

def test_example_1():
    assert count_patterns_in_word([2, 1, 3, 3], 2) == [3, 3]


def test_example_2():
    assert count_patterns_in_word([-1, -2, 3, 4], 3) == [-1, 3, 4]


def test_example_3():
    result = count_patterns_in_word([3, 4, 3, 3], 2)
    _is_valid_subsequence([3, 4, 3, 3], result, 2)


# --- Edge cases ---

def test_k_equals_n():
    nums = [5, 3, 1]
    assert count_patterns_in_word(nums, 3) == [5, 3, 1]


def test_k_equals_1():
    assert count_patterns_in_word([1, 5, 2, 4], 1) == [5]


def test_single_element():
    assert count_patterns_in_word([42], 1) == [42]


def test_all_identical():
    assert count_patterns_in_word([7, 7, 7, 7], 2) == [7, 7]


def test_all_negative():
    result = count_patterns_in_word([-5, -1, -3, -2], 2)
    _is_valid_subsequence([-5, -1, -3, -2], result, 2)


def test_mixed_positive_negative():
    result = count_patterns_in_word([-10, 20, -30, 40, -50], 3)
    _is_valid_subsequence([-10, 20, -30, 40, -50], result, 3)


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v'])
