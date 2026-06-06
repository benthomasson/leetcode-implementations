# Review: Search in a Binary Search Tree

## Solution
- **Approach**: Iterative BST traversal comparing target value with current node, moving left if smaller or right if larger until found or null.
- **Time Complexity**: O(h) where h is tree height; O(log n) average, O(n) worst case
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes problem examples, edge cases (None root, single node, leaf, root as target), and verifies subtree reference identity
- **Edge Cases**: Yes - covers None input, single node (found/not found), boundary values, and both subtrees

## Plan
- **Quality**: Adequate - minimal as specified by effort level, correctly identifies iterative traversal as optimal approach

## Overall
Clean, correct implementation of BST search with comprehensive test coverage. The iterative approach is optimal for both time and space complexity.
