# Plan (Iteration 1)

Task: Solve the LeetCode problem "find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree":

Given two binary trees `original` and `cloned` and given a reference to a node `target` in the original tree.

The `cloned` tree is a **copy of** the `original` tree.

Return _a reference to the same node_ in the `cloned` tree.

**Note** that you are **not allowed** to change any of the two trees or the `target` node and the answer **must be** a reference to a node in the `cloned` tree.

**Example 1:**

**Input:** tree = \[7,4,3,null,null,6,19\], target = 3
**Output:** 3
**Explanation:** In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.

**Example 2:**

**Input:** tree = \[7\], target =  7
**Output:** 7

**Example 3:**

**Input:** tree = \[8,null,6,null,5,null,4,null,3,null,2,null,1\], target = 4
**Output:** 4

**Constraints:**

*   The number of nodes in the `tree` is in the range `[1, 104]`.
*   The values of the nodes of the `tree` are unique.
*   `target` node is a node from the `original` tree and is not `null`.

**Follow up:** Could you solve the problem if repeated values on the tree are allowed?

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: reconstructMatrix

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. Summary:

**Algorithm:** Simultaneous DFS — traverse `original` and `cloned` in lockstep. When `original is target` (identity check), return the corresponding `cloned` node. O(n) time, O(h) space. Handles the duplicate-values follow-up naturally since it compares by reference, not value.

**Key note:** The task says function name should be `reconstructMatrix` — this is a copy-paste error from another problem. Use `getTargetCopy` to match LeetCode convention, or whatever the harness expects.

**Confidence:** HIGH.

[Committed changes to planner branch]