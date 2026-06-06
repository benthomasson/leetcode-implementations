import pytest
from solution import find_final_value


def test_example_1():
    """Test first LeetCode example: multiple doublings."""
    assert find_final_value([5, 3, 6, 1, 12], 3) == 24


def test_example_2():
    """Test second LeetCode example: no doubling."""
    assert find_final_value([2, 7, 9], 4) == 4


def test_single_element_match():
    """Test single element array where original is found."""
    assert find_final_value([8], 8) == 16


def test_single_element_no_match():
    """Test single element array where original is not found."""
    assert find_final_value([5], 3) == 3


def test_no_doubling():
    """Test when original is not in nums at all."""
    assert find_final_value([10, 20, 30], 5) == 5


def test_long_doubling_chain():
    """Test multiple consecutive doublings."""
    assert find_final_value([1, 2, 4, 8, 16, 32], 1) == 64


def test_duplicates_in_nums():
    """Test array with duplicate values."""
    assert find_final_value([5, 5, 10, 10, 20], 5) == 40


def test_original_at_minimum():
    """Test with original = 1 (minimum constraint value)."""
    assert find_final_value([1, 2, 4], 1) == 8


def test_large_values():
    """Test with larger values approaching constraint limits."""
    assert find_final_value([100, 200, 400, 800], 100) == 1600


def test_larger_array():
    """Test with larger array and multiple doublings."""
    nums = list(range(1, 101)) + [128, 256, 512]
    assert find_final_value(nums, 64) == 1024
