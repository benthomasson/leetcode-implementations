import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import MyQueue


def test_leetcode_example():
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() is False


def test_single_element():
    q = MyQueue()
    q.push(5)
    assert q.peek() == 5
    assert q.pop() == 5
    assert q.empty() is True


def test_fifo_order():
    q = MyQueue()
    for i in range(1, 6):
        q.push(i)
    for i in range(1, 6):
        assert q.pop() == i
    assert q.empty() is True


def test_interleaved_push_pop():
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.pop() == 1
    q.push(3)
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.empty() is True


def test_peek_does_not_remove():
    q = MyQueue()
    q.push(7)
    assert q.peek() == 7
    assert q.peek() == 7
    assert q.empty() is False
    assert q.pop() == 7
    assert q.empty() is True


def test_push_after_drain():
    q = MyQueue()
    q.push(1)
    q.pop()
    assert q.empty() is True
    q.push(2)
    assert q.empty() is False
    assert q.peek() == 2


def test_empty_on_new_queue():
    q = MyQueue()
    assert q.empty() is True


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v'])
