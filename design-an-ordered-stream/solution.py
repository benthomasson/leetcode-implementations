"""LeetCode: Design an Ordered Stream."""

from typing import List


class OrderedStream:
    """Stream that returns values in increasing order of their IDs.

    Args:
        n: Number of values the stream will take.
    """

    def __init__(self, n: int):
        self.stream = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        """Insert a (idKey, value) pair and return the next contiguous chunk.

        Args:
            idKey: Integer ID between 1 and n.
            value: String value to insert.

        Returns:
            Largest contiguous chunk of values starting from the current pointer.
        """
        self.stream[idKey - 1] = value
        result = []
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            result.append(self.stream[self.ptr])
            self.ptr += 1
        return result
