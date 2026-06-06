import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def test_basic_swap(sol):
    assert sol.buddyStrings("ab", "ba") is True


def test_identical_no_duplicates(sol):
    assert sol.buddyStrings("ab", "ab") is False


def test_identical_with_duplicates(sol):
    assert sol.buddyStrings("aa", "aa") is True


def test_different_lengths(sol):
    assert sol.buddyStrings("ab", "abc") is False


def test_single_char(sol):
    assert sol.buddyStrings("a", "a") is False


def test_all_same_chars(sol):
    assert sol.buddyStrings("aaa", "aaa") is True


def test_three_diffs(sol):
    assert sol.buddyStrings("abcd", "badc") is False


def test_two_diffs_no_cross_match(sol):
    assert sol.buddyStrings("abcd", "abdc") is True


def test_long_identical_with_dup(sol):
    assert sol.buddyStrings("abcaa", "abcaa") is True


def test_long_identical_no_dup(sol):
    assert sol.buddyStrings("abcde", "abcde") is False


def test_swap_at_ends(sol):
    assert sol.buddyStrings("abcdef", "fbcdea") is True


def test_two_diffs_wrong_cross(sol):
    assert sol.buddyStrings("ab", "cd") is False
