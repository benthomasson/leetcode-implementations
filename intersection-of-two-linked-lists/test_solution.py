from solution import ListNode, Solution


def make_lists(vals_a, vals_b, shared_vals):
    """Build two lists that share a common tail."""
    shared = None
    for v in reversed(shared_vals):
        node = ListNode(v)
        node.next = shared
        shared = node

    head_a = shared
    for v in reversed(vals_a):
        node = ListNode(v)
        node.next = head_a
        head_a = node

    head_b = shared
    for v in reversed(vals_b):
        node = ListNode(v)
        node.next = head_b
        head_b = node

    return head_a, head_b, shared


def test_example1():
    head_a, head_b, intersection = make_lists([4, 1], [5, 6, 1], [8, 4, 5])
    assert Solution().getIntersectionNode(head_a, head_b) is intersection


def test_example2():
    head_a, head_b, intersection = make_lists([1, 9, 1], [3], [2, 4])
    assert Solution().getIntersectionNode(head_a, head_b) is intersection


def test_no_intersection():
    head_a, head_b, _ = make_lists([2, 6, 4], [1, 5], [])
    assert Solution().getIntersectionNode(head_a, head_b) is None


def test_intersection_at_head():
    head_a, head_b, intersection = make_lists([], [], [1, 2, 3])
    assert Solution().getIntersectionNode(head_a, head_b) is intersection


def test_intersection_at_tail():
    head_a, head_b, intersection = make_lists([1, 2], [3, 4, 5], [99])
    assert Solution().getIntersectionNode(head_a, head_b) is intersection


def test_single_node_intersection():
    node = ListNode(1)
    assert Solution().getIntersectionNode(node, node) is node


def test_different_lengths_no_intersection():
    a = ListNode(1)
    a.next = ListNode(2)
    b = ListNode(3)
    assert Solution().getIntersectionNode(a, b) is None
