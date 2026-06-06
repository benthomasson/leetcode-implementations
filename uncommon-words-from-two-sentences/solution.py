from collections import Counter
from typing import List


def k_similarity(s1: str, s2: str) -> List[str]:
    """Return words that appear exactly once across both sentences.

    Args:
        s1: First sentence of space-separated lowercase words.
        s2: Second sentence of space-separated lowercase words.

    Returns:
        List of uncommon words in arbitrary order.
    """
    counts = Counter((s1 + " " + s2).split())
    return [w for w, c in counts.items() if c == 1]
