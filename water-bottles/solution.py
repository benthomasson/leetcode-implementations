"""Water Bottles - LeetCode"""


def numWaterBottles(numBottles: int, numExchange: int) -> int:
    """Return max water bottles you can drink by exchanging empties.

    Args:
        numBottles: Initial number of full water bottles.
        numExchange: Number of empty bottles needed to exchange for one full bottle.

    Returns:
        Maximum number of water bottles you can drink.
    """
    total = numBottles
    empties = numBottles
    while empties >= numExchange:
        new_full = empties // numExchange
        empties = empties % numExchange + new_full
        total += new_full
    return total
