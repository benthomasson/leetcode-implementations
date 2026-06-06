"""Tests for decode-the-message solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import valid_selections


class TestDecodeMessage(unittest.TestCase):
    """Tests for valid_selections (decode the message)."""

    def test_example1(self):
        self.assertEqual(
            valid_selections(
                "the quick brown fox jumps over the lazy dog",
                "vkbs bs t suepuv",
            ),
            "this is a secret",
        )

    def test_example2(self):
        self.assertEqual(
            valid_selections(
                "eljuxhpwnyrdgtqkviszcfmabo",
                "zwx hnfx lqantp mnoeius ycgk vcnjrdb",
            ),
            "the five boxing wizards jump quickly",
        )

    def test_spaces_preserved(self):
        key = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(valid_selections(key, "   "), "   ")

    def test_identity_key(self):
        """When key is a-z in order, message decodes to itself."""
        key = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(valid_selections(key, "hello world"), "hello world")

    def test_single_char(self):
        key = "bacdefghijklmnopqrstuvwxyz"
        self.assertEqual(valid_selections(key, "b"), "a")
        self.assertEqual(valid_selections(key, "a"), "b")

    def test_trailing_space(self):
        self.assertEqual(
            valid_selections(
                "the quick brown fox jumps over the lazy dog ",
                "vkbs bs t suepuv ",
            ),
            "this is a secret ",
        )

    def test_key_with_duplicates_and_spaces(self):
        """Duplicates and spaces in key should be skipped."""
        key = "aaabbbcccthe quick brown fox jumps over the lazy dog"
        # first unique letters: a, b, c, t, h, e, ...
        # a->a, so decoding 'a' should give 'a'
        self.assertEqual(valid_selections(key, "a"), "a")
        # b->b
        self.assertEqual(valid_selections(key, "b"), "b")
        # t is the 4th unique letter -> maps to 'd'
        self.assertEqual(valid_selections(key, "t"), "d")

    def test_reversed_key(self):
        """Key is z-a, so z->a, y->b, ..., a->z."""
        key = "zyxwvutsrqponmlkjihgfedcba"
        self.assertEqual(valid_selections(key, "z"), "a")
        self.assertEqual(valid_selections(key, "a"), "z")
        self.assertEqual(valid_selections(key, "z a"), "a z")

    def test_empty_message(self):
        key = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(valid_selections(key, ""), "")

    def test_full_alphabet_message(self):
        """Decode every letter with reversed key."""
        key = "zyxwvutsrqponmlkjihgfedcba"
        msg = "zyxwvutsrqponmlkjihgfedcba"
        expected = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(valid_selections(key, msg), expected)


if __name__ == "__main__":
    unittest.main()
