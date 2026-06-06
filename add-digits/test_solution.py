import unittest
from solution import Solution


class TestAddDigits(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_zero(self):
        self.assertEqual(self.s.addDigits(0), 0)

    def test_single_digits(self):
        for i in range(1, 10):
            self.assertEqual(self.s.addDigits(i), i)

    def test_example(self):
        self.assertEqual(self.s.addDigits(38), 2)

    def test_multiples_of_nine(self):
        self.assertEqual(self.s.addDigits(9), 9)
        self.assertEqual(self.s.addDigits(18), 9)
        self.assertEqual(self.s.addDigits(81), 9)

    def test_large(self):
        self.assertEqual(self.s.addDigits(2**31 - 1), 1)  # 2147483647 -> 1

    def test_misc(self):
        self.assertEqual(self.s.addDigits(10), 1)
        self.assertEqual(self.s.addDigits(99), 9)
        self.assertEqual(self.s.addDigits(123), 6)


if __name__ == "__main__":
    unittest.main()
