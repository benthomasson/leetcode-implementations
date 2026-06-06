"""Tests for difference_between_element_and_digit_sum."""

from solution import difference_between_element_and_digit_sum


def test_example_1():
    assert difference_between_element_and_digit_sum([1, 15, 6, 3]) == 9


def test_example_2():
    assert difference_between_element_and_digit_sum([1, 2, 3, 4]) == 0


def test_single_digit_elements():
    assert difference_between_element_and_digit_sum([9]) == 0


def test_all_max_values():
    # 2000: element_sum = 2000, digit_sum = 2. diff = 1998 per element.
    assert difference_between_element_and_digit_sum([2000] * 5) == 5 * 1998


def test_single_element_multi_digit():
    # 123: digits 1+2+3=6, diff=117
    assert difference_between_element_and_digit_sum([123]) == 117


def test_large_array():
    nums = list(range(1, 2001))
    element_sum = sum(nums)
    digit_sum = sum(int(d) for n in nums for d in str(n))
    assert difference_between_element_and_digit_sum(nums) == abs(element_sum - digit_sum)
