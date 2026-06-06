# Review: Range Sum of BST

## Solution
- **Approach**: Recursive BST traversal with pruning—searches only left subtree when root > high, only right when root < low, otherwise includes root and searches both subtrees.
- **Time Complexity**: O(n) worst case, but O(k + log n) average when k nodes are in range due to BST pruning
- **Space Complexity**: O(h) for recursion stack, where h is tree height
- **Correctness**: Correct

## Tests
- **Coverage**: Good—includes both examples, empty tree, single node cases, boundary values, all/none in range, and skewed trees
- **Edge Cases**: Yes—covers empty tree, single nodes at boundaries (equal to low/high), nodes outside range, and skewed tree structures

## Plan
- **Quality**: Adequate—brief as requested for minimal effort level, correctly identifies function naming discrepancy from requirements

## Overall
Solution is correct and optimal for BST structure. Tests have strong coverage including edge cases. Minor redundancy: tests are duplicated in both solution.py and test_solution.py.
