"""Decode the Message - LeetCode Solution."""

import unittest


def valid_selections(key: str, message: str) -> str:
    """Decode a message using a substitution cipher derived from key.

    Args:
        key: Cipher key containing all 26 lowercase letters at least once.
        message: Secret message to decode.

    Returns:
        The decoded message.
    """
    table = {}
    idx = 0
    for ch in key:
        if ch != ' ' and ch not in table:
            table[ch] = chr(ord('a') + idx)
            idx += 1
    return ''.join(table.get(ch, ch) for ch in message)


class TestValidSelections(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(
            valid_selections("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"),
            "this is a secret",
        )

    def test_example2(self):
        self.assertEqual(
            valid_selections("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"),
            "the five boxing wizards jump quickly",
        )

    def test_spaces_only(self):
        key = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(valid_selections(key, "   "), "   ")

    def test_identity_key(self):
        key = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(valid_selections(key, "hello world"), "hello world")

    def test_single_char(self):
        key = "bacdefghijklmnopqrstuvwxyz"
        self.assertEqual(valid_selections(key, "b"), "a")

    def test_trailing_space(self):
        self.assertEqual(
            valid_selections("the quick brown fox jumps over the lazy dog ", "vkbs bs t suepuv "),
            "this is a secret ",
        )

    def test_key_with_many_duplicates(self):
        key = "aaabbbcccthe quick brown fox jumps over the lazy dog"
        # 'a'->a, 'b'->b, 'c'->c, 't'->d, 'h'->e, 'e'->f, ...
        self.assertEqual(valid_selections(key, "a"), "a")


if __name__ == "__main__":
    unittest.main()
