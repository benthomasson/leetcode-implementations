"""Tests for sort_names_by_height."""

from solution import sort_names_by_height


def test_example_1():
    assert sort_names_by_height(["Mary", "John", "Emma"], [180, 165, 170]) == ["Mary", "Emma", "John"]


def test_example_2():
    assert sort_names_by_height(["Alice", "Bob", "Bob"], [155, 185, 150]) == ["Bob", "Alice", "Bob"]


def test_single_person():
    assert sort_names_by_height(["Alice"], [100]) == ["Alice"]


def test_already_sorted_descending():
    assert sort_names_by_height(["A", "B", "C"], [300, 200, 100]) == ["A", "B", "C"]


def test_reverse_sorted():
    assert sort_names_by_height(["A", "B", "C"], [100, 200, 300]) == ["C", "B", "A"]


def test_duplicate_names_different_heights():
    assert sort_names_by_height(["Bob", "Bob", "Bob"], [50, 150, 100]) == ["Bob", "Bob", "Bob"]
