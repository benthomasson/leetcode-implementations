import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import Solution
import unittest


class TestDefangIPaddr(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.defangIPaddr("1.1.1.1"), "1[.]1[.]1[.]1")

    def test_example2(self):
        self.assertEqual(self.sol.defangIPaddr("255.100.50.0"), "255[.]100[.]50[.]0")

    def test_all_zeros(self):
        self.assertEqual(self.sol.defangIPaddr("0.0.0.0"), "0[.]0[.]0[.]0")

    def test_all_max(self):
        self.assertEqual(self.sol.defangIPaddr("255.255.255.255"), "255[.]255[.]255[.]255")

    def test_common_private(self):
        self.assertEqual(self.sol.defangIPaddr("192.168.1.1"), "192[.]168[.]1[.]1")

    def test_loopback(self):
        self.assertEqual(self.sol.defangIPaddr("127.0.0.1"), "127[.]0[.]0[.]1")

    def test_class_b(self):
        self.assertEqual(self.sol.defangIPaddr("172.16.0.1"), "172[.]16[.]0[.]1")


if __name__ == "__main__":
    unittest.main()
