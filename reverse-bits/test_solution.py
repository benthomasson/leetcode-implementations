"""Tests for reverse_bits."""

from solution import reverse_bits


def test_example1():
    assert reverse_bits(0b00000010100101000001111010011100) == 964176192


def test_example2():
    assert reverse_bits(0b11111111111111111111111111111101) == 3221225471


def test_zero():
    assert reverse_bits(0) == 0


def test_all_ones():
    assert reverse_bits(0xFFFFFFFF) == 0xFFFFFFFF


def test_one():
    assert reverse_bits(1) == (1 << 31)


def test_high_bit():
    assert reverse_bits(1 << 31) == 1


def test_alternating_bits():
    assert reverse_bits(0xAAAAAAAA) == 0x55555555


def test_inverse_alternating():
    assert reverse_bits(0x55555555) == 0xAAAAAAAA
