"""Split a String in Balanced Strings."""

import unittest


def find_special_integer(s: str) -> int:
    """Return the maximum number of balanced substrings of s.

    Args:
        s: A balanced string containing only 'L' and 'R'.

    Returns:
        Maximum number of balanced (equal L and R) substrings.
    """
    balance = 0
    result = 0
    for ch in s:
        balance += 1 if ch == "R" else -1
        if balance == 0:
            result += 1
    return result


class TestFindSpecialInteger(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(find_special_integer("RLRRLLRLRL"), 4)

    def test_example2(self):
        self.assertEqual(find_special_integer("RLRRRLLRLL"), 2)

    def test_example3(self):
        self.assertEqual(find_special_integer("LLLLRRRR"), 1)

    def test_minimal(self):
        self.assertEqual(find_special_integer("RL"), 1)

    def test_alternating(self):
        self.assertEqual(find_special_integer("RLRL"), 2)

    def test_nested(self):
        self.assertEqual(find_special_integer("RRLLRRLL"), 2)


if __name__ == "__main__":
    unittest.main()
