import unittest
from solution import Solution


class TestFirstDayBeenInAllRooms(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_all_as_then_bs(self):
        self.assertTrue(self.sol.firstDayBeenInAllRooms("aaabbb"))

    def test_interleaved(self):
        self.assertFalse(self.sol.firstDayBeenInAllRooms("abab"))

    def test_only_bs(self):
        self.assertTrue(self.sol.firstDayBeenInAllRooms("bbb"))

    def test_only_as(self):
        self.assertTrue(self.sol.firstDayBeenInAllRooms("aaa"))

    def test_single_a(self):
        self.assertTrue(self.sol.firstDayBeenInAllRooms("a"))

    def test_single_b(self):
        self.assertTrue(self.sol.firstDayBeenInAllRooms("b"))

    def test_ba(self):
        self.assertFalse(self.sol.firstDayBeenInAllRooms("ba"))

    def test_ab(self):
        self.assertTrue(self.sol.firstDayBeenInAllRooms("ab"))

    def test_aab(self):
        self.assertTrue(self.sol.firstDayBeenInAllRooms("aab"))


if __name__ == "__main__":
    unittest.main()
