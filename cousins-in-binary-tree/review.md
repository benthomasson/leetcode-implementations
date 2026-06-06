# Review: Cousins in Binary Tree

## Solution
- **Approach**: BFS level-order traversal tracking parents for each node; at each level, checks if both target nodes are found with different parents.
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Correctness**: Has Issues - Function name `tallestBillboard` is incorrect (wrong problem); logic is correct.

## Tests
- **Coverage**: Good - Tests cover LeetCode examples, siblings, minimal trees, deep nodes, and full trees.
- **Edge Cases**: Yes - Siblings (same parent), root with child, different depths, minimal tree, deep cousins.

## Plan
- **Quality**: Adequate - Brief as requested for MINIMAL effort; identifies algorithm and notes the function name error.

## Overall
Solution logic is correct but has critical naming bug: function should be `isCousins` not `tallestBillboard` (acknowledged in plan but not fixed). Tests are comprehensive and would pass if the function were called correctly.
