import unittest
from solution import Solution


class TestTotalMoney(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.totalMoney(4), 10)

    def test_example2(self):
        self.assertEqual(self.s.totalMoney(10), 37)

    def test_example3(self):
        self.assertEqual(self.s.totalMoney(20), 96)

    def test_single_day(self):
        self.assertEqual(self.s.totalMoney(1), 1)

    def test_full_week(self):
        self.assertEqual(self.s.totalMoney(7), 28)

    def test_two_weeks(self):
        self.assertEqual(self.s.totalMoney(14), 63)

    def test_max(self):
        # n=1000: verify against brute force
        total = 0
        for i in range(1000):
            total += (i // 7) + (i % 7) + 1
        self.assertEqual(self.s.totalMoney(1000), total)


if __name__ == "__main__":
    unittest.main()
