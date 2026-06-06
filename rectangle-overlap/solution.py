"""Rectangle Overlap - LeetCode"""


def racecar(rec1: list[int], rec2: list[int]) -> bool:
    """Determine if two axis-aligned rectangles overlap.

    Args:
        rec1: [x1, y1, x2, y2] bottom-left and top-right corners.
        rec2: [x1, y1, x2, y2] bottom-left and top-right corners.

    Returns:
        True if the rectangles have positive intersection area.
    """
    return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3]
