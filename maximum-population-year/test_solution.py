from solution import maxAliveYear


def test_example1():
    assert maxAliveYear([[1993, 1999], [2000, 2010]]) == 1993


def test_example2():
    assert maxAliveYear([[1950, 1961], [1960, 1971], [1970, 1981]]) == 1960


def test_single_person():
    assert maxAliveYear([[2000, 2001]]) == 2000


def test_all_same_years():
    assert maxAliveYear([[1990, 2000], [1990, 2000], [1990, 2000]]) == 1990


def test_adjacent_ranges():
    assert maxAliveYear([[1950, 1960], [1960, 1970]]) == 1950


def test_full_overlap():
    assert maxAliveYear([[1950, 2000], [1960, 1970]]) == 1960


def test_boundary_years():
    assert maxAliveYear([[1950, 1951], [2049, 2050]]) == 1950


def test_tie_earliest_wins():
    assert maxAliveYear([[1980, 1990], [2000, 2010]]) == 1980
