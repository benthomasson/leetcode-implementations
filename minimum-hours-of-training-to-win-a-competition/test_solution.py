"""Tests for minimum hours of training solution."""

import unittest
from solution import min_training_hours


class TestMinTrainingHours(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(
            min_training_hours(5, 3, [1, 4, 3, 2], [2, 6, 3, 1]), 8
        )

    def test_example2(self):
        self.assertEqual(min_training_hours(2, 4, [1], [3]), 0)

    def test_no_training_needed(self):
        self.assertEqual(min_training_hours(100, 100, [1], [1]), 0)

    def test_only_energy_needed(self):
        self.assertEqual(min_training_hours(1, 100, [5, 5], [1, 1]), 10)

    def test_only_experience_needed(self):
        self.assertEqual(min_training_hours(100, 1, [1], [5]), 5)

    def test_single_opponent_exact_boundary(self):
        # Need strictly greater: energy=3 vs cost=3 -> need 1 more energy
        # Experience=3 vs opp=3 -> need 1 more experience
        self.assertEqual(min_training_hours(3, 3, [3], [3]), 2)

    def test_experience_accumulates(self):
        # Start with exp=1, opponents exp=[1,1,1]
        # Opp 0: need >1, gap=1, cur=2, after=2+1=3
        # Opp 1: 3>1, ok, after=3+1=4
        # Opp 2: 4>1, ok, after=4+1=5
        # Energy: need >3, with initialEnergy=10 -> 0
        self.assertEqual(min_training_hours(10, 1, [1, 1, 1], [1, 1, 1]), 1)

    def test_all_max_values(self):
        n = 100
        energy = [100] * n
        experience = [100] * n
        # Energy needed: 100*100 + 1 - 1 = 10000
        # Experience: opp0 need >100, gap=100, cur=101, after=201
        # All subsequent: 201>100, ok. So exp_needed=100
        self.assertEqual(
            min_training_hours(1, 1, energy, experience), 10100
        )


if __name__ == "__main__":
    unittest.main()
