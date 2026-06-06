import unittest
from solution import Solution


class TestCheckIfAllAsAppearsBeforeAllBs(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_all_as_then_bs(self):
        self.assertTrue(self.sol.checkIfAllAsAppearsBeforeAllBs("aaabbb"))

    def test_interleaved(self):
        self.assertFalse(self.sol.checkIfAllAsAppearsBeforeAllBs("abab"))

    def test_only_bs(self):
        self.assertTrue(self.sol.checkIfAllAsAppearsBeforeAllBs("bbb"))

    def test_only_as(self):
        self.assertTrue(self.sol.checkIfAllAsAppearsBeforeAllBs("aaa"))

    def test_single_a(self):
        self.assertTrue(self.sol.checkIfAllAsAppearsBeforeAllBs("a"))

    def test_single_b(self):
        self.assertTrue(self.sol.checkIfAllAsAppearsBeforeAllBs("b"))

    def test_ba(self):
        self.assertFalse(self.sol.checkIfAllAsAppearsBeforeAllBs("ba"))

    def test_ab(self):
        self.assertTrue(self.sol.checkIfAllAsAppearsBeforeAllBs("ab"))

    def test_aab(self):
        self.assertTrue(self.sol.checkIfAllAsAppearsBeforeAllBs("aab"))


if __name__ == "__main__":
    unittest.main()
