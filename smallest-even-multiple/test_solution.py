"""Tests for the smallest_multiple function."""

import pytest

from solution import smallest_multiple


class TestSmallestMultiple:
    """Tests for smallest_multiple."""

    def test_odd_input(self):
        assert smallest_multiple(5) == 10

    def test_even_input(self):
        assert smallest_multiple(6) == 6

    def test_n_is_1(self):
        assert smallest_multiple(1) == 2

    def test_n_is_2(self):
        assert smallest_multiple(2) == 2

    def test_upper_bound_even(self):
        assert smallest_multiple(150) == 150

    def test_upper_bound_odd(self):
        assert smallest_multiple(149) == 298

    def test_small_odd(self):
        assert smallest_multiple(3) == 6

    def test_small_even(self):
        assert smallest_multiple(4) == 4

    def test_mid_odd(self):
        assert smallest_multiple(99) == 198

    def test_mid_even(self):
        assert smallest_multiple(100) == 100

    def test_invalid_zero(self):
        with pytest.raises(ValueError):
            smallest_multiple(0)

    def test_invalid_negative(self):
        with pytest.raises(ValueError):
            smallest_multiple(-1)

    def test_invalid_above_range(self):
        with pytest.raises(ValueError):
            smallest_multiple(151)

    def test_invalid_type(self):
        with pytest.raises(ValueError):
            smallest_multiple(5.5)  # type: ignore[arg-type]
