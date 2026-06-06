import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import Solution
import unittest


class TestPangram(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1_pangram(self):
        assert self.s.min_operations("thequickbrownfoxjumpsoverthelazydog") is True

    def test_example2_not_pangram(self):
        assert self.s.min_operations("leetcode") is False

    def test_exact_alphabet(self):
        assert self.s.min_operations("abcdefghijklmnopqrstuvwxyz") is True

    def test_single_char(self):
        assert self.s.min_operations("a") is False

    def test_missing_one_letter(self):
        # missing 'z'
        assert self.s.min_operations("abcdefghijklmnopqrstuvwxy") is False

    def test_repeated_alphabet(self):
        assert self.s.min_operations("abcdefghijklmnopqrstuvwxyz" * 10) is True

    def test_all_same_char(self):
        assert self.s.min_operations("a" * 1000) is False


if __name__ == "__main__":
    unittest.main()
