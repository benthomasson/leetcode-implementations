"""Tests for Goal Parser Interpretation."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import num_ways


def test_example_1():
    assert num_ways("G()(al)") == "Goal"


def test_example_2():
    assert num_ways("G()()()()(al)") == "Gooooal"


def test_example_3():
    assert num_ways("(al)G(al)()()G") == "alGalooG"


def test_single_g():
    assert num_ways("G") == "G"


def test_single_parens():
    assert num_ways("()") == "o"


def test_single_al():
    assert num_ways("(al)") == "al"


def test_all_g():
    assert num_ways("GGG") == "GGG"


def test_all_parens():
    assert num_ways("()()()") == "ooo"


def test_all_al():
    assert num_ways("(al)(al)(al)") == "alalal"


def test_mixed():
    assert num_ways("G()G(al)G()") == "GoGalGo"
