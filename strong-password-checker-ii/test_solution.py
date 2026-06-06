import unittest
import sys
sys.path.insert(0, "../implementer")
from solution import Solution


class TestStrongPasswordChecker(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- LeetCode examples ---
    def test_example1_strong(self):
        self.assertTrue(self.s.strong_password_checker_ii("IloveLe3tcode! "))

    def test_example2_no_digit_and_adjacent_dupes(self):
        self.assertFalse(self.s.strong_password_checker_ii("Me+You--IsMyDream "))

    def test_example3_too_short(self):
        self.assertFalse(self.s.strong_password_checker_ii("1aB! "))

    # --- Edge cases ---
    def test_exactly_8_chars_all_criteria(self):
        self.assertTrue(self.s.strong_password_checker_ii("aB1!xyzW"))

    def test_7_chars_fails_length(self):
        self.assertFalse(self.s.strong_password_checker_ii("aB1!xyz"))

    def test_adjacent_duplicates(self):
        self.assertFalse(self.s.strong_password_checker_ii("aabcDeF1!"))

    def test_no_special_char(self):
        self.assertFalse(self.s.strong_password_checker_ii("abcDefg1A"))

    def test_non_adjacent_repeats_ok(self):
        self.assertTrue(self.s.strong_password_checker_ii("aB1!aB1!"))

    def test_single_char(self):
        self.assertFalse(self.s.strong_password_checker_ii("a"))

    def test_all_special_chars_present(self):
        # Has space as special char, all criteria met, no adjacent dupes
        self.assertTrue(self.s.strong_password_checker_ii("aB1! xYz9"))


if __name__ == "__main__":
    unittest.main()
