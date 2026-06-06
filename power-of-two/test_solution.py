"""Tests for Power of Two solution."""

from solution import is_power_of_two


def test_powers_of_two():
    assert is_power_of_two(1) is True
    assert is_power_of_two(2) is True
    assert is_power_of_two(4) is True
    assert is_power_of_two(16) is True
    assert is_power_of_two(1024) is True
    assert is_power_of_two(2**30) is True


def test_not_powers_of_two():
    assert is_power_of_two(0) is False
    assert is_power_of_two(3) is False
    assert is_power_of_two(5) is False
    assert is_power_of_two(6) is False


def test_negative_numbers():
    assert is_power_of_two(-1) is False
    assert is_power_of_two(-2) is False
    assert is_power_of_two(-(2**31)) is False


def test_edge_cases():
    assert is_power_of_two(2**31 - 1) is False


if __name__ == "__main__":
    test_powers_of_two()
    test_not_powers_of_two()
    test_negative_numbers()
    test_edge_cases()
    print("All tests passed!")
