"""Tests for license_key_formatting."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import license_key_formatting


class TestLicenseKeyFormatting(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(license_key_formatting("5F3Z-2e-9-w", 4), "5F3Z-2E9W")

    def test_example2(self):
        self.assertEqual(license_key_formatting("2-5g-3-J", 2), "2-5G-3J")

    def test_single_char(self):
        self.assertEqual(license_key_formatting("a", 1), "A")

    def test_no_dashes(self):
        self.assertEqual(license_key_formatting("ABCDEF", 3), "ABC-DEF")

    def test_all_dashes_except_one(self):
        self.assertEqual(license_key_formatting("--a--", 2), "A")

    def test_k_equals_length(self):
        self.assertEqual(license_key_formatting("ab-cd", 4), "ABCD")

    def test_k_is_one(self):
        self.assertEqual(license_key_formatting("abc", 1), "A-B-C")

    def test_first_group_shorter(self):
        self.assertEqual(license_key_formatting("abcde", 2), "A-BC-DE")

    def test_digits_only(self):
        self.assertEqual(license_key_formatting("1-2-3-4-5", 3), "12-345")

    def test_single_char_with_dashes(self):
        self.assertEqual(license_key_formatting("-a-", 5), "A")


if __name__ == "__main__":
    unittest.main()
