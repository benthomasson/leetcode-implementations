"""Apply Operations to an Array."""

import unittest


def performOps(nums: list[int]) -> list[int]:
    """Apply pairwise operations then shift zeros to end.

    Args:
        nums: List of non-negative integers.

    Returns:
        Resulting array after operations and zero-shifting.
    """
    result = nums[:]

    # Phase 1: apply operations sequentially
    for i in range(len(result) - 1):
        if result[i] == result[i + 1]:
            result[i] *= 2
            result[i + 1] = 0

    # Phase 2: move zeros to end
    write = 0
    for val in result:
        if val != 0:
            result[write] = val
            write += 1
    while write < len(result):
        result[write] = 0
        write += 1

    return result


class TestPerformOps(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(performOps([1, 2, 2, 1, 1, 0]), [1, 4, 2, 0, 0, 0])

    def test_example2(self):
        self.assertEqual(performOps([0, 1]), [1, 0])

    def test_all_zeros(self):
        self.assertEqual(performOps([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_no_duplicates(self):
        self.assertEqual(performOps([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_consecutive_triples(self):
        # [2,2,2] -> after ops: [4,0,2] -> shifted: [4,2,0]
        self.assertEqual(performOps([2, 2, 2]), [4, 2, 0])

    def test_all_same(self):
        # [1,1,1,1] -> [2,0,2,0] -> [2,2,0,0]
        self.assertEqual(performOps([1, 1, 1, 1]), [2, 2, 0, 0])

    def test_single_pair(self):
        self.assertEqual(performOps([5, 5]), [10, 0])

    def test_zeros_between(self):
        # [1,0,0,1] -> no adjacent equal non-zeros match ops: i=1: 0==0 -> [1,0,0,1]
        # Wait: 0==0 is true, so [1,0,0,1] -> i=0: 1!=0 skip, i=1: 0==0 -> [1,0,0,1] -> double 0 is 0, set next to 0
        # Result stays [1,0,0,1] -> shifted: [1,1,0,0]
        self.assertEqual(performOps([1, 0, 0, 1]), [1, 1, 0, 0])


if __name__ == "__main__":
    unittest.main()
