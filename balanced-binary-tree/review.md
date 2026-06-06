# Review: Balanced Binary Tree

## Solution
- **Approach**: Bottom-up DFS where `getHeight` returns -1 for unbalanced subtrees and actual height otherwise, propagating unbalanced state upward.
- **Time Complexity**: O(n)
- **Space Complexity**: O(h)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes all LeetCode examples, edge cases (empty, single node, chains, perfect tree, boundary height difference), and direct `getHeight` testing
- **Edge Cases**: Yes - empty tree, single node, left/right chains (unbalanced), height difference of exactly 1 (balanced)

## Plan
- **Quality**: Good - clearly describes bottom-up DFS approach with O(n) time and O(h) space, appropriate detail for minimal effort level

## Overall
Clean, correct implementation with comprehensive test coverage. No bugs detected. The solution efficiently handles all edge cases and the dual test file structure (in-file and separate) provides thorough validation.
