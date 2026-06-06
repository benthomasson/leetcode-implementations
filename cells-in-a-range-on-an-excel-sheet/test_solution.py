"""Tests for cells-in-a-range-on-an-excel-sheet solution."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import cell_range


def test_example1():
    assert cell_range("K1:L2") == ["K1", "K2", "L1", "L2"]


def test_example2():
    assert cell_range("A1:F1") == ["A1", "B1", "C1", "D1", "E1", "F1"]


def test_single_cell():
    assert cell_range("A1:A1") == ["A1"]


def test_single_column():
    assert cell_range("B1:B5") == ["B1", "B2", "B3", "B4", "B5"]


def test_single_row():
    assert cell_range("A3:D3") == ["A3", "B3", "C3", "D3"]


def test_full_range():
    result = cell_range("A1:Z9")
    assert len(result) == 26 * 9
    assert result[0] == "A1"
    assert result[-1] == "Z9"


def test_last_cell():
    assert cell_range("Z9:Z9") == ["Z9"]


def test_ordering():
    result = cell_range("A1:B3")
    assert result == ["A1", "A2", "A3", "B1", "B2", "B3"]


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
