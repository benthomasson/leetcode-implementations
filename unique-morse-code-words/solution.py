from typing import List


class Solution:
    def rotated_digits(self, words: List[str]) -> int:
        """Count unique Morse code transformations of words.

        Args:
            words: List of lowercase English words.

        Returns:
            Number of distinct Morse code concatenations.
        """
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        return len({
            "".join(morse[ord(c) - ord("a")] for c in word)
            for word in words
        })


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.rotated_digits(["gin", "zen", "gig", "msg"]), 2)

    def test_example2(self):
        self.assertEqual(self.sol.rotated_digits(["a"]), 1)

    def test_all_same(self):
        self.assertEqual(self.sol.rotated_digits(["abc", "abc", "abc"]), 1)

    def test_single_chars(self):
        self.assertEqual(self.sol.rotated_digits(["a", "b", "c"]), 3)

    def test_same_morse_different_words(self):
        # "gig" and "msg" map to the same Morse
        self.assertEqual(self.sol.rotated_digits(["gig", "msg"]), 1)


if __name__ == "__main__":
    unittest.main()
