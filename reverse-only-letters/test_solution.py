import unittest
from solution import Solution


class TestReverseOnlyLetters(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.num_rescue_boats("ab-cd"), "dc-ba")

    def test_example2(self):
        self.assertEqual(self.sol.num_rescue_boats("a-bC-dEf-ghIj"), "j-Ih-gfE-dCba")

    def test_example3(self):
        self.assertEqual(self.sol.num_rescue_boats("Test1ng-Leet=code-Q!"), "Qedo1ct-eeLg=ntse-T!")

    def test_all_letters(self):
        self.assertEqual(self.sol.num_rescue_boats("abcde"), "edcba")

    def test_no_letters(self):
        self.assertEqual(self.sol.num_rescue_boats("12-34!"), "12-34!")

    def test_single_letter(self):
        self.assertEqual(self.sol.num_rescue_boats("a"), "a")

    def test_single_non_letter(self):
        self.assertEqual(self.sol.num_rescue_boats("-"), "-")

    def test_letters_with_digits(self):
        self.assertEqual(self.sol.num_rescue_boats("a1b2c"), "c1b2a")


if __name__ == "__main__":
    unittest.main()
