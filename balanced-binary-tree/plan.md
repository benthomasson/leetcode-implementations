# Plan (Iteration 1)

Task: Solve the LeetCode problem "balanced-binary-tree":

Given a binary tree, determine if it is **height-balanced**.

**Example 1:**

**Input:** root = \[3,9,20,null,null,15,7\]
**Output:** true

**Example 2:**

**Input:** root = \[1,2,2,3,3,null,null,4,4\]
**Output:** false

**Example 3:**

**Input:** root = \[\]
**Output:** true

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 5000]`.
*   `-104 <= Node.val <= 104`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: getHeight

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `/workspaces/balanced-binary-tree/planner/PLAN.md`. 

**Summary:** Use bottom-up DFS via `getHeight` returning `-1` for unbalanced subtrees. O(n) time, O(h) space. Straightforward implementation with standard `TreeNode` class, wrapper `isBalanced`, and tests covering all examples plus edge cases. High confidence.

[Committed changes to planner branch]