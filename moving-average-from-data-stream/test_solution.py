import pytest
from solution import MovingAverage


def test_example():
    ma = MovingAverage(3)
    assert ma.next(1) == pytest.approx(1.0)
    assert ma.next(10) == pytest.approx(5.5)
    assert ma.next(3) == pytest.approx(4.66667, abs=1e-4)
    assert ma.next(5) == pytest.approx(6.0)


def test_window_size_one():
    ma = MovingAverage(1)
    assert ma.next(5) == pytest.approx(5.0)
    assert ma.next(-3) == pytest.approx(-3.0)
    assert ma.next(0) == pytest.approx(0.0)


def test_negative_values():
    ma = MovingAverage(2)
    assert ma.next(-10) == pytest.approx(-10.0)
    assert ma.next(-20) == pytest.approx(-15.0)
    assert ma.next(30) == pytest.approx(5.0)


def test_large_window_not_full():
    ma = MovingAverage(1000)
    assert ma.next(100) == pytest.approx(100.0)
    assert ma.next(200) == pytest.approx(150.0)


def test_many_calls():
    ma = MovingAverage(3)
    for i in range(10000):
        result = ma.next(i)
    # Last 3 values: 9997, 9998, 9999
    assert result == pytest.approx(9998.0)
