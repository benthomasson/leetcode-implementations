import unittest
from solution import worker_with_longest_task


class TestWorkerWithLongestTask(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(worker_with_longest_task(10, [[0, 3], [2, 5], [0, 9], [1, 15]]), 1)

    def test_example_2(self):
        self.assertEqual(worker_with_longest_task(26, [[1, 1], [3, 7], [2, 12], [7, 17]]), 3)

    def test_example_3_tie_returns_smallest(self):
        self.assertEqual(worker_with_longest_task(2, [[0, 10], [1, 20]]), 0)

    def test_single_log(self):
        self.assertEqual(worker_with_longest_task(5, [[3, 10]]), 3)

    def test_all_same_duration(self):
        self.assertEqual(worker_with_longest_task(3, [[2, 5], [0, 10], [1, 15]]), 0)

    def test_longest_is_first_task(self):
        self.assertEqual(worker_with_longest_task(3, [[1, 100], [2, 101]]), 1)

    def test_tie_non_adjacent(self):
        self.assertEqual(worker_with_longest_task(5, [[4, 10], [2, 15], [1, 25]]), 1)


if __name__ == "__main__":
    unittest.main()
