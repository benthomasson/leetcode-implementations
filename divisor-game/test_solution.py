import unittest
from solution import Solution


class TestDivisorGame(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_n1(self):
        self.assertFalse(self.s.divisorGame(1))

    def test_n2(self):
        self.assertTrue(self.s.divisorGame(2))

    def test_n3(self):
        self.assertFalse(self.s.divisorGame(3))

    def test_n4(self):
        self.assertTrue(self.s.divisorGame(4))

    def test_large_even(self):
        self.assertTrue(self.s.divisorGame(1000))

    def test_large_odd(self):
        self.assertFalse(self.s.divisorGame(999))

    def test_alias(self):
        self.assertTrue(self.s.mincostTickets(2))
        self.assertFalse(self.s.mincostTickets(1))


if __name__ == "__main__":
    unittest.main()
