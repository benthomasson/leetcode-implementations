from collections import deque


class MovingAverage:
    """Calculates moving average over a sliding window of integers."""

    def __init__(self, size: int):
        self._queue: deque[int] = deque(maxlen=size)
        self._sum = 0

    def next(self, val: int) -> float:
        """Adds val to the stream and returns the current moving average."""
        if len(self._queue) == self._queue.maxlen:
            self._sum -= self._queue[0]
        self._queue.append(val)
        self._sum += val
        return self._sum / len(self._queue)
