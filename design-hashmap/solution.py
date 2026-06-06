"""Design HashMap using separate chaining."""


class MyHashMap:
    """HashMap implementation using separate chaining with a fixed bucket array."""

    def __init__(self) -> None:
        self._size = 1009
        self._buckets: list[list[list[int]]] = [[] for _ in range(self._size)]

    def _hash(self, key: int) -> int:
        return key % self._size

    def put(self, key: int, value: int) -> None:
        """Insert or update a key-value pair."""
        bucket = self._buckets[self._hash(key)]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def get(self, key: int) -> int:
        """Return value for key, or -1 if not found."""
        for pair in self._buckets[self._hash(key)]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        """Remove key and its value if present."""
        bucket = self._buckets[self._hash(key)]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                return
