"""Tests for backspace string compare."""

import unittest

from solution import backspaceCompare


class TestBackspaceCompare(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(backspaceCompare("ab#c", "ad#c"))

    def test_example2(self):
        self.assertTrue(backspaceCompare("ab##", "c#d#"))

    def test_example3(self):
        self.assertFalse(backspaceCompare("a#c", "b"))

    def test_no_backspaces(self):
        self.assertTrue(backspaceCompare("abc", "abc"))
        self.assertFalse(backspaceCompare("abc", "abd"))

    def test_all_backspaced(self):
        self.assertTrue(backspaceCompare("a#", "b#"))
        self.assertTrue(backspaceCompare("ab##", "cd##"))

    def test_backspace_on_empty(self):
        self.assertTrue(backspaceCompare("#a", "a"))
        self.assertTrue(backspaceCompare("##a", "a"))

    def test_consecutive_backspaces(self):
        self.assertTrue(backspaceCompare("abc###", ""))
        self.assertTrue(backspaceCompare("abc###d", "d"))

    def test_single_chars(self):
        self.assertTrue(backspaceCompare("a", "a"))
        self.assertFalse(backspaceCompare("a", "b"))

    def test_empty_results(self):
        self.assertTrue(backspaceCompare("#", "#"))
        self.assertTrue(backspaceCompare("###", "#"))

    def test_trailing_backspaces(self):
        self.assertTrue(backspaceCompare("ab#c#d", "ad#d"))


if __name__ == "__main__":
    unittest.main()
