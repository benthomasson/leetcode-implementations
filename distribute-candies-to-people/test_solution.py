"""Tests for distribute_candies."""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from solution import distribute_candies


def test_example_1():
    assert distribute_candies(7, 4) == [1, 2, 3, 1]


def test_example_2():
    assert distribute_candies(10, 3) == [5, 2, 3]


def test_single_person():
    assert distribute_candies(10, 1) == [10]


def test_single_candy():
    assert distribute_candies(1, 4) == [1, 0, 0, 0]


def test_exact_exhaustion():
    # 1+2+3 = 6, exactly enough for one full round with 3 people
    assert distribute_candies(6, 3) == [1, 2, 3]


def test_large_candies():
    result = distribute_candies(10**9, 1000)
    assert sum(result) == 10**9
    assert len(result) == 1000


def test_sum_preserved():
    for candies, n in [(7, 4), (10, 3), (100, 5), (1, 1)]:
        result = distribute_candies(candies, n)
        assert sum(result) == candies
        assert len(result) == n


def test_two_full_rounds():
    # 1+2+3 + 4+5+6 = 21, two full rounds with 3 people
    assert distribute_candies(21, 3) == [1 + 4, 2 + 5, 3 + 6]


def test_partial_last_gift():
    # 11 candies, 3 people:
    # give 1→p0, 2→p1, 3→p2, 4→p0 (remaining=1), 5→p1 gets min(5,1)=1
    assert distribute_candies(11, 3) == [5, 3, 3]
