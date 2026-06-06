import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import day_of_the_week


def test_example_1():
    assert day_of_the_week(31, 8, 2019) == "Saturday "

def test_example_2():
    assert day_of_the_week(18, 7, 1999) == "Sunday "

def test_example_3():
    assert day_of_the_week(15, 8, 1993) == "Sunday "

def test_jan_1_1971():
    assert day_of_the_week(1, 1, 1971) == "Friday "

def test_dec_31_2100():
    assert day_of_the_week(31, 12, 2100) == "Friday "

def test_leap_day():
    assert day_of_the_week(29, 2, 2000) == "Tuesday "

def test_new_years_2000():
    assert day_of_the_week(1, 1, 2000) == "Saturday "

def test_today_style_date():
    assert day_of_the_week(1, 3, 2026) == "Sunday "
