import unittest
from solution import Solution


class TestSum(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_positive(self):
        self.assertEqual(self.s.sum(12, 5), 17)

    def test_negative(self):
        self.assertEqual(self.s.sum(-10, -5), -15)

    def test_mixed(self):
        self.assertEqual(self.s.sum(-10, 4), -6)

    def test_zeros(self):
        self.assertEqual(self.s.sum(0, 0), 0)

    def test_zero_with_positive(self):
        self.assertEqual(self.s.sum(0, 50), 50)

    def test_boundaries(self):
        self.assertEqual(self.s.sum(-100, -100), -200)
        self.assertEqual(self.s.sum(100, 100), 200)
        self.assertEqual(self.s.sum(-100, 100), 0)


if __name__ == "__main__":
    unittest.main()
