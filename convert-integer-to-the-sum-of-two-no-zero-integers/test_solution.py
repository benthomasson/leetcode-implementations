"""Tests for no_zero_integers."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import no_zero_integers


def _has_no_zero(x: int) -> bool:
    return x > 0 and '0' not in str(x)


def _validate(n: int) -> None:
    result = no_zero_integers(n)
    a, b = result
    assert a + b == n, f"Sum {a}+{b}={a+b} != {n}"
    assert _has_no_zero(a), f"{a} contains 0"
    assert _has_no_zero(b), f"{b} contains 0"


def test_example_1():
    _validate(2)

def test_example_2():
    _validate(11)

def test_n_10():
    _validate(10)

def test_n_100():
    _validate(100)

def test_n_1000():
    _validate(1000)

def test_n_10000():
    _validate(10000)

def test_n_1111():
    _validate(1111)

def test_all_range():
    for n in range(2, 10001):
        _validate(n)
