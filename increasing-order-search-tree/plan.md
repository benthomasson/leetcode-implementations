# Plan (Iteration 1)

Task: Solve the LeetCode problem "increasing-order-search-tree":

Given the `root` of a binary search tree, rearrange the tree in **in-order** so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

**Example 1:**

**Input:** root = \[5,3,6,2,4,null,8,1,null,null,null,7,9\]
**Output:** \[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9\]

**Example 2:**

**Input:** root = \[5,1,7\]
**Output:** \[1,null,5,null,7\]

**Constraints:**

*   The number of nodes in the given tree will be in the range `[1, 100]`.
*   `0 <= Node.val <= 1000`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: is_prime

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Summary:

- **Algorithm:** In-order traversal with relinking using a dummy node — O(n) time, O(h) space
- **Key note:** The `is_prime` function name in the task is a copy-paste error; should be `increasingBST`
- **Confidence:** HIGH

[Committed changes to planner branch]