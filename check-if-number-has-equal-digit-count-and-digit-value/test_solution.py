import unittest
import sys
sys.path.insert(0, "../implementer")
from solution import Solution, rearrange_array


class TestDigitCount(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # Problem examples
    def test_example1_true(self):
        self.assertTrue(self.s.digitCount("1210"))

    def test_example2_false(self):
        self.assertFalse(self.s.digitCount("030"))

    # Edge cases
    def test_single_zero(self):
        self.assertFalse(self.s.digitCount("0"))

    def test_single_one(self):
        self.assertFalse(self.s.digitCount("1"))

    def test_2020_true(self):
        self.assertTrue(self.s.digitCount("2020"))

    def test_10_false(self):
        self.assertFalse(self.s.digitCount("10"))

    def test_2100_false(self):
        self.assertFalse(self.s.digitCount("2100"))

    # Alias works
    def test_rearrange_array_alias(self):
        self.assertTrue(rearrange_array("1210"))
        self.assertFalse(rearrange_array("030"))


if __name__ == "__main__":
    unittest.main()
