import unittest
from solution import Solution


class TestFlipAndInvertImage(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(
            self.s.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]),
            [[1, 0, 0], [0, 1, 0], [1, 1, 1]],
        )

    def test_example2(self):
        self.assertEqual(
            self.s.flipAndInvertImage(
                [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
            ),
            [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]],
        )

    def test_1x1_zero(self):
        self.assertEqual(self.s.flipAndInvertImage([[0]]), [[1]])

    def test_1x1_one(self):
        self.assertEqual(self.s.flipAndInvertImage([[1]]), [[0]])

    def test_all_zeros(self):
        self.assertEqual(
            self.s.flipAndInvertImage([[0, 0], [0, 0]]),
            [[1, 1], [1, 1]],
        )

    def test_all_ones(self):
        self.assertEqual(
            self.s.flipAndInvertImage([[1, 1], [1, 1]]),
            [[0, 0], [0, 0]],
        )

    def test_odd_dimension(self):
        # 3x3 with middle element: flip+invert middle of row means just XOR
        self.assertEqual(
            self.s.flipAndInvertImage([[1, 0, 1], [0, 1, 0], [1, 1, 0]]),
            [[0, 1, 0], [1, 0, 1], [1, 0, 0]],
        )


if __name__ == "__main__":
    unittest.main()
