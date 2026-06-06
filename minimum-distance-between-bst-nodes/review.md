# Review: Minimum Distance Between BST Nodes

## Solution
- **Approach**: In-order traversal to visit nodes in sorted order, tracking previous value to compute consecutive differences and maintain minimum.
- **Time Complexity**: O(n)
- **Space Complexity**: O(h) for recursion stack
- **Correctness**: Has Issues - Critical bug with instance variable reuse. `self.prev` and `self.min_diff` are never reset between calls, causing incorrect results on subsequent calls. The `test_reusability` test would fail. Also, function name `searchBST` is misleading (should be something like `minDiffInBST`).

## Tests
- **Coverage**: Good - tests include both examples, two-node edge cases, large gaps, skewed trees, and consecutive values.
- **Edge Cases**: Yes - covers minimum tree size (2 nodes), skewed trees, large value gaps, and reusability (which would actually catch the bug if run).

## Plan
- **Quality**: Adequate - Correctly identifies in-order traversal approach and complexity, but specifies wrong function name that doesn't match problem semantics.

## Overall
The algorithm is correct but has a critical implementation bug: instance variables aren't reset between calls, causing state pollution. Fix by adding `self.prev = None` and `self.min_diff = float('inf')` at the start of `searchBST`. Also rename function to better reflect the problem (e.g., `minDiffInBST`).
