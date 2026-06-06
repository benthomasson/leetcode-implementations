"""Count the digits that divide a number."""

import unittest


def digits_dividing_num(num: int) -> int:
    """Return count of digits in num that evenly divide num.

    Args:
        num: Positive integer (1 <= num <= 10^9), no zero digits.

    Returns:
        Number of digits that divide num.
    """
    count = 0
    n = num
    while n:
        digit = n % 10
        if num % digit == 0:
            count += 1
        n //= 10
    return count


class TestDigitsDividingNum(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(digits_dividing_num(7), 1)

    def test_repeated_digit_partial(self):
        self.assertEqual(digits_dividing_num(121), 2)

    def test_all_divide(self):
        self.assertEqual(digits_dividing_num(1248), 4)

    def test_single_digit_one(self):
        self.assertEqual(digits_dividing_num(1), 1)

    def test_large_number(self):
        self.assertEqual(digits_dividing_num(111111111), 9)

    def test_no_digit_divides_except_one(self):
        # 13: 1 divides 13, 3 does not -> 1
        self.assertEqual(digits_dividing_num(13), 1)

    def test_all_same_digit(self):
        self.assertEqual(digits_dividing_num(555), 3)


if __name__ == "__main__":
    unittest.main()
