"""Tests for Best Time to Buy and Sell Stock."""

from solution import maxProfit


def test_example_1():
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 5


def test_example_2():
    assert maxProfit([7, 6, 4, 3, 1]) == 0


def test_single_element():
    assert maxProfit([5]) == 0


def test_two_elements_profit():
    assert maxProfit([1, 5]) == 4


def test_two_elements_no_profit():
    assert maxProfit([5, 1]) == 0


def test_all_same():
    assert maxProfit([3, 3, 3, 3]) == 0


def test_monotonically_increasing():
    assert maxProfit([1, 2, 3, 4, 5]) == 4


def test_monotonically_decreasing():
    assert maxProfit([5, 4, 3, 2, 1]) == 0


def test_min_at_end():
    assert maxProfit([3, 5, 1]) == 2


def test_large_input():
    prices = list(range(100000, 0, -1))  # worst case: decreasing
    assert maxProfit(prices) == 0
