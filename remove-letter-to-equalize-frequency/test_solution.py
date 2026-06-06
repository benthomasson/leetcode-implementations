import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import can_equal_frequency
import unittest


class TestCanEqualFrequency(unittest.TestCase):
    def test_example1_abcc(self):
        self.assertTrue(can_equal_frequency("abcc"))

    def test_example2_aazz(self):
        self.assertFalse(can_equal_frequency("aazz"))

    def test_two_distinct_chars(self):
        self.assertTrue(can_equal_frequency("ab"))

    def test_all_same(self):
        self.assertTrue(can_equal_frequency("aaaa"))

    def test_all_unique(self):
        self.assertTrue(can_equal_frequency("abcde"))

    def test_aabb_false(self):
        self.assertFalse(can_equal_frequency("aabb"))

    def test_remove_singleton(self):
        # remove 'a' leaves "bbcc" with equal freq
        self.assertTrue(can_equal_frequency("abbcc"))

    def test_single_repeated_pair(self):
        self.assertTrue(can_equal_frequency("aa"))

    def test_aaab(self):
        # remove 'b' leaves "aaa"
        self.assertTrue(can_equal_frequency("aaab"))


if __name__ == "__main__":
    unittest.main()
