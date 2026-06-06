from solution import kth_distinct


def test_example_1():
    assert kth_distinct(["d", "b", "c", "b", "c", "a"], 2) == "a"


def test_example_2():
    assert kth_distinct(["aaa", "aa", "a"], 1) == "aaa"


def test_example_3():
    assert kth_distinct(["a", "b", "a"], 3) == ""


def test_all_distinct():
    assert kth_distinct(["x", "y", "z"], 3) == "z"


def test_no_distinct():
    assert kth_distinct(["a", "a", "b", "b"], 1) == ""


def test_single_element():
    assert kth_distinct(["only"], 1) == "only"


def test_k_equals_distinct_count():
    assert kth_distinct(["a", "b", "b", "c"], 2) == "c"


def test_k_exceeds_distinct_count():
    assert kth_distinct(["a", "b", "b", "c"], 3) == ""


def test_first_element_distinct():
    assert kth_distinct(["a", "b", "b"], 1) == "a"
