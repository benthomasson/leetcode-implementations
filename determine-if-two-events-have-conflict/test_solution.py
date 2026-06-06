"""Tests for has_event_conflict."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import has_event_conflict


def test_example1_boundary_overlap():
    assert has_event_conflict(["01:15", "02:00"], ["02:00", "03:00"]) is True

def test_example2_partial_overlap():
    assert has_event_conflict(["01:00", "02:00"], ["01:20", "03:00"]) is True

def test_example3_no_overlap():
    assert has_event_conflict(["10:00", "11:00"], ["14:00", "15:00"]) is False

def test_identical_events():
    assert has_event_conflict(["09:00", "10:00"], ["09:00", "10:00"]) is True

def test_adjacent_no_overlap():
    """Event1 ends at 10:00, event2 starts at 10:01 — no conflict."""
    assert has_event_conflict(["08:00", "10:00"], ["10:01", "12:00"]) is False

def test_event2_before_event1():
    assert has_event_conflict(["14:00", "15:00"], ["10:00", "11:00"]) is False

def test_one_contains_other():
    assert has_event_conflict(["08:00", "18:00"], ["10:00", "12:00"]) is True

def test_single_minute_events_same():
    assert has_event_conflict(["12:00", "12:00"], ["12:00", "12:00"]) is True

def test_single_minute_events_different():
    assert has_event_conflict(["12:00", "12:00"], ["12:01", "12:01"]) is False

def test_midnight_boundaries():
    assert has_event_conflict(["00:00", "23:59"], ["12:00", "13:00"]) is True
