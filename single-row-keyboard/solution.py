"""Single Row Keyboard - LeetCode Solution."""

import unittest


def calculate_time(keyboard: str, word: str) -> int:
    """Calculate time to type a word on a single-row keyboard.

    Args:
        keyboard: 26-char string mapping each position to a letter.
        word: The word to type.

    Returns:
        Total time (sum of absolute index differences).
    """
    pos = {c: i for i, c in enumerate(keyboard)}
    current = 0
    total = 0
    for c in word:
        total += abs(current - pos[c])
        current = pos[c]
    return total


class TestCalculateTime(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(calculate_time("abcdefghijklmnopqrstuvwxyz", "cba"), 4)

    def test_example2(self):
        self.assertEqual(calculate_time("pqrstuvwxyzabcdefghijklmno", "leetcode"), 73)

    def test_single_char(self):
        self.assertEqual(calculate_time("abcdefghijklmnopqrstuvwxyz", "a"), 0)

    def test_single_char_far(self):
        self.assertEqual(calculate_time("abcdefghijklmnopqrstuvwxyz", "z"), 25)

    def test_repeated_char(self):
        self.assertEqual(calculate_time("abcdefghijklmnopqrstuvwxyz", "aaa"), 0)

    def test_worst_case_alternating(self):
        # a at 0, z at 25 -> alternating costs 25 each move
        self.assertEqual(calculate_time("abcdefghijklmnopqrstuvwxyz", "azaz"), 25 + 25 + 25)

    def test_all_letters(self):
        kb = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(calculate_time(kb, kb), 25)  # 0->1->2->...->25 = 25


if __name__ == "__main__":
    unittest.main()
