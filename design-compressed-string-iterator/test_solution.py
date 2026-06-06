"""Tests for Design Compressed String Iterator."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import StringIterator


class TestStringIterator(unittest.TestCase):
    """Tests for the StringIterator class."""

    def test_leetcode_example(self):
        """Exact example from the problem statement."""
        it = StringIterator("L1e2t1C1o1d1e1")
        self.assertEqual(it.next(), "L")
        self.assertEqual(it.next(), "e")
        self.assertEqual(it.next(), "e")
        self.assertEqual(it.next(), "t")
        self.assertEqual(it.next(), "C")
        self.assertEqual(it.next(), "o")
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), "d")
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), "e")
        self.assertFalse(it.hasNext())

    def test_single_char_single_count(self):
        """Minimal input: one character with count 1."""
        it = StringIterator("a1")
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), "a")
        self.assertFalse(it.hasNext())

    def test_exhausted_returns_space(self):
        """After all chars consumed, next() returns ' '."""
        it = StringIterator("x1")
        it.next()
        self.assertEqual(it.next(), " ")
        self.assertEqual(it.next(), " ")

    def test_large_count(self):
        """Count up to 10^9 should work without expanding."""
        it = StringIterator("a1000000000")
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), "a")
        self.assertTrue(it.hasNext())

    def test_multi_digit_counts(self):
        """Multi-digit counts parse correctly."""
        it = StringIterator("a12b3")
        for _ in range(12):
            self.assertEqual(it.next(), "a")
        for _ in range(3):
            self.assertEqual(it.next(), "b")
        self.assertFalse(it.hasNext())
        self.assertEqual(it.next(), " ")

    def test_mixed_case(self):
        """Upper and lower case letters handled correctly."""
        it = StringIterator("A1b2C3")
        self.assertEqual(it.next(), "A")
        self.assertEqual(it.next(), "b")
        self.assertEqual(it.next(), "b")
        self.assertEqual(it.next(), "C")
        self.assertEqual(it.next(), "C")
        self.assertEqual(it.next(), "C")
        self.assertFalse(it.hasNext())

    def test_has_next_idempotent(self):
        """Calling hasNext() multiple times doesn't consume characters."""
        it = StringIterator("z2")
        self.assertTrue(it.hasNext())
        self.assertTrue(it.hasNext())
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), "z")
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), "z")
        self.assertFalse(it.hasNext())
        self.assertFalse(it.hasNext())

    def test_consecutive_same_letter_different_groups(self):
        """Same letter appearing in separate groups."""
        it = StringIterator("a2a3")
        for _ in range(2):
            self.assertEqual(it.next(), "a")
        for _ in range(3):
            self.assertEqual(it.next(), "a")
        self.assertFalse(it.hasNext())


if __name__ == "__main__":
    unittest.main()
