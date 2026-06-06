from solution import is_ugly


def test_ugly_numbers():
    for n in (1, 2, 3, 4, 5, 6, 8, 10, 15, 30):
        assert is_ugly(n) is True, f"{n} should be ugly"


def test_not_ugly():
    for n in (7, 11, 14, 26):
        assert is_ugly(n) is False, f"{n} should not be ugly"


def test_zero_and_negative():
    assert is_ugly(0) is False
    assert is_ugly(-1) is False
    assert is_ugly(-6) is False
