"""Tests for detectCapitalUse."""

import unittest
from solution import detectCapitalUse


class TestDetectCapitalUse(unittest.TestCase):

    # Valid cases
    def test_all_caps(self):
        assert detectCapitalUse("USA") is True

    def test_all_lower(self):
        assert detectCapitalUse("leetcode") is True

    def test_title_case(self):
        assert detectCapitalUse("Google") is True

    # Invalid cases
    def test_flag(self):
        assert detectCapitalUse("FlaG") is False

    def test_lower_then_upper(self):
        assert detectCapitalUse("mL") is False

    def test_mixed_middle(self):
        assert detectCapitalUse("fLaG") is False

    # Single character
    def test_single_upper(self):
        assert detectCapitalUse("A") is True

    def test_single_lower(self):
        assert detectCapitalUse("a") is True

    # Two-letter edge cases
    def test_two_upper(self):
        assert detectCapitalUse("AB") is True

    def test_upper_lower(self):
        assert detectCapitalUse("Ab") is True

    def test_lower_upper(self):
        assert detectCapitalUse("aB") is False

    def test_two_lower(self):
        assert detectCapitalUse("ab") is True


if __name__ == "__main__":
    unittest.main()
