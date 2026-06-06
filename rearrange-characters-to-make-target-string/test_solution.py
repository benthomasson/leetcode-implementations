from solution import maxNumberOfCopies


def test_example_1():
    assert maxNumberOfCopies("ilovecodingonleetcode", "code") == 2


def test_example_2():
    assert maxNumberOfCopies("abcba", "abc") == 1


def test_example_3():
    assert maxNumberOfCopies("abbaccaddaeea", "aaaaa") == 1


def test_missing_char():
    assert maxNumberOfCopies("abc", "z") == 0


def test_single_char():
    assert maxNumberOfCopies("aaa", "a") == 3


def test_exact_match():
    assert maxNumberOfCopies("abc", "abc") == 1


def test_repeated_target_char():
    assert maxNumberOfCopies("aabbcc", "aab") == 1


def test_large_multiple():
    assert maxNumberOfCopies("a" * 100, "a") == 100
