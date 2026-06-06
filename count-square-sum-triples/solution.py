class Solution:
    def countTriples(self, n: int) -> int:
        """Count square triples (a,b,c) where a² + b² = c² and 1 ≤ a,b,c ≤ n.

        Args:
            n: Upper bound for triple values.

        Returns:
            Number of valid square triples.
        """
        squares = {i * i for i in range(1, n + 1)}
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                s = a * a + b * b
                if s in squares:
                    count += 1
        return count
