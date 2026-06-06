# Review: Invert Binary Tree

## Solution
- **Approach**: Recursive DFS that swaps left and right children at each node, processing subtrees bottom-up
- **Time Complexity**: O(n)
- **Space Complexity**: O(h) where h is tree height, O(n) worst case for skewed tree
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes all example cases plus edge cases (empty, single node, skewed trees)
- **Edge Cases**: Yes - empty tree, single node, left-skewed, and right-skewed trees all covered

## Plan
- **Quality**: Adequate - brief as requested for MINIMAL effort level, clearly states recursive swap approach

## Overall
Clean, correct recursive solution with proper type hints and comprehensive tests. The implementation elegantly handles all edge cases with a simple base case check. No issues found.
