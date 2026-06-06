class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        """Flip each row horizontally then invert all values.

        Args:
            image: n x n binary matrix.

        Returns:
            The flipped and inverted image.
        """
        for row in image:
            lo, hi = 0, len(row) - 1
            while lo <= hi:
                row[lo], row[hi] = row[hi] ^ 1, row[lo] ^ 1
                lo += 1
                hi -= 1
        return image
