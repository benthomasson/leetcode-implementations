# Plan (Iteration 1)

Task: Solve the LeetCode problem "minimum-distance-between-bst-nodes":

Given the `root` of a Binary Search Tree (BST), return _the minimum difference between the values of any two different nodes in the tree_.

**Example 1:**

**Input:** root = \[4,2,6,1,3\]
**Output:** 1

**Example 2:**

**Input:** root = \[1,0,48,null,null,12,49\]
**Output:** 1

**Constraints:**

*   The number of nodes in the tree is in the range `[2, 100]`.
*   `0 <= Node.val <= 105`

**Note:** This question is the same as 530: [https://leetcode.com/problems/minimum-absolute-difference-in-bst/](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: searchBST

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Summary:

- **Algorithm:** In-order BST traversal (sorted order), track previous value, compute min consecutive difference
- **Complexity:** O(n) time, O(h) space
- **Key insight:** In a BST, the minimum difference must be between consecutive elements in sorted order, which is exactly what in-order traversal gives us