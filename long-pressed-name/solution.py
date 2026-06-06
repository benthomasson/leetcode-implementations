"""Long Pressed Name - LeetCode"""

import unittest


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        """Check if typed could be name with some keys long-pressed.

        Args:
            name: The intended name.
            typed: The actual typed string.

        Returns:
            True if typed matches name allowing long-pressed repeats.
        """
        i = 0
        for j in range(len(typed)):
            if i < len(name) and typed[j] == name[i]:
                i += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                continue  # long press repeat
            else:
                return False
        return i == len(name)


class TestLongPressedName(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertTrue(self.s.isLongPressedName("alex", "aaleex"))

    def test_example2(self):
        self.assertFalse(self.s.isLongPressedName("saeed", "ssaaedd"))

    def test_identical(self):
        self.assertTrue(self.s.isLongPressedName("abc", "abc"))

    def test_single_char(self):
        self.assertTrue(self.s.isLongPressedName("a", "aaa"))

    def test_single_char_mismatch(self):
        self.assertFalse(self.s.isLongPressedName("a", "b"))

    def test_typed_shorter(self):
        self.assertFalse(self.s.isLongPressedName("abc", "ab"))

    def test_all_same(self):
        self.assertTrue(self.s.isLongPressedName("aaa", "aaaaaaa"))

    def test_extra_char_at_end(self):
        self.assertFalse(self.s.isLongPressedName("alex", "aaleexa"))

    def test_wrong_first_char(self):
        self.assertFalse(self.s.isLongPressedName("alex", "baleex"))

    def test_empty_typed(self):
        self.assertFalse(self.s.isLongPressedName("a", ""))

    def test_both_single(self):
        self.assertTrue(self.s.isLongPressedName("a", "a"))


if __name__ == "__main__":
    unittest.main()
