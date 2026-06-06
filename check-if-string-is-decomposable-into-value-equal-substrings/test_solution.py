import pytest
from solution import is_decomposable_into_value_equal_substrings


@pytest.mark.parametrize("s, expected", [
    # Problem examples
    ("000111000", False),       # All length-3, no length-2
    ("00011111222", True),      # 000|111|11|222
    ("011100022233", False),    # Leading '0' alone → remainder 1
    # Edge: single group
    ("00", True),               # Exactly one length-2
    ("0", False),               # Length 1 → remainder 1
    ("000", False),             # Only length-3, no length-2
    # Edge: remainder combos
    ("00000", True),            # 000|00 → one remainder-2
    ("0000", False),            # 4 % 3 = 1 → impossible
    # Edge: two remainder-2 groups → False
    ("112233", False),          # 11|22|33 → three remainder-2 groups
    # Edge: long valid string
    ("33322211", True),         # 333|222|11
])
def test_is_decomposable_into_value_equal_substrings(s, expected):
    assert is_decomposable_into_value_equal_substrings(s) == expected
