import unittest
from solution import Solution


class TestStrobogrammatic(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_examples(self):
        self.assertTrue(self.s.isStrobogrammatic("69"))
        self.assertTrue(self.s.isStrobogrammatic("88"))
        self.assertFalse(self.s.isStrobogrammatic("962"))

    def test_single_digits(self):
        for d in "018":
            self.assertTrue(self.s.isStrobogrammatic(d))
        for d in "2345679":
            self.assertFalse(self.s.isStrobogrammatic(d))

    def test_even_length(self):
        self.assertTrue(self.s.isStrobogrammatic("1001"))
        self.assertFalse(self.s.isStrobogrammatic("9669"))
        self.assertFalse(self.s.isStrobogrammatic("1221"))

    def test_odd_length_middle(self):
        self.assertTrue(self.s.isStrobogrammatic("101"))
        self.assertTrue(self.s.isStrobogrammatic("808"))
        self.assertTrue(self.s.isStrobogrammatic("609"))
        self.assertTrue(self.s.isStrobogrammatic("619"))
        self.assertFalse(self.s.isStrobogrammatic("123"))
        self.assertFalse(self.s.isStrobogrammatic("629"))

    def test_edge(self):
        self.assertTrue(self.s.isStrobogrammatic("0"))
        self.assertTrue(self.s.isStrobogrammatic("1"))
        self.assertTrue(self.s.isStrobogrammatic("96"))
        self.assertFalse(self.s.isStrobogrammatic("95"))


if __name__ == "__main__":
    unittest.main()
