"""Tests for MyHashMap."""

from solution import MyHashMap


def test_example():
    m = MyHashMap()
    m.put(1, 1)
    m.put(2, 2)
    assert m.get(1) == 1
    assert m.get(3) == -1
    m.put(2, 1)
    assert m.get(2) == 1
    m.remove(2)
    assert m.get(2) == -1


def test_empty_map():
    m = MyHashMap()
    assert m.get(0) == -1
    assert m.get(999999) == -1


def test_update_existing_key():
    m = MyHashMap()
    m.put(1, 10)
    assert m.get(1) == 10
    m.put(1, 20)
    assert m.get(1) == 20


def test_remove_nonexistent():
    m = MyHashMap()
    m.remove(5)  # should not raise


def test_boundary_values():
    m = MyHashMap()
    m.put(0, 0)
    m.put(1000000, 1000000)
    assert m.get(0) == 0
    assert m.get(1000000) == 1000000


def test_collision_handling():
    m = MyHashMap()
    # Keys that hash to the same bucket (mod 1009)
    m.put(0, 100)
    m.put(1009, 200)
    m.put(2018, 300)
    assert m.get(0) == 100
    assert m.get(1009) == 200
    assert m.get(2018) == 300
    m.remove(1009)
    assert m.get(1009) == -1
    assert m.get(0) == 100
    assert m.get(2018) == 300


def test_remove_and_reinsert():
    m = MyHashMap()
    m.put(5, 50)
    m.remove(5)
    assert m.get(5) == -1
    m.put(5, 99)
    assert m.get(5) == 99
