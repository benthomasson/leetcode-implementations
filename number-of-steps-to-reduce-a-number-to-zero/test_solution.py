import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

import unittest
from solution import Solution


class TestNumberOfSteps(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.queensAttacktheKing(14), 6)

    def test_example2(self):
        self.assertEqual(self.s.queensAttacktheKing(8), 4)

    def test_example3(self):
        self.assertEqual(self.s.queensAttacktheKing(123), 12)

    def test_zero(self):
        self.assertEqual(self.s.queensAttacktheKing(0), 0)

    def test_one(self):
        self.assertEqual(self.s.queensAttacktheKing(1), 1)

    def test_two(self):
        self.assertEqual(self.s.queensAttacktheKing(2), 2)

    def test_upper_bound(self):
        # 10^6 = 1111010000100100000000 in binary (20 bits, 7 ones)
        # steps = (bit_length - 1) + popcount = 19 + 7 = 26
        self.assertEqual(self.s.queensAttacktheKing(10**6), 26)

    def test_alias(self):
        self.assertEqual(self.s.numberOfSteps(14), 6)


if __name__ == '__main__':
    unittest.main()
