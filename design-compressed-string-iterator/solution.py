"""Design Compressed String Iterator."""

import unittest


class StringIterator:
    """Iterator over a compressed string like 'L1e2t1C1o1d1e1'."""

    def __init__(self, compressedString: str):
        self._s = compressedString
        self._i = 0
        self._char = ' '
        self._count = 0
        self._extract_next()

    def _extract_next(self):
        """Parse the next (char, count) pair from the compressed string."""
        if self._i >= len(self._s):
            self._char = ' '
            self._count = 0
            return
        self._char = self._s[self._i]
        self._i += 1
        j = self._i
        while j < len(self._s) and self._s[j].isdigit():
            j += 1
        self._count = int(self._s[self._i:j])
        self._i = j

    def next(self) -> str:
        """Return the next character, or ' ' if exhausted."""
        if not self.hasNext():
            return ' '
        ch = self._char
        self._count -= 1
        if self._count == 0:
            self._extract_next()
        return ch

    def hasNext(self) -> bool:
        """Return True if there are uncompressed characters remaining."""
        return self._count > 0


class TestStringIterator(unittest.TestCase):
    def test_basic_example(self):
        it = StringIterator("L1e2t1C1o1d1e1")
        self.assertEqual(it.next(), 'L')
        self.assertEqual(it.next(), 'e')
        self.assertEqual(it.next(), 'e')
        self.assertEqual(it.next(), 't')
        self.assertEqual(it.next(), 'C')
        self.assertEqual(it.next(), 'o')
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 'd')
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 'e')
        self.assertFalse(it.hasNext())

    def test_single_char(self):
        it = StringIterator("a1")
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 'a')
        self.assertFalse(it.hasNext())
        self.assertEqual(it.next(), ' ')

    def test_large_count(self):
        it = StringIterator("a1000000000")
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 'a')
        self.assertTrue(it.hasNext())

    def test_multi_digit_counts(self):
        it = StringIterator("a12b3")
        for _ in range(12):
            self.assertEqual(it.next(), 'a')
        for _ in range(3):
            self.assertEqual(it.next(), 'b')
        self.assertFalse(it.hasNext())

    def test_mixed_case(self):
        it = StringIterator("A1b2C3")
        self.assertEqual(it.next(), 'A')
        self.assertEqual(it.next(), 'b')
        self.assertEqual(it.next(), 'b')
        self.assertEqual(it.next(), 'C')
        self.assertEqual(it.next(), 'C')
        self.assertEqual(it.next(), 'C')
        self.assertFalse(it.hasNext())

    def test_exhausted_returns_space(self):
        it = StringIterator("x1")
        it.next()
        self.assertEqual(it.next(), ' ')
        self.assertEqual(it.next(), ' ')

    def test_has_next_does_not_consume(self):
        it = StringIterator("z2")
        self.assertTrue(it.hasNext())
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 'z')
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 'z')
        self.assertFalse(it.hasNext())


if __name__ == '__main__':
    unittest.main()
