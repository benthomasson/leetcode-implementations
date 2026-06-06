"""Tests for Greatest Common Divisor of Strings."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import gcdOfStrings


class TestGcdOfStrings(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(gcdOfStrings("ABCABC", "ABC"), "ABC")

    def test_example2(self):
        self.assertEqual(gcdOfStrings("ABABAB", "ABAB"), "AB")

    def test_example3(self):
        self.assertEqual(gcdOfStrings("LEET", "CODE"), "")

    def test_identical_strings(self):
        self.assertEqual(gcdOfStrings("ABC", "ABC"), "ABC")

    def test_single_char_repeated(self):
        self.assertEqual(gcdOfStrings("AAA", "A"), "A")

    def test_no_common_divisor(self):
        self.assertEqual(gcdOfStrings("A", "B"), "")

    def test_both_single_same(self):
        self.assertEqual(gcdOfStrings("A", "A"), "A")

    def test_longer_pattern_gcd(self):
        # gcd(9,6)=3, pattern "ABC"
        self.assertEqual(gcdOfStrings("ABCABCABC", "ABCABC"), "ABC")

    def test_no_divisor_despite_shared_prefix(self):
        self.assertEqual(gcdOfStrings("ABCDEF", "ABC"), "")

    def test_swapped_order(self):
        # Result should be the same regardless of argument order
        self.assertEqual(gcdOfStrings("ABC", "ABCABC"), "ABC")


if __name__ == "__main__":
    unittest.main()
