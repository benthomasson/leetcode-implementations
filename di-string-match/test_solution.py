import unittest
from solution import Solution


class TestDIStringMatch(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def _validate(self, s, perm):
        n = len(s)
        self.assertEqual(len(perm), n + 1)
        self.assertEqual(sorted(perm), list(range(n + 1)))
        for i, ch in enumerate(s):
            if ch == 'I':
                self.assertLess(perm[i], perm[i + 1])
            else:
                self.assertGreater(perm[i], perm[i + 1])

    def test_example1(self):
        self._validate("IDID", self.sol.isPalindrome("IDID"))

    def test_example2(self):
        self._validate("III", self.sol.isPalindrome("III"))

    def test_example3(self):
        self._validate("DDI", self.sol.isPalindrome("DDI"))

    def test_all_increasing(self):
        s = "IIIII"
        self._validate(s, self.sol.isPalindrome(s))

    def test_all_decreasing(self):
        s = "DDDDD"
        self._validate(s, self.sol.isPalindrome(s))

    def test_single_I(self):
        self._validate("I", self.sol.isPalindrome("I"))

    def test_single_D(self):
        self._validate("D", self.sol.isPalindrome("D"))

    def test_long_mixed(self):
        s = "DIDIDID"
        self._validate(s, self.sol.isPalindrome(s))


if __name__ == "__main__":
    unittest.main()
