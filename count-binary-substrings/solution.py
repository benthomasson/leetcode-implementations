"""Count Binary Substrings - LeetCode"""

import unittest


def count_binary_substrings(s: str) -> int:
    """Count substrings with equal grouped 0's and 1's.

    Args:
        s: Binary string of '0's and '1's.

    Returns:
        Number of valid substrings.
    """
    result = 0
    prev, curr = 0, 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            curr += 1
        else:
            result += min(prev, curr)
            prev = curr
            curr = 1

    result += min(prev, curr)
    return result


class TestCountBinarySubstrings(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(count_binary_substrings("00110011"), 6)

    def test_example2(self):
        self.assertEqual(count_binary_substrings("10101"), 4)

    def test_single_char(self):
        self.assertEqual(count_binary_substrings("0"), 0)
        self.assertEqual(count_binary_substrings("1"), 0)

    def test_all_same(self):
        self.assertEqual(count_binary_substrings("0000"), 0)
        self.assertEqual(count_binary_substrings("1111"), 0)

    def test_two_chars(self):
        self.assertEqual(count_binary_substrings("01"), 1)
        self.assertEqual(count_binary_substrings("10"), 1)

    def test_alternating(self):
        self.assertEqual(count_binary_substrings("010101"), 5)

    def test_equal_runs(self):
        self.assertEqual(count_binary_substrings("000111"), 3)

    def test_unequal_runs(self):
        self.assertEqual(count_binary_substrings("00011"), 2)
        self.assertEqual(count_binary_substrings("00111"), 2)


if __name__ == "__main__":
    unittest.main()
