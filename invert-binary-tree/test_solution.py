from solution import invert_tree, TreeNode, list_to_tree, tree_to_list


def test_example1():
    root = list_to_tree([4, 2, 7, 1, 3, 6, 9])
    result = invert_tree(root)
    assert tree_to_list(result) == [4, 7, 2, 9, 6, 3, 1]


def test_example2():
    root = list_to_tree([2, 1, 3])
    result = invert_tree(root)
    assert tree_to_list(result) == [2, 3, 1]


def test_example3_empty():
    result = invert_tree(None)
    assert result is None


def test_single_node():
    root = list_to_tree([1])
    result = invert_tree(root)
    assert tree_to_list(result) == [1]


def test_left_skewed_tree():
    root = list_to_tree([1, 2, None, 3])
    result = invert_tree(root)
    assert tree_to_list(result) == [1, None, 2, None, 3]


def test_right_skewed_tree():
    root = list_to_tree([1, None, 2, None, 3])
    result = invert_tree(root)
    assert tree_to_list(result) == [1, 2, None, 3]


def test_two_nodes_left_only():
    root = list_to_tree([1, 2])
    result = invert_tree(root)
    assert tree_to_list(result) == [1, None, 2]


def test_two_nodes_right_only():
    root = list_to_tree([1, None, 2])
    result = invert_tree(root)
    assert tree_to_list(result) == [1, 2]


def test_larger_balanced_tree():
    root = list_to_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    result = invert_tree(root)
    assert tree_to_list(result) == [1, 3, 2, 7, 6, 5, 4, 15, 14, 13, 12, 11, 10, 9, 8]


def test_negative_values():
    root = list_to_tree([-100, -50, 50, -25, 25, 0, 100])
    result = invert_tree(root)
    assert tree_to_list(result) == [-100, 50, -50, 100, 0, 25, -25]
