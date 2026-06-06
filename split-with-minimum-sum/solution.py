"""Split With Minimum Sum - LeetCode Solution."""

import unittest


def min_sum_of_two_numbers(num: int) -> int:
    """Split num into two numbers with minimum possible sum.

    Args:
        num: A positive integer (10 <= num <= 10^9).

    Returns:
        The minimum possible sum of the two split numbers.
    """
    digits = sorted(str(num))
    parts = ["", ""]
    for i, d in enumerate(digits):
        parts[i % 2] += d
    return int(parts[0]) + int(parts[1])


class TestMinSumOfTwoNumbers(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(min_sum_of_two_numbers(4325), 59)

    def test_example_2(self):
        self.assertEqual(min_sum_of_two_numbers(687), 75)

    def test_two_digits(self):
        self.assertEqual(min_sum_of_two_numbers(10), 1)

    def test_repeated_digits(self):
        self.assertEqual(min_sum_of_two_numbers(1111), 22)

    def test_large_input(self):
        self.assertEqual(min_sum_of_two_numbers(999999999), 109998)

    def test_with_zeros(self):
        # 2030 -> digits [0,0,2,3] -> parts "02" "03" -> 2 + 3 = 5
        self.assertEqual(min_sum_of_two_numbers(2030), 5)


if __name__ == "__main__":
    unittest.main()
