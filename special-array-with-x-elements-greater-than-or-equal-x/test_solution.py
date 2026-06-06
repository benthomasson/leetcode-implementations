"""Tests for Special Array with X Elements Greater Than or Equal X."""

import sys
sys.path.insert(0, "../implementer")

from solution import specialArray


def test_example1():
    assert specialArray([3, 5]) == 2

def test_example2():
    assert specialArray([0, 0]) == -1

def test_example3():
    assert specialArray([0, 4, 3, 0, 4]) == 3

def test_single_zero():
    assert specialArray([0]) == -1

def test_single_one():
    assert specialArray([1]) == 1

def test_all_same_no_special():
    assert specialArray([1, 1, 1]) == -1

def test_all_large():
    assert specialArray([100, 100, 100]) == 3

def test_ascending_no_special():
    assert specialArray([0, 1, 2, 3, 4]) == -1

def test_single_large():
    assert specialArray([1000]) == 1
