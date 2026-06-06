from solution import isPowerOfFour


def test_powers_of_four():
    for exp in range(16):  # 4^0 through 4^15
        assert isPowerOfFour(4 ** exp) is True, f"4^{exp} should be True"


def test_examples():
    assert isPowerOfFour(16) is True
    assert isPowerOfFour(5) is False
    assert isPowerOfFour(1) is True


def test_non_powers():
    for n in [0, 2, 3, 5, 6, 7, 8, 9, 12, 15, 32, 100]:
        assert isPowerOfFour(n) is False, f"{n} should be False"


def test_negatives():
    for n in [-1, -4, -16, -(2**31)]:
        assert isPowerOfFour(n) is False, f"{n} should be False"


def test_large_boundary():
    assert isPowerOfFour(2**31 - 1) is False
    assert isPowerOfFour(4**15) is True  # 1073741824
