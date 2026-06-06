from solution import uncommon_from_sentences


def test_example1():
    assert sorted(uncommon_from_sentences("this apple is sweet", "this apple is sour")) == ["sour", "sweet"]


def test_example2():
    assert uncommon_from_sentences("apple apple", "banana") == ["banana"]


def test_single_words_both_same():
    assert uncommon_from_sentences("a", "a") == []


def test_single_words_different():
    assert sorted(uncommon_from_sentences("a", "b")) == ["a", "b"]


def test_all_unique():
    assert sorted(uncommon_from_sentences("a b", "c d")) == ["a", "b", "c", "d"]


def test_duplicate_within_one_sentence():
    assert uncommon_from_sentences("a a", "b b") == []


def test_identical_sentences():
    assert uncommon_from_sentences("x y z", "x y z") == []


def test_no_overlap():
    assert sorted(uncommon_from_sentences("cat", "dog")) == ["cat", "dog"]


def test_word_appears_three_times():
    # "a" appears twice in s1 + once in s2 = 3 times total, not uncommon
    assert uncommon_from_sentences("a a", "a") == []
