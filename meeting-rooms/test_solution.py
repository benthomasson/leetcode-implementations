"""Tests for Meeting Rooms solution."""

from solution import can_attend_meetings


def test_example1_overlapping():
    assert can_attend_meetings([[0, 30], [5, 10], [15, 20]]) is False


def test_example2_no_overlap():
    assert can_attend_meetings([[7, 10], [2, 4]]) is True


def test_empty():
    assert can_attend_meetings([]) is True


def test_single_meeting():
    assert can_attend_meetings([[1, 5]]) is True


def test_adjacent_no_overlap():
    assert can_attend_meetings([[1, 5], [5, 10]]) is True


def test_nested_interval():
    assert can_attend_meetings([[1, 10], [3, 5]]) is False


def test_all_overlapping():
    assert can_attend_meetings([[1, 5], [2, 6], [3, 7]]) is False


def test_multiple_no_overlap():
    assert can_attend_meetings([[1, 2], [3, 4], [5, 6], [7, 8]]) is True


def test_overlap_at_boundary():
    assert can_attend_meetings([[1, 6], [5, 10]]) is False
