"""Tests for Binary Watch solution."""

from solution import readBinaryWatch


def test_zero():
    assert readBinaryWatch(0) == ["0:00"]


def test_one():
    result = readBinaryWatch(1)
    assert sorted(result) == sorted(
        ["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"]
    )


def test_two():
    result = readBinaryWatch(2)
    assert "0:03" in result
    assert "1:01" in result
    assert "3:00" in result
    assert len(result) == 44


def test_high_values_empty():
    assert readBinaryWatch(9) == []
    assert readBinaryWatch(10) == []


def test_no_invalid_times():
    for n in range(11):
        for time in readBinaryWatch(n):
            h, m = time.split(":")
            assert 0 <= int(h) <= 11
            assert 0 <= int(m) <= 59
            assert len(m) == 2
            assert h == str(int(h))  # no leading zero on hour
