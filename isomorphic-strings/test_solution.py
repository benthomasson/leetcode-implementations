"""Tests for isomorphic strings solution."""

from solution import is_isomorphic


def test_example_1():
    assert is_isomorphic("egg", "add") is True


def test_example_2():
    assert is_isomorphic("foo", "bar") is False


def test_example_3():
    assert is_isomorphic("paper", "title") is True


def test_single_char():
    assert is_isomorphic("a", "b") is True


def test_self_mapping():
    assert is_isomorphic("abc", "abc") is True


def test_forward_not_reverse():
    # "ab" -> "aa": two different chars map to same target
    assert is_isomorphic("ab", "aa") is False


def test_reverse_not_forward():
    # "aa" -> "ab": same char must map to two different targets
    assert is_isomorphic("aa", "ab") is False


def test_all_same():
    assert is_isomorphic("aaaa", "bbbb") is True


def test_empty():
    assert is_isomorphic("", "") is True


def test_ascii_range():
    s = "".join(chr(i) for i in range(128))
    t = "".join(chr(127 - i) for i in range(128))
    assert is_isomorphic(s, t) is True
