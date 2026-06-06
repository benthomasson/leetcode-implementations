"""Tests for Can Place Flowers."""

from solution import canPlaceFlowers


def test_example1():
    assert canPlaceFlowers([1, 0, 0, 0, 1], 1) is True


def test_example2():
    assert canPlaceFlowers([1, 0, 0, 0, 1], 2) is False


def test_n_zero():
    assert canPlaceFlowers([1, 0, 1], 0) is True


def test_single_empty():
    assert canPlaceFlowers([0], 1) is True


def test_single_planted():
    assert canPlaceFlowers([1], 1) is False


def test_all_zeros():
    assert canPlaceFlowers([0, 0, 0, 0, 0], 3) is True


def test_all_zeros_too_many():
    assert canPlaceFlowers([0, 0, 0, 0, 0], 4) is False


def test_already_full():
    assert canPlaceFlowers([1, 0, 1, 0, 1], 1) is False


def test_plant_at_edges():
    assert canPlaceFlowers([0, 0, 1, 0, 0], 2) is True


def test_single_zero_n_zero():
    assert canPlaceFlowers([0], 0) is True
