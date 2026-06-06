"""Tests for Sum of Root To Leaf Binary Numbers."""

import pytest

from solution import Solution, TreeNode, build_tree


@pytest.fixture
def sol() -> Solution:
    return Solution()


class TestSumRootToLeaf:
    """Core functionality tests."""

    def test_example_1(self, sol: Solution) -> None:
        """[1,0,1,0,1,0,1] -> paths 100,101,110,111 -> 4+5+6+7 = 22."""
        root = build_tree([1, 0, 1, 0, 1, 0, 1])
        assert sol.sumRootToLeaf(root) == 22

    def test_example_2(self, sol: Solution) -> None:
        """Single node [0] -> 0."""
        root = build_tree([0])
        assert sol.sumRootToLeaf(root) == 0

    def test_single_node_one(self, sol: Solution) -> None:
        """Single node [1] -> 1."""
        root = build_tree([1])
        assert sol.sumRootToLeaf(root) == 1

    def test_none_root(self, sol: Solution) -> None:
        """None root should return 0."""
        assert sol.sumRootToLeaf(None) == 0

    def test_left_skewed(self, sol: Solution) -> None:
        """Left-skewed tree: 1 -> 0 -> 1 = binary 101 = 5."""
        root = TreeNode(1, TreeNode(0, TreeNode(1)))
        assert sol.sumRootToLeaf(root) == 5

    def test_right_skewed(self, sol: Solution) -> None:
        """Right-skewed tree: 1 -> 1 -> 0 = binary 110 = 6."""
        root = TreeNode(1, None, TreeNode(1, None, TreeNode(0)))
        assert sol.sumRootToLeaf(root) == 6

    def test_all_zeros(self, sol: Solution) -> None:
        """Complete tree of all zeros -> every path is 0."""
        root = build_tree([0, 0, 0])
        assert sol.sumRootToLeaf(root) == 0

    def test_all_ones(self, sol: Solution) -> None:
        """[1,1,1] -> paths 11, 11 -> 3 + 3 = 6."""
        root = build_tree([1, 1, 1])
        assert sol.sumRootToLeaf(root) == 6

    def test_unbalanced_tree(self, sol: Solution) -> None:
        """Tree with missing right child on left subtree.

            1
           / \\
          0   1
         /
        1
        Paths: 1->0->1 = 101 = 5, 1->1 = 11 = 3. Sum = 8.
        """
        root = TreeNode(1, TreeNode(0, TreeNode(1)), TreeNode(1))
        assert sol.sumRootToLeaf(root) == 8

    def test_deeper_tree(self, sol: Solution) -> None:
        """Deeper 4-level tree.

              1
             / \\
            0   1
           / \\
          1   0
        Paths: 1->0->1 = 101 = 5, 1->0->0 = 100 = 4, 1->1 = 11 = 3.
        Sum = 12.
        """
        root = TreeNode(
            1,
            TreeNode(0, TreeNode(1), TreeNode(0)),
            TreeNode(1),
        )
        assert sol.sumRootToLeaf(root) == 12


class TestBuildTree:
    """Tests for the build_tree helper."""

    def test_empty_list(self) -> None:
        assert build_tree([]) is None

    def test_single_element(self) -> None:
        root = build_tree([1])
        assert root is not None
        assert root.val == 1
        assert root.left is None
        assert root.right is None

    def test_complete_tree(self) -> None:
        root = build_tree([1, 0, 1])
        assert root is not None
        assert root.val == 1
        assert root.left is not None and root.left.val == 0
        assert root.right is not None and root.right.val == 1

    def test_with_none_values(self) -> None:
        """[1, None, 1] -> root has no left child, right child is 1."""
        root = build_tree([1, None, 1])
        assert root is not None
        assert root.left is None
        assert root.right is not None and root.right.val == 1
