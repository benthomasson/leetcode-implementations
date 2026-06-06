"""Tests for smallest_index."""

from solution import smallest_index


def test_example1_all_match():
    assert smallest_index([0, 1, 2]) == 0


def test_example2_single_match():
    assert smallest_index([4, 3, 2, 1]) == 2


def test_example3_no_match():
    assert smallest_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == -1


def test_single_element_match():
    assert smallest_index([0]) == 0


def test_single_element_no_match():
    assert smallest_index([1]) == -1


def test_mod10_wrap():
    # Index 9: 9 % 10 == 9 == nums[9], so smallest match is 9
    nums = [9] * 12 + [2]
    assert smallest_index(nums) == 9


def test_max_length_match_at_9():
    assert smallest_index([9] * 100) == 9


def test_last_index_match():
    # Only index 99 matches: 99 % 10 == 9
    nums = [3] * 100
    nums[3] = 0   # prevent match at i=3 (3%10==3)
    nums[13] = 0  # prevent match at i=13
    nums[23] = 0  # prevent match at i=23
    nums[33] = 0  # prevent match at i=33
    nums[43] = 0  # prevent match at i=43
    nums[53] = 0  # prevent match at i=53
    nums[63] = 0  # prevent match at i=63
    nums[73] = 0  # prevent match at i=73
    nums[83] = 0  # prevent match at i=83
    nums[93] = 0  # prevent match at i=93
    nums[99] = 9
    assert smallest_index(nums) == 99
