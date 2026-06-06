# Review: Binary Tree Paths

## Solution
- **Approach**: Recursive DFS traversal building path strings by appending node values with "->" separators. When a leaf is reached, the complete path is added to results.
- **Time Complexity**: O(n) - visits each node once
- **Space Complexity**: O(h) for recursion stack where h is tree height, plus O(n) for storing paths
- **Correctness**: Correct

## Tests
- **Coverage**: Good - covers standard cases, edge cases, and boundary conditions
- **Edge Cases**: Yes - empty tree (None), single node, skewed trees (left/right), negative values, and balanced trees all tested

## Plan
- **Quality**: Adequate - brief but correctly identifies recursive DFS approach, appropriate for minimal effort level

## Overall
Clean, correct implementation with comprehensive test coverage. The DFS approach efficiently generates all root-to-leaf paths, and the tests verify behavior across diverse tree structures including edge cases.
