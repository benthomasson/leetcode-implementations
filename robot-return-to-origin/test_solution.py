"""Tests for Robot Return to Origin."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import judgeCircle


def test_example1_ud():
    assert judgeCircle("UD") is True

def test_example2_ll():
    assert judgeCircle("LL") is False

def test_single_move():
    assert judgeCircle("R") is False

def test_all_four_directions_balanced():
    assert judgeCircle("UDLR") is True

def test_repeated_same_direction():
    assert judgeCircle("UUUU") is False

def test_lr_balanced_ud_not():
    assert judgeCircle("LRUD") is True

def test_lr_unbalanced():
    assert judgeCircle("LLRR") is True

def test_complex_balanced():
    assert judgeCircle("LLRRUURLDD") is True  # L:3 R:3 U:2 D:2

def test_long_alternating():
    assert judgeCircle("UD" * 10000) is True

def test_long_unbalanced():
    assert judgeCircle("U" * 20000) is False
