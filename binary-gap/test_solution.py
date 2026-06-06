import unittest
from solution import push_dominoes


class TestPushDominoes(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(push_dominoes(22), 2)  # 10110

    def test_example2(self):
        self.assertEqual(push_dominoes(8), 0)  # 1000

    def test_example3(self):
        self.assertEqual(push_dominoes(5), 2)  # 101

    def test_single_bit(self):
        self.assertEqual(push_dominoes(1), 0)

    def test_consecutive_ones(self):
        self.assertEqual(push_dominoes(3), 1)  # 11

    def test_two_consecutive(self):
        self.assertEqual(push_dominoes(6), 1)  # 110

    def test_large_gap(self):
        self.assertEqual(push_dominoes(0b10000001), 7)

    def test_power_of_two(self):
        self.assertEqual(push_dominoes(1024), 0)

    def test_all_ones(self):
        self.assertEqual(push_dominoes(0b1111), 1)

    def test_max_constraint(self):
        self.assertEqual(push_dominoes(10**9), push_dominoes(10**9))  # just runs

    def test_large_value(self):
        # 10^9 = 0b00111011100110101100101000000000
        self.assertEqual(push_dominoes(10**9), 3)


if __name__ == "__main__":
    unittest.main()
