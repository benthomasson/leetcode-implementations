import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


def _is_valid_swap(alice, bob, result):
    """Check that swapping result[0] from Alice and result[1] from Bob equalizes totals."""
    a, b = result
    assert a in alice, f"{a} not in aliceSizes"
    assert b in bob, f"{b} not in bobSizes"
    new_alice = sum(alice) - a + b
    new_bob = sum(bob) - b + a
    return new_alice == new_bob


class TestFairCandySwap(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- LeetCode examples ---
    def test_example1(self):
        self.assertEqual(self.s.fairCandySwap([1, 1], [2, 2]), [1, 2])

    def test_example2(self):
        self.assertEqual(self.s.fairCandySwap([1, 2], [2, 3]), [1, 2])

    def test_example3(self):
        self.assertEqual(self.s.fairCandySwap([2], [1, 3]), [2, 3])

    # --- Edge cases (all inputs satisfy sumA+sumB is even) ---
    def test_bob_has_more(self):
        # sumA=3, sumB=7 => odd total, invalid. Use [1,2],[3,4,2]: sumA=3,sumB=9,sum=12
        # delta=-3, a=1: 1+3=4 in {3,4,2}? yes => [1,4]
        result = self.s.fairCandySwap([1, 2], [3, 4, 2])
        self.assertTrue(_is_valid_swap([1, 2], [3, 4, 2], result))

    def test_alice_has_more(self):
        # sumA=5, sumB=3, delta=1. a=3: 3-1=2 in {1,2}? yes => [3,2]
        result = self.s.fairCandySwap([3, 2], [1, 2])
        self.assertTrue(_is_valid_swap([3, 2], [1, 2], result))

    def test_duplicate_values(self):
        # sumA=2, sumB=4, delta=-1. a=1: 1+1=2 in {2,2}? yes => [1,2]
        result = self.s.fairCandySwap([1, 1], [2, 2])
        self.assertTrue(_is_valid_swap([1, 1], [2, 2], result))

    def test_larger_arrays(self):
        # sumA=15, sumB=17, delta=-1. a=2: 2+1=3 in bob? yes => [2,3]
        alice = [1, 2, 3, 4, 5]
        bob = [1, 3, 5, 8]
        result = self.s.fairCandySwap(alice, bob)
        self.assertTrue(_is_valid_swap(alice, bob, result))

    def test_single_alice_multiple_bob(self):
        # sumA=5, sumB=3, delta=1. a=5: 5-1=4 in {1,4}? no wait, bob={1,2}
        # Use [5],[1,2]: sumA=5,sumB=3, delta=1. a=5: 5-1=4, not in {1,2}. Bad.
        # Use [5],[2,4]: sumA=5,sumB=6, sum=11 odd. Bad.
        # Use [4],[1,3]: sumA=4,sumB=4 equal. Bad.
        # Use [5],[1,6]: sumA=5,sumB=7, sum=12, delta=-1. a=5: 5+1=6 in {1,6}? yes => [5,6]
        result = self.s.fairCandySwap([5], [1, 6])
        self.assertTrue(_is_valid_swap([5], [1, 6], result))

    def test_return_type_is_list(self):
        result = self.s.fairCandySwap([1, 1], [2, 2])
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()
