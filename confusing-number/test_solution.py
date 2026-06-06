import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


# Examples from problem
def test_example_6(sol):
    assert sol.confusingNumber(6) is True

def test_example_89(sol):
    assert sol.confusingNumber(89) is True

def test_example_11(sol):
    assert sol.confusingNumber(11) is False


# Edge cases
def test_zero(sol):
    assert sol.confusingNumber(0) is False

def test_single_invalid_digits(sol):
    for d in [2, 3, 4, 5, 7]:
        assert sol.confusingNumber(d) is False

def test_single_symmetric_digits(sol):
    for d in [0, 1, 8]:
        assert sol.confusingNumber(d) is False

def test_single_asymmetric_digits(sol):
    assert sol.confusingNumber(6) is True
    assert sol.confusingNumber(9) is True


# Multi-digit
def test_leading_zeros_after_rotation(sol):
    # 8000 rotates to 0008 = 8, which != 8000
    assert sol.confusingNumber(8000) is True

def test_contains_invalid_digit(sol):
    assert sol.confusingNumber(25) is False
    assert sol.confusingNumber(123) is False

def test_symmetric_multi(sol):
    # 96 -> 96 (rotated: 6->9, 9->6, reversed = 69... wait)
    # 69: rotate each digit -> 6->9, 9->6 => "96", reversed => 69. 69==69? No wait.
    # Let's think: 96 digit extraction: 6 then 9. rotated built as 9, then 9*10+6=96. 96==96 -> False
    assert sol.confusingNumber(96) is False

def test_large_confusing(sol):
    # 1000000009: digits 9,0,0,0,0,0,0,0,0,1 -> rotated built as 6, 60, 600,..., 6000000001
    assert sol.confusingNumber(1000000009) is True
