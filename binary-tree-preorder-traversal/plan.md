# Plan (Iteration 1)

Task: Solve the LeetCode problem "binary-tree-preorder-traversal":

Given the `root` of a binary tree, return _the preorder traversal of its nodes' values_.

**Example 1:**

**Input:** root = \[1,null,2,3\]
**Output:** \[1,2,3\]

**Example 2:**

**Input:** root = \[\]
**Output:** \[\]

**Example 3:**

**Input:** root = \[1\]
**Output:** \[1\]

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 100]`.
*   `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: preorderTraversal

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The iterative stack approach is the right call here — it directly addresses the follow-up question and is clean to implement.

[Committed changes to planner branch]