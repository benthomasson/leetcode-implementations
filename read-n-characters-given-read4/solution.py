"""Read N Characters Given Read4 - LeetCode Solution."""

import unittest
from typing import List


class Reader4:
    """Simulates the read4 API with an internal file pointer."""

    def __init__(self, file: str):
        self._file = file
        self._pos = 0

    def read4(self, buf4: List[str]) -> int:
        """Reads up to 4 characters from file into buf4.

        Args:
            buf4: Destination buffer (list of length >= 4).

        Returns:
            Number of characters actually read.
        """
        count = 0
        while count < 4 and self._pos < len(self._file):
            buf4[count] = self._file[self._pos]
            self._pos += 1
            count += 1
        return count


class Solution(Reader4):
    """Solution using read4 to read n characters."""

    def read(self, buf: List[str], n: int) -> int:
        """Reads n characters from file into buf using read4.

        Args:
            buf: Destination buffer.
            n: Number of characters to read.

        Returns:
            Number of characters actually read.
        """
        total = 0
        buf4 = [''] * 4
        while total < n:
            count = self.read4(buf4)
            to_copy = min(count, n - total)
            for i in range(to_copy):
                buf[total] = buf4[i]
                total += 1
            if count < 4:
                break
        return total


class TestSolution(unittest.TestCase):

    def _run_read(self, file: str, n: int):
        sol = Solution(file)
        buf = [''] * n
        result = sol.read(buf, n)
        return result, ''.join(buf[:result])

    def test_file_shorter_than_n(self):
        count, content = self._run_read("abc", 4)
        self.assertEqual(count, 3)
        self.assertEqual(content, "abc")

    def test_file_exact_length(self):
        count, content = self._run_read("abcde", 5)
        self.assertEqual(count, 5)
        self.assertEqual(content, "abcde")

    def test_file_longer_than_n(self):
        count, content = self._run_read("abcdABCD1234", 12)
        self.assertEqual(count, 12)
        self.assertEqual(content, "abcdABCD1234")

    def test_n_less_than_file(self):
        count, content = self._run_read("abcdefgh", 3)
        self.assertEqual(count, 3)
        self.assertEqual(content, "abc")

    def test_single_char_file(self):
        count, content = self._run_read("a", 1)
        self.assertEqual(count, 1)
        self.assertEqual(content, "a")

    def test_n_one_long_file(self):
        count, content = self._run_read("abcdef", 1)
        self.assertEqual(count, 1)
        self.assertEqual(content, "a")

    def test_exactly_four_chars(self):
        count, content = self._run_read("abcd", 4)
        self.assertEqual(count, 4)
        self.assertEqual(content, "abcd")

    def test_five_chars_read_four(self):
        count, content = self._run_read("abcde", 4)
        self.assertEqual(count, 4)
        self.assertEqual(content, "abcd")

    def test_large_n(self):
        count, content = self._run_read("abc", 1000)
        self.assertEqual(count, 3)
        self.assertEqual(content, "abc")


if __name__ == "__main__":
    unittest.main()
