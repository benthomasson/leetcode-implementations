import unittest
from solution import inorder


class TestInorder(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(inorder("abc", [[0, 1], [1, 2]]), "cab")

    def test_example2(self):
        self.assertEqual(inorder("abcdefg", [[1, 1], [1, 1], [0, 2], [1, 3]]), "efgabcd")

    def test_single_char(self):
        self.assertEqual(inorder("a", [[0, 5], [1, 3]]), "a")

    def test_all_left(self):
        self.assertEqual(inorder("abcd", [[0, 1], [0, 1]]), "cdab")

    def test_all_right(self):
        self.assertEqual(inorder("abcd", [[1, 1], [1, 1]]), "cdab")

    def test_net_zero(self):
        self.assertEqual(inorder("abc", [[0, 2], [1, 2]]), "abc")

    def test_shift_exceeds_length(self):
        self.assertEqual(inorder("abc", [[1, 7]]), "cab")

    def test_single_shift(self):
        self.assertEqual(inorder("abcde", [[0, 2]]), "cdeab")


if __name__ == "__main__":
    unittest.main()
