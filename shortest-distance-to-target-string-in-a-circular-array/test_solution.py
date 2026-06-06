"""Tests for shortest_distance."""

from solution import shortest_distance


def test_example1():
    assert shortest_distance(["hello", "i", "am", "leetcode", "hello"], "hello", 1) == 1


def test_example2():
    assert shortest_distance(["a", "b", "leetcode"], "leetcode", 0) == 1


def test_example3():
    assert shortest_distance(["i", "eat", "leetcode"], "ate", 0) == -1


def test_target_at_start():
    assert shortest_distance(["a", "b", "c"], "a", 0) == 0


def test_single_element_match():
    assert shortest_distance(["x"], "x", 0) == 0


def test_single_element_no_match():
    assert shortest_distance(["x"], "y", 0) == -1


def test_wraparound_closer():
    assert shortest_distance(["a", "b", "c", "d", "a"], "a", 3) == 1


def test_start_at_last_index():
    assert shortest_distance(["a", "b", "c"], "a", 2) == 1


def test_multiple_occurrences():
    assert shortest_distance(["a", "b", "a", "b", "a"], "a", 1) == 1
