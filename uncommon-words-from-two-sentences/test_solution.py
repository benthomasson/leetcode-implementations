from solution import k_similarity


def test_example1():
    assert sorted(k_similarity("this apple is sweet", "this apple is sour")) == ["sour", "sweet"]


def test_example2():
    assert k_similarity("apple apple", "banana") == ["banana"]


def test_single_words_both_same():
    assert k_similarity("a", "a") == []


def test_single_words_different():
    assert sorted(k_similarity("a", "b")) == ["a", "b"]


def test_all_unique():
    assert sorted(k_similarity("a b", "c d")) == ["a", "b", "c", "d"]


def test_duplicate_within_one_sentence():
    assert k_similarity("a a", "b b") == []


def test_identical_sentences():
    assert k_similarity("x y z", "x y z") == []


def test_no_overlap():
    assert sorted(k_similarity("cat", "dog")) == ["cat", "dog"]


def test_word_appears_three_times():
    # "a" appears twice in s1 + once in s2 = 3 times total, not uncommon
    assert k_similarity("a a", "a") == []
