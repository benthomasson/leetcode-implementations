import unittest
from solution import is_self_dividing, self_dividing_numbers


class TestIsSelfDividing(unittest.TestCase):
    def test_single_digits(self):
        for n in range(1, 10):
            self.assertTrue(is_self_dividing(n))

    def test_contains_zero(self):
        for n in [10, 20, 30, 100, 101, 200]:
            self.assertFalse(is_self_dividing(n))

    def test_self_dividing(self):
        for n in [11, 12, 15, 22, 48, 128]:
            self.assertTrue(is_self_dividing(n))

    def test_not_self_dividing(self):
        for n in [13, 14, 16, 21, 23, 26]:
            self.assertFalse(is_self_dividing(n))


class TestSelfDividingNumbers(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(
            self_dividing_numbers(1, 22),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22],
        )

    def test_example2(self):
        self.assertEqual(self_dividing_numbers(47, 85), [48, 55, 66, 77])

    def test_single_value_range(self):
        self.assertEqual(self_dividing_numbers(11, 11), [11])
        self.assertEqual(self_dividing_numbers(10, 10), [])

    def test_upper_bound(self):
        result = self_dividing_numbers(9990, 10000)
        self.assertEqual(result, [9999])


if __name__ == "__main__":
    unittest.main()
