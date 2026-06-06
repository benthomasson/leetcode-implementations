"""Tests for split_and_minimize (Largest 3-Same-Digit Number in String)."""

import unittest

from solution import Solution


class TestSplitAndMinimize(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    # --- LeetCode examples ---

    def test_example_1(self) -> None:
        self.assertEqual(self.sol.split_and_minimize("6777133339"), "777")

    def test_example_2(self) -> None:
        self.assertEqual(self.sol.split_and_minimize("2300019"), "000")

    def test_example_3(self) -> None:
        self.assertEqual(self.sol.split_and_minimize("42352338"), "")

    # --- Edge cases ---

    def test_all_same_digit(self) -> None:
        self.assertEqual(self.sol.split_and_minimize("999"), "999")

    def test_all_zeros(self) -> None:
        self.assertEqual(self.sol.split_and_minimize("000"), "000")

    def test_minimum_length_no_match(self) -> None:
        self.assertEqual(self.sol.split_and_minimize("123"), "")

    def test_multiple_good_integers(self) -> None:
        # "111" and "999" both present; should return "999"
        self.assertEqual(self.sol.split_and_minimize("111999"), "999")

    def test_multiple_good_integers_reverse_order(self) -> None:
        # "999" appears before "111"; should still return "999"
        self.assertEqual(self.sol.split_and_minimize("999111"), "999")

    def test_four_same_digits(self) -> None:
        # "5555" contains two overlapping "555" substrings
        self.assertEqual(self.sol.split_and_minimize("5555"), "555")

    def test_long_run_of_same_digit(self) -> None:
        self.assertEqual(self.sol.split_and_minimize("0000000"), "000")

    def test_good_integer_at_end(self) -> None:
        self.assertEqual(self.sol.split_and_minimize("12888"), "888")

    def test_good_integer_at_start(self) -> None:
        self.assertEqual(self.sol.split_and_minimize("33312"), "333")

    def test_adjacent_different_triples(self) -> None:
        # "222333" -> both "222" and "333" are good; return "333"
        self.assertEqual(self.sol.split_and_minimize("222333"), "333")

    def test_no_triple_with_pairs(self) -> None:
        # Lots of pairs but no triple
        self.assertEqual(self.sol.split_and_minimize("112233"), "")

    def test_all_nines(self) -> None:
        self.assertEqual(self.sol.split_and_minimize("999999999"), "999")

    def test_leading_zeros_good_integer(self) -> None:
        self.assertEqual(self.sol.split_and_minimize("10001"), "000")


if __name__ == "__main__":
    unittest.main()
