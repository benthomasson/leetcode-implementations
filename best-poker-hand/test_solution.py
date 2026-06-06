import unittest
from solution import best_poker_hand


class TestBestPokerHand(unittest.TestCase):
    def test_flush(self):
        assert best_poker_hand([13, 2, 3, 1, 9], ["a", "a", "a", "a", "a"]) == "Flush "

    def test_three_of_a_kind(self):
        assert best_poker_hand([4, 4, 2, 4, 4], ["d", "a", "a", "b", "c"]) == "Three of a Kind "

    def test_pair(self):
        assert best_poker_hand([10, 10, 2, 12, 9], ["a", "b", "c", "a", "d"]) == "Pair "

    def test_high_card(self):
        assert best_poker_hand([1, 2, 3, 4, 5], ["a", "b", "c", "d", "a"]) == "High Card "

    def test_four_of_a_kind_returns_three(self):
        assert best_poker_hand([3, 3, 3, 3, 5], ["a", "b", "c", "d", "a"]) == "Three of a Kind "

    def test_flush_with_pair(self):
        assert best_poker_hand([1, 1, 3, 4, 5], ["b", "b", "b", "b", "b"]) == "Flush "

    def test_two_pairs(self):
        assert best_poker_hand([1, 1, 2, 2, 3], ["a", "b", "c", "d", "a"]) == "Pair "


if __name__ == "__main__":
    unittest.main()
