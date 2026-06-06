"""Tests for boxCategory."""

from solution import boxCategory


def test_example1_heavy():
    assert boxCategory(1000, 35, 700, 300) == "Heavy "


def test_example2_neither():
    assert boxCategory(200, 50, 800, 50) == "Neither "


def test_both():
    assert boxCategory(10000, 100, 100, 100) == "Both "


def test_bulky_by_dimension():
    assert boxCategory(10000, 1, 1, 1) == "Bulky "


def test_bulky_by_volume():
    assert boxCategory(1000, 1000, 1000, 1) == "Bulky "


def test_bulky_volume_exact_threshold():
    # 10^9 exactly -> bulky
    assert boxCategory(1000, 1000, 1000, 99) == "Bulky "


def test_heavy_exact_threshold():
    assert boxCategory(1, 1, 1, 100) == "Heavy "


def test_not_heavy_below_threshold():
    assert boxCategory(1, 1, 1, 99) == "Neither "


def test_not_bulky_below_dimension_threshold():
    assert boxCategory(9999, 9999, 9999, 1) == "Bulky "  # volume exceeds 10^9


def test_dimension_exact_threshold():
    assert boxCategory(10000, 1, 1, 1) == "Bulky "


def test_min_values():
    assert boxCategory(1, 1, 1, 1) == "Neither "


def test_both_all_max():
    assert boxCategory(100000, 100000, 100000, 1000) == "Both "
