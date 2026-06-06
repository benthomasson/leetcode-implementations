"""Maximum Number of Balloons - LeetCode"""

from collections import Counter


def max_number_of_balloons(text: str) -> int:
    """Return max instances of 'balloon' formable from text characters.

    Args:
        text: String of lowercase English letters.

    Returns:
        Maximum number of 'balloon' instances.
    """
    count = Counter(text)
    return min(
        count['b'],
        count['a'],
        count['l'] // 2,
        count['o'] // 2,
        count['n'],
    )


# --- Tests ---
import unittest


class TestMaxNumberOfBalloons(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(max_number_of_balloons("nlaebolko"), 1)

    def test_example2(self):
        self.assertEqual(max_number_of_balloons("loonbalxballpoon"), 2)

    def test_example3(self):
        self.assertEqual(max_number_of_balloons("leetcode"), 0)

    def test_empty(self):
        self.assertEqual(max_number_of_balloons(""), 0)

    def test_exact_balloon(self):
        self.assertEqual(max_number_of_balloons("balloon"), 1)

    def test_no_matching_chars(self):
        self.assertEqual(max_number_of_balloons("zzzzz"), 0)

    def test_partial_chars(self):
        self.assertEqual(max_number_of_balloons("bal"), 0)

    def test_limited_by_double_letter(self):
        # Has enough of everything except only 1 'l'
        self.assertEqual(max_number_of_balloons("balon"), 0)

    def test_multiple(self):
        self.assertEqual(max_number_of_balloons("balloonballoon"), 2)


if __name__ == "__main__":
    unittest.main()
