import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def test_example1(sol):
    result = sol.convert_temperature(36.50)
    assert result == pytest.approx([309.65, 97.70], abs=1e-5)


def test_example2(sol):
    result = sol.convert_temperature(122.11)
    assert result == pytest.approx([395.26, 251.798], abs=1e-5)


def test_zero(sol):
    result = sol.convert_temperature(0)
    assert result == pytest.approx([273.15, 32.00], abs=1e-5)


def test_max(sol):
    result = sol.convert_temperature(1000)
    assert result == pytest.approx([1273.15, 1832.00], abs=1e-5)


def test_boiling_point(sol):
    result = sol.convert_temperature(100.00)
    assert result == pytest.approx([373.15, 212.00], abs=1e-5)


def test_return_type(sol):
    result = sol.convert_temperature(50.0)
    assert isinstance(result, list)
    assert len(result) == 2


def test_small_decimal(sol):
    result = sol.convert_temperature(0.01)
    assert result == pytest.approx([273.16, 32.018], abs=1e-5)
