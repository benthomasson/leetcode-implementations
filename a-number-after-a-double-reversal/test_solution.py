import unittest
from solution import Solution


class TestMinOperations(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_zero(self):
        self.assertTrue(self.s.minOperations(0))

    def test_single_digits(self):
        for n in range(1, 10):
            self.assertTrue(self.s.minOperations(n))

    def test_no_trailing_zeros(self):
        self.assertTrue(self.s.minOperations(526))
        self.assertTrue(self.s.minOperations(123))

    def test_trailing_zeros(self):
        self.assertFalse(self.s.minOperations(1800))
        self.assertFalse(self.s.minOperations(10))
        self.assertFalse(self.s.minOperations(100))

    def test_boundary(self):
        self.assertTrue(self.s.minOperations(1))
        self.assertFalse(self.s.minOperations(1000000))


if __name__ == "__main__":
    unittest.main()
