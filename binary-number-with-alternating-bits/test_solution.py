import unittest
from solution import has_alternating_bits


class TestHasAlternatingBits(unittest.TestCase):

    def test_example_5(self):
        self.assertTrue(has_alternating_bits(5))  # 101

    def test_example_7(self):
        self.assertFalse(has_alternating_bits(7))  # 111

    def test_example_11(self):
        self.assertFalse(has_alternating_bits(11))  # 1011

    def test_one(self):
        self.assertTrue(has_alternating_bits(1))  # 1

    def test_two(self):
        self.assertTrue(has_alternating_bits(2))  # 10

    def test_three(self):
        self.assertFalse(has_alternating_bits(3))  # 11

    def test_ten(self):
        self.assertTrue(has_alternating_bits(10))  # 1010

    def test_21(self):
        self.assertTrue(has_alternating_bits(21))  # 10101

    def test_power_of_two(self):
        self.assertFalse(has_alternating_bits(4))  # 100

    def test_large_alternating(self):
        self.assertTrue(has_alternating_bits(0b1010101010))

    def test_max_value(self):
        self.assertFalse(has_alternating_bits(2**31 - 1))


if __name__ == "__main__":
    unittest.main()
