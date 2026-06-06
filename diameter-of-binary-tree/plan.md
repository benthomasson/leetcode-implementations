# Plan (Iteration 1)

Task: Solve the LeetCode problem "diameter-of-binary-tree":

Given the `root` of a binary tree, return _the length of the **diameter** of the tree_.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.

**Example 1:**

**Input:** root = \[1,2,3,4,5\]
**Output:** 3
**Explanation:** 3 is the length of the path \[4,2,1,3\] or \[5,2,1,3\].

**Example 2:**

**Input:** root = \[1,2\]
**Output:** 1

**Constraints:**

*   The number of nodes in the tree is in the range `[1, 104]`.
*   `-100 <= Node.val <= 100`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: diameter_of_binary_tree

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Straightforward DFS problem — the implementer should have no issues with this.

[Committed changes to planner branch]