import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import Solution, make_string_sorted
import unittest


class TestAreOccurrencesEqual(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertTrue(self.sol.areOccurrencesEqual("abacbc"))

    def test_example2(self):
        self.assertFalse(self.sol.areOccurrencesEqual("aaabb"))

    def test_single_char(self):
        self.assertTrue(self.sol.areOccurrencesEqual("a"))

    def test_all_same_char(self):
        self.assertTrue(self.sol.areOccurrencesEqual("aaaa"))

    def test_two_chars_equal(self):
        self.assertTrue(self.sol.areOccurrencesEqual("aabb"))

    def test_two_chars_unequal(self):
        self.assertFalse(self.sol.areOccurrencesEqual("aab"))

    def test_full_alphabet_equal(self):
        self.assertTrue(self.sol.areOccurrencesEqual("abcdefghijklmnopqrstuvwxyz"))

    def test_full_alphabet_one_extra(self):
        self.assertFalse(self.sol.areOccurrencesEqual("abcdefghijklmnopqrstuvwxyza"))

    def test_make_string_sorted_alias(self):
        self.assertTrue(make_string_sorted("aabb"))
        self.assertFalse(make_string_sorted("aab"))


if __name__ == '__main__':
    unittest.main()
