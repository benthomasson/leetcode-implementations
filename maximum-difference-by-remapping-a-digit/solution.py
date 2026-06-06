"""Maximum Difference by Remapping a Digit."""

import unittest


def diffMaxMin(num: int) -> int:
    """Return max - min achievable by remapping exactly one digit.

    Args:
        num: Positive integer (1 <= num <= 10^8).

    Returns:
        Difference between maximum and minimum remapped values.
    """
    s = str(num)

    # Max: remap first non-9 digit to 9
    max_val = num
    for d in s:
        if d != '9':
            max_val = int(s.replace(d, '9'))
            break

    # Min: remap first digit to 0 (leading zeros allowed)
    min_val = int(s.replace(s[0], '0'))

    return max_val - min_val


class TestDiffMaxMin(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(diffMaxMin(11891), 99009)

    def test_example2(self):
        self.assertEqual(diffMaxMin(90), 99)

    def test_single_digit(self):
        self.assertEqual(diffMaxMin(5), 9)

    def test_single_digit_nine(self):
        self.assertEqual(diffMaxMin(9), 9)

    def test_all_same(self):
        self.assertEqual(diffMaxMin(1111), 9999)

    def test_starts_with_nine(self):
        # 9288 -> max: remap 2->9 = 9988, min: remap 9->0 = 0288=288
        self.assertEqual(diffMaxMin(9288), 9700)

    def test_all_nines(self):
        # max=9999, min: remap 9->0 = 0000=0
        self.assertEqual(diffMaxMin(9999), 9999)

    def test_one(self):
        self.assertEqual(diffMaxMin(1), 9)

    def test_max_constraint(self):
        # 100000000: max remap 1->9 = 900000000, min remap 1->0 = 0
        self.assertEqual(diffMaxMin(100000000), 900000000)


if __name__ == '__main__':
    unittest.main()
