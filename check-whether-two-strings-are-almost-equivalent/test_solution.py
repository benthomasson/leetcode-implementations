import unittest
from solution import Solution


class TestCheckAlmostEquivalent(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertFalse(self.s.checkAlmostEquivalent("aaaa", "bccb"))

    def test_example2(self):
        self.assertTrue(self.s.checkAlmostEquivalent("abcdeef", "abaaacc"))

    def test_example3(self):
        self.assertTrue(self.s.checkAlmostEquivalent("cccddabba", "babababab"))

    def test_identical(self):
        self.assertTrue(self.s.checkAlmostEquivalent("abc", "abc"))

    def test_single_char(self):
        self.assertTrue(self.s.checkAlmostEquivalent("a", "b"))

    def test_boundary_diff_3(self):
        self.assertTrue(self.s.checkAlmostEquivalent("aaab", "b", ))

    def test_boundary_diff_4(self):
        self.assertFalse(self.s.checkAlmostEquivalent("aaaa", "b"))

    def test_all_same_letter(self):
        self.assertTrue(self.s.checkAlmostEquivalent("aaa", "aaa"))


if __name__ == "__main__":
    unittest.main()
