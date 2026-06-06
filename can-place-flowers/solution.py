"""Can Place Flowers - Greedy single-pass solution."""


def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    """Determine if n flowers can be planted without adjacent violations.

    Args:
        flowerbed: List of 0s and 1s representing empty/planted plots.
        n: Number of flowers to plant.

    Returns:
        True if n flowers can be planted, False otherwise.
    """
    for i in range(len(flowerbed)):
        if n <= 0:
            return True
        if (flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
            flowerbed[i] = 1
            n -= 1
    return n <= 0
