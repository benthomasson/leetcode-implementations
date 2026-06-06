import unittest
from solution import Solution


class TestMinBitFlips(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.minBitFlips(10, 7), 3)

    def test_example2(self):
        self.assertEqual(self.s.minBitFlips(3, 4), 3)

    def test_equal(self):
        self.assertEqual(self.s.minBitFlips(5, 5), 0)

    def test_both_zero(self):
        self.assertEqual(self.s.minBitFlips(0, 0), 0)

    def test_one_zero(self):
        self.assertEqual(self.s.minBitFlips(0, 1), 1)
        self.assertEqual(self.s.minBitFlips(7, 0), 3)

    def test_power_of_two(self):
        self.assertEqual(self.s.minBitFlips(0, 1024), 1)

    def test_large_values(self):
        self.assertEqual(self.s.minBitFlips(10**9, 0), bin(10**9).count('1'))

    def test_all_bits_differ(self):
        # 0 vs 2^30 - 1 (30 ones)
        self.assertEqual(self.s.minBitFlips(0, (1 << 30) - 1), 30)


if __name__ == '__main__':
    unittest.main()
