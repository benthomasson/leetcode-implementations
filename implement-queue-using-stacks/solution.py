class MyQueue:
    """FIFO queue implemented using two stacks with amortized O(1) operations."""

    def __init__(self):
        self._in_stack: list[int] = []
        self._out_stack: list[int] = []

    def push(self, x: int) -> None:
        """Push element to back of queue."""
        self._in_stack.append(x)

    def pop(self) -> int:
        """Remove and return front element."""
        self._transfer()
        return self._out_stack.pop()

    def peek(self) -> int:
        """Return front element without removing."""
        self._transfer()
        return self._out_stack[-1]

    def empty(self) -> bool:
        """Return True if queue is empty."""
        return not self._in_stack and not self._out_stack

    def _transfer(self) -> None:
        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())
