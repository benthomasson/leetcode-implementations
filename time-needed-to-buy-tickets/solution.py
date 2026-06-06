def time_to_buy_tickets(tickets: list[int], k: int) -> int:
    """Calculate time for person at position k to finish buying tickets.

    Args:
        tickets: Number of tickets each person wants to buy.
        k: Index of the person to track.

    Returns:
        Total seconds until person k finishes buying all their tickets.
    """
    total = 0
    for i, t in enumerate(tickets):
        if i <= k:
            total += min(t, tickets[k])
        else:
            total += min(t, tickets[k] - 1)
    return total
