"""Minimum Recolors to Get K Consecutive Black Blocks."""


def min_operations(blocks: str, k: int) -> int:
    """Return minimum recolors needed for k consecutive black blocks.

    Args:
        blocks: String of 'W' and 'B' characters.
        k: Desired number of consecutive black blocks.

    Returns:
        Minimum number of white blocks to recolor.
    """
    # Count W's in the first window
    white_count = blocks[:k].count("W")
    min_ops = white_count

    # Slide the window
    for i in range(k, len(blocks)):
        white_count += (blocks[i] == "W") - (blocks[i - k] == "W")
        min_ops = min(min_ops, white_count)

    return min_ops
