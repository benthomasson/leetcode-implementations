import sys
sys.path.insert(0, "../implementer")
from solution import Solution

import unittest


class TestCountTriples(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1_n5(self):
        self.assertEqual(self.s.countTriples(5), 2)

    def test_example2_n10(self):
        self.assertEqual(self.s.countTriples(10), 4)

    def test_n1_no_triples(self):
        self.assertEqual(self.s.countTriples(1), 0)

    def test_n4_no_triples(self):
        self.assertEqual(self.s.countTriples(4), 0)

    def test_n13_includes_5_12_13(self):
        # (3,4,5),(4,3,5),(5,12,13),(12,5,13),(6,8,10),(8,6,10)
        self.assertEqual(self.s.countTriples(13), 6)

    def test_n25_multiple_triples(self):
        # Includes (7,24,25),(24,7,25) plus earlier ones
        result = self.s.countTriples(25)
        self.assertGreater(result, 6)

    def test_n250_upper_bound(self):
        # Constraint max; just verify it runs and returns positive
        result = self.s.countTriples(250)
        self.assertGreater(result, 0)

    def test_counts_both_orderings(self):
        # (3,4,5) and (4,3,5) should both count
        self.assertEqual(self.s.countTriples(5), 2)


if __name__ == "__main__":
    unittest.main()
