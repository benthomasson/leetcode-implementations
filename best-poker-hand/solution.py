from collections import Counter


def best_poker_hand(ranks: list[int], suits: list[str]) -> str:
    """Determine the best poker hand from 5 cards.

    Args:
        ranks: List of 5 card ranks (1-13).
        suits: List of 5 card suits ('a'-'d').

    Returns:
        String representing the best hand type.
    """
    if len(set(suits)) == 1:
        return "Flush "

    max_freq = max(Counter(ranks).values())
    if max_freq >= 3:
        return "Three of a Kind "
    if max_freq == 2:
        return "Pair "
    return "High Card "
