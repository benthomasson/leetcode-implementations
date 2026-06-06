"""Valid Word Abbreviation - LeetCode"""

import unittest


def validWordAbbreviation(word: str, abbr: str) -> bool:
    """Check if abbr is a valid abbreviation of word.

    Args:
        word: The original word (lowercase letters only).
        abbr: The abbreviation to validate (lowercase letters and digits).

    Returns:
        True if abbr is a valid abbreviation of word.
    """
    i, j = 0, 0
    while i < len(word) and j < len(abbr):
        if abbr[j].isdigit():
            if abbr[j] == '0':  # leading zero
                return False
            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            i += num
        else:
            if word[i] != abbr[j]:
                return False
            i += 1
            j += 1
    return i == len(word) and j == len(abbr)


class TestValidWordAbbreviation(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(validWordAbbreviation("internationalization", "i12iz4n"))

    def test_example2(self):
        self.assertFalse(validWordAbbreviation("apple", "a2e"))

    def test_full_numeric(self):
        self.assertTrue(validWordAbbreviation("substitution", "12"))

    def test_no_abbreviation(self):
        self.assertTrue(validWordAbbreviation("word", "word"))

    def test_leading_zero(self):
        self.assertFalse(validWordAbbreviation("substitution", "s010n"))

    def test_zero_replacement(self):
        self.assertFalse(validWordAbbreviation("ab", "a0b"))

    def test_leading_zero_standalone(self):
        self.assertFalse(validWordAbbreviation("a", "01"))

    def test_number_exceeds_length(self):
        self.assertFalse(validWordAbbreviation("hi", "9"))

    def test_single_char_match(self):
        self.assertTrue(validWordAbbreviation("a", "1"))

    def test_single_char_letter(self):
        self.assertTrue(validWordAbbreviation("a", "a"))

    def test_single_char_mismatch(self):
        self.assertFalse(validWordAbbreviation("a", "b"))

    def test_abbr_too_short(self):
        self.assertFalse(validWordAbbreviation("apple", "a2"))

    def test_abbr_too_long(self):
        self.assertFalse(validWordAbbreviation("ab", "a1b"))

    def test_multiple_numbers(self):
        self.assertTrue(validWordAbbreviation("substitution", "sub4u4"))

    def test_adjacent_numbers_invalid(self):
        # "s55n" would mean s + skip 5 + skip 5 + n = adjacent replacements
        # But as a matching problem, s + skip 55 + n would be 57 chars — doesn't match 12-char word
        self.assertFalse(validWordAbbreviation("substitution", "s55n"))


if __name__ == "__main__":
    unittest.main()
