# Plan (Iteration 1)

Task: Solve the LeetCode problem "symmetric-tree":

Given the `root` of a binary tree, _check whether it is a mirror of itself_ (i.e., symmetric around its center).

**Example 1:**

**Input:** root = \[1,2,2,3,4,4,3\]
**Output:** true

**Example 2:**

**Input:** root = \[1,2,2,null,3,null,3\]
**Output:** false

**Constraints:**

*   The number of nodes in the tree is in the range `[1, 1000]`.
*   `-100 <= Node.val <= 100`

**Follow up:** Could you solve it both recursively and iteratively?

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: isSymmetric

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. This is a straightforward classic problem — recursive mirror comparison is the standard optimal approach, with an iterative deque variant for the follow-up.

[Committed changes to planner branch]