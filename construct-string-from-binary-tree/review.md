# Review: Construct String from Binary Tree

## Solution
- **Approach**: Recursive preorder DFS that stringifies each node's value and appends `(left)` and `(right)` with conditional omission—right `()` omitted when right is null, left `()` kept when left is null but right exists.
- **Time Complexity**: O(n)
- **Space Complexity**: O(h) recursion stack, O(n) worst case
- **Correctness**: Correct

## Tests
- **Coverage**: Good—includes problem examples, null root, single node, left-only, right-only, negative values, zero, deep chain, and boundary values.
- **Edge Cases**: Yes—covers critical case of right-only child requiring empty `()` for left, negative/zero values, and boundary constraints.

## Plan
- **Quality**: Good—brief as requested for minimal effort level, correctly identifies recursive approach and omission rules with accurate complexity analysis.

## Overall
Solution is correct and efficiently implemented. Tests are comprehensive with excellent edge case coverage, particularly the right-only child scenario. No bugs or improvements needed.
