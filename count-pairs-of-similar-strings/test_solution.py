from solution import count_similar_pairs


def test_example_1():
    assert count_similar_pairs(["aba", "aabb", "abcd", "bac", "aabc"]) == 2


def test_example_2():
    assert count_similar_pairs(["aabb", "ab", "ba"]) == 3


def test_example_3():
    assert count_similar_pairs(["nba", "cba", "dba"]) == 0


def test_single_word():
    assert count_similar_pairs(["abc"]) == 0


def test_all_identical():
    assert count_similar_pairs(["a", "a", "a"]) == 3


def test_all_unique():
    assert count_similar_pairs(["a", "b", "c"]) == 0


def test_single_char_words():
    assert count_similar_pairs(["a", "aa", "aaa", "b"]) == 3
