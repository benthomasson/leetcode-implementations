from solution import binary_tree_paths, TreeNode


def build_tree(values):
    """Build a binary tree from level-order list representation."""
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def test_example1():
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
    result = binary_tree_paths(root)
    assert sorted(result) == sorted(["1->2->5", "1->3"])


def test_example2_single_node():
    root = TreeNode(1)
    assert binary_tree_paths(root) == ["1"]


def test_empty_tree():
    assert binary_tree_paths(None) == []


def test_left_skewed_tree():
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert binary_tree_paths(root) == ["1->2->3->4"]


def test_right_skewed_tree():
    root = TreeNode(5, None, TreeNode(4, None, TreeNode(3, None, TreeNode(2))))
    assert binary_tree_paths(root) == ["5->4->3->2"]


def test_balanced_tree():
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    result = binary_tree_paths(root)
    assert sorted(result) == sorted(["1->2->4", "1->2->5", "1->3->6", "1->3->7"])


def test_negative_values():
    root = TreeNode(-10, TreeNode(-20), TreeNode(-30))
    result = binary_tree_paths(root)
    assert sorted(result) == sorted(["-10->-20", "-10->-30"])


def test_mixed_values():
    root = TreeNode(0, TreeNode(-100, TreeNode(50)), TreeNode(100))
    result = binary_tree_paths(root)
    assert sorted(result) == sorted(["0->-100->50", "0->100"])


def test_complete_tree():
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    result = binary_tree_paths(root)
    expected = ["1->2->4", "1->2->5", "1->3->6", "1->3->7"]
    assert sorted(result) == sorted(expected)


def test_large_tree():
    root = TreeNode(
        10,
        TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(7, TreeNode(6), TreeNode(8))),
        TreeNode(15, TreeNode(12, TreeNode(11), TreeNode(13)), TreeNode(20, TreeNode(18), TreeNode(25)))
    )
    result = binary_tree_paths(root)
    expected = [
        "10->5->3->1",
        "10->5->3->4",
        "10->5->7->6",
        "10->5->7->8",
        "10->15->12->11",
        "10->15->12->13",
        "10->15->20->18",
        "10->15->20->25"
    ]
    assert sorted(result) == sorted(expected)
