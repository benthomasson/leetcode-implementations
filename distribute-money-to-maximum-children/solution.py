"""Distribute Money to Maximum Children."""

import unittest


def maximum_children_with_eight_dollars(money: int, children: int) -> int:
    """Return max children who can receive exactly $8.

    Args:
        money: Total dollars to distribute.
        children: Number of children to distribute to.

    Returns:
        Max children receiving exactly $8, or -1 if distribution is impossible.
    """
    if money < children:
        return -1

    remaining = money - children  # after giving $1 to each child
    eights = min(remaining // 7, children)

    leftover = remaining - eights * 7
    others = children - eights

    # If everyone gets $8 but there's surplus, one child must take extra
    if eights == children and leftover > 0:
        eights -= 1

    # If exactly 1 child left and leftover is exactly 3, that child gets $4 (1+3)
    elif others == 1 and leftover == 3:
        eights -= 1

    return eights


class TestMaximumChildrenWithEightDollars(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(maximum_children_with_eight_dollars(20, 3), 1)

    def test_example2(self):
        self.assertEqual(maximum_children_with_eight_dollars(16, 2), 2)

    def test_impossible(self):
        self.assertEqual(maximum_children_with_eight_dollars(1, 2), -1)

    def test_exact_minimum(self):
        self.assertEqual(maximum_children_with_eight_dollars(2, 2), 0)

    def test_all_get_eight_exact(self):
        self.assertEqual(maximum_children_with_eight_dollars(24, 3), 3)

    def test_surplus_when_all_eight(self):
        self.assertEqual(maximum_children_with_eight_dollars(17, 2), 1)

    def test_avoid_four_dollars(self):
        # 2 children, $12: eights=1, other gets 1+3=4 -> must reduce
        self.assertEqual(maximum_children_with_eight_dollars(12, 2), 0)

    def test_single_child_not_four(self):
        # 3 children, $23: remaining=20, eights=2, leftover=6, others=1 -> ok
        self.assertEqual(maximum_children_with_eight_dollars(23, 3), 2)

    def test_min_constraints(self):
        self.assertEqual(maximum_children_with_eight_dollars(1, 2), -1)

    def test_large_money_few_children(self):
        self.assertEqual(maximum_children_with_eight_dollars(200, 2), 1)

    def test_many_children_little_money(self):
        self.assertEqual(maximum_children_with_eight_dollars(30, 30), 0)


if __name__ == "__main__":
    unittest.main()
