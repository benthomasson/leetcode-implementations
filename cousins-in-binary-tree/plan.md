# Plan (Iteration 1)

Task: Solve the LeetCode problem "cousins-in-binary-tree":

Given the `root` of a binary tree with unique values and the values of two different nodes of the tree `x` and `y`, return `true` _if the nodes corresponding to the values_ `x` _and_ `y` _in the tree are **cousins**, or_ `false` _otherwise._

Two nodes of a binary tree are **cousins** if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth `0`, and children of each depth `k` node are at the depth `k + 1`.

**Example 1:**

**Input:** root = \[1,2,3,4\], x = 4, y = 3
**Output:** false

**Example 2:**

**Input:** root = \[1,2,3,null,4,null,5\], x = 5, y = 4
**Output:** true

**Example 3:**

**Input:** root = \[1,2,3,null,4\], x = 2, y = 3
**Output:** false

**Constraints:**

*   The number of nodes in the tree is in the range `[2, 100]`.
*   `1 <= Node.val <= 100`
*   Each node has a **unique** value.
*   `x != y`
*   `x` and `y` are exist in the tree.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: tallestBillboard

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Summary:

**Algorithm:** BFS level-order traversal, tracking parents. O(n) time/space.

**Key note:** The required function name `tallestBillboard` is clearly a copy-paste error from another problem, but the plan follows the requirement as stated.

**Confidence:** HIGH — straightforward easy-level problem with a clean standard solution.

[Committed changes to planner branch]