"""Tests for Happy Number solution."""

from solution import get_next, is_happy


class TestGetNext:
    def test_single_digit(self):
        assert get_next(7) == 49

    def test_multi_digit(self):
        assert get_next(19) == 1 + 81  # 82

    def test_one(self):
        assert get_next(1) == 1

    def test_with_zeros(self):
        assert get_next(100) == 1


class TestIsHappy:
    def test_example_happy_19(self):
        assert is_happy(19) is True

    def test_example_unhappy_2(self):
        assert is_happy(2) is False

    def test_one(self):
        assert is_happy(1) is True

    def test_happy_7(self):
        assert is_happy(7) is True

    def test_unhappy_4(self):
        assert is_happy(4) is False

    def test_large_input(self):
        assert is_happy(2**31 - 1) is not None  # should terminate

    def test_all_single_digits(self):
        happy = {1, 7}
        for d in range(1, 10):
            assert is_happy(d) == (d in happy)
