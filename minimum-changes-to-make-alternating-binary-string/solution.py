"""Minimum Changes to Make Alternating Binary String."""

import unittest


def canDistribute(s: str) -> int:
    """Return minimum changes to make s an alternating binary string.

    Args:
        s: Binary string of '0's and '1's.

    Returns:
        Minimum number of character flips needed.
    """
    count = sum(1 for i, c in enumerate(s) if c != ('0' if i % 2 == 0 else '1'))
    return min(count, len(s) - count)


class TestCanDistribute(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(canDistribute("0100"), 1)

    def test_example2(self):
        self.assertEqual(canDistribute("10"), 0)

    def test_example3(self):
        self.assertEqual(canDistribute("1111"), 2)

    def test_single_char(self):
        self.assertEqual(canDistribute("0"), 0)
        self.assertEqual(canDistribute("1"), 0)

    def test_all_same(self):
        self.assertEqual(canDistribute("0000"), 2)
        self.assertEqual(canDistribute("111"), 1)

    def test_already_alternating(self):
        self.assertEqual(canDistribute("0101"), 0)
        self.assertEqual(canDistribute("1010"), 0)

    def test_two_chars(self):
        self.assertEqual(canDistribute("00"), 1)
        self.assertEqual(canDistribute("11"), 1)


if __name__ == "__main__":
    unittest.main()
