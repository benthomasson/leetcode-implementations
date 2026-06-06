import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import Solution

import pytest

sol = Solution()


def test_example_1():
    sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    assert sol.mostWordsFound(sentences) == 6


def test_example_2():
    sentences = ["please wait", "continue to fight", "continue to win"]
    assert sol.mostWordsFound(sentences) == 3


def test_single_sentence():
    assert sol.mostWordsFound(["hello world"]) == 2


def test_single_word():
    assert sol.mostWordsFound(["hello"]) == 1


def test_all_single_words():
    assert sol.mostWordsFound(["a", "b", "c"]) == 1


def test_all_same_length():
    assert sol.mostWordsFound(["a b c", "d e f", "g h i"]) == 3


def test_max_at_beginning():
    assert sol.mostWordsFound(["a b c d", "a b", "a"]) == 4


def test_max_at_end():
    assert sol.mostWordsFound(["a", "a b", "a b c d"]) == 4
