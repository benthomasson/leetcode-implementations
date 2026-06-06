"""Check if one string swap can make strings equal."""

import unittest


def are_almost_equal(s1: str, s2: str) -> bool:
    """Return True if at most one swap on one string can make them equal.

    Args:
        s1: First string.
        s2: Second string of equal length.

    Returns:
        True if strings can be made equal with at most one swap.
    """
    diffs = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diffs.append(i)
            if len(diffs) > 2:
                return False
    if len(diffs) == 0:
        return True
    if len(diffs) == 2:
        i, j = diffs
        return s1[i] == s2[j] and s1[j] == s2[i]
    return False


class TestAreAlmostEqual(unittest.TestCase):
    def test_already_equal(self):
        self.assertTrue(are_almost_equal("kelb", "kelb"))

    def test_one_swap_needed(self):
        self.assertTrue(are_almost_equal("bank", "kanb"))

    def test_impossible(self):
        self.assertFalse(are_almost_equal("attack", "defend"))

    def test_single_char_equal(self):
        self.assertTrue(are_almost_equal("a", "a"))

    def test_single_char_different(self):
        self.assertFalse(are_almost_equal("a", "b"))

    def test_single_mismatch(self):
        self.assertFalse(are_almost_equal("ab", "ac"))

    def test_same_freq_but_too_many_diffs(self):
        self.assertFalse(are_almost_equal("abcd", "dcba"))

    def test_swap_same_index(self):
        # Swapping same index is a no-op, so strings must already be equal
        self.assertTrue(are_almost_equal("aa", "aa"))

    def test_two_diffs_wrong_chars(self):
        self.assertFalse(are_almost_equal("ab", "cd"))


if __name__ == "__main__":
    unittest.main()
