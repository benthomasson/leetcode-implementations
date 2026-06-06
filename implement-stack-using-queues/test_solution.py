"""Tests for MyStack."""

import unittest
from solution import MyStack


class TestMyStack(unittest.TestCase):
    def test_example(self):
        s = MyStack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.top(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertFalse(s.empty())

    def test_empty(self):
        s = MyStack()
        self.assertTrue(s.empty())

    def test_single_element(self):
        s = MyStack()
        s.push(5)
        self.assertEqual(s.top(), 5)
        self.assertEqual(s.pop(), 5)
        self.assertTrue(s.empty())

    def test_lifo_order(self):
        s = MyStack()
        for i in range(1, 6):
            s.push(i)
        for i in range(5, 0, -1):
            self.assertEqual(s.pop(), i)
        self.assertTrue(s.empty())

    def test_interleaved(self):
        s = MyStack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)
        s.push(3)
        self.assertEqual(s.top(), 3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.empty())


if __name__ == "__main__":
    unittest.main()
