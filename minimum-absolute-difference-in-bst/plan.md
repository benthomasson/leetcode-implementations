# Plan (Iteration 1)

Task: Solve the LeetCode problem "minimum-absolute-difference-in-bst":

Given the `root` of a Binary Search Tree (BST), return _the minimum absolute difference between the values of any two different nodes in the tree_.

**Example 1:**

**Input:** root = \[4,2,6,1,3\]
**Output:** 1

**Example 2:**

**Input:** root = \[1,0,48,null,null,12,49\]
**Output:** 1

**Constraints:**

*   The number of nodes in the tree is in the range `[2, 104]`.
*   `0 <= Node.val <= 105`

**Note:** This question is the same as 783: [https://leetcode.com/problems/minimum-distance-between-bst-nodes/](https://leetcode.com/problems/minimum-distance-between-bst-nodes/)

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. 

**Summary:** Use in-order traversal (which visits BST nodes in sorted order), track the previous value, and compute the minimum difference between consecutive pairs. O(n) time, O(h) space. Straightforward and optimal.

[Committed changes to planner branch]