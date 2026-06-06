"""Tests for Read N Characters Given Read4."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestReadNChars(unittest.TestCase):
    """Test the Solution.read method."""

    def _run(self, file: str, n: int):
        sol = Solution(file)
        buf = [''] * max(n, 1)
        count = sol.read(buf, n)
        return count, ''.join(buf[:count])

    # --- LeetCode examples ---
    def test_example1_file_shorter(self):
        count, content = self._run("abc", 4)
        self.assertEqual(count, 3)
        self.assertEqual(content, "abc")

    def test_example2_exact(self):
        count, content = self._run("abcde", 5)
        self.assertEqual(count, 5)
        self.assertEqual(content, "abcde")

    def test_example3_twelve_chars(self):
        count, content = self._run("abcdABCD1234", 12)
        self.assertEqual(count, 12)
        self.assertEqual(content, "abcdABCD1234")

    # --- Edge cases ---
    def test_single_char(self):
        count, content = self._run("a", 1)
        self.assertEqual(count, 1)
        self.assertEqual(content, "a")

    def test_n_larger_than_file(self):
        count, content = self._run("ab", 1000)
        self.assertEqual(count, 2)
        self.assertEqual(content, "ab")

    def test_n_smaller_than_file(self):
        count, content = self._run("abcdefgh", 3)
        self.assertEqual(count, 3)
        self.assertEqual(content, "abc")

    def test_exact_multiple_of_4(self):
        count, content = self._run("abcdefgh", 8)
        self.assertEqual(count, 8)
        self.assertEqual(content, "abcdefgh")

    def test_not_multiple_of_4(self):
        count, content = self._run("abcde", 4)
        self.assertEqual(count, 4)
        self.assertEqual(content, "abcd")


if __name__ == "__main__":
    unittest.main()
