"""Best Time to Buy and Sell Stock."""


def maxProfit(prices: list[int]) -> int:
    """Find max profit from a single buy-sell transaction.

    Args:
        prices: Stock prices where prices[i] is the price on day i.

    Returns:
        Maximum profit achievable, or 0 if no profit possible.
    """
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit
