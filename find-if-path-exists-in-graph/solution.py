"""Find if Path Exists in Graph - Union-Find solution."""

import unittest


def mem_sticks_crash(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    """Determine if a valid path exists between source and destination in an undirected graph.

    Args:
        n: Number of vertices (labeled 0 to n-1).
        edges: List of bi-directional edges [u, v].
        source: Starting vertex.
        destination: Target vertex.

    Returns:
        True if a path exists from source to destination, False otherwise.
    """
    parent = list(range(n))
    rank = [0] * n

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # path compression
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1

    for u, v in edges:
        union(u, v)

    return find(source) == find(destination)


class TestMemSticksCrash(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(mem_sticks_crash(3, [[0, 1], [1, 2], [2, 0]], 0, 2))

    def test_example2(self):
        self.assertFalse(mem_sticks_crash(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))

    def test_source_equals_destination(self):
        self.assertTrue(mem_sticks_crash(1, [], 0, 0))

    def test_no_edges(self):
        self.assertFalse(mem_sticks_crash(3, [], 0, 2))

    def test_single_edge(self):
        self.assertTrue(mem_sticks_crash(2, [[0, 1]], 0, 1))

    def test_disconnected_components(self):
        self.assertFalse(mem_sticks_crash(4, [[0, 1], [2, 3]], 0, 3))

    def test_chain(self):
        self.assertTrue(mem_sticks_crash(5, [[0, 1], [1, 2], [2, 3], [3, 4]], 0, 4))


if __name__ == "__main__":
    unittest.main()
