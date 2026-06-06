# Plan (Iteration 1)

Task: Solve the LeetCode problem "n-ary-tree-postorder-traversal":

Given the `root` of an n-ary tree, return _the postorder traversal of its nodes' values_.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

**Example 1:**

**Input:** root = \[1,null,3,2,4,null,5,6\]
**Output:** \[5,6,3,2,4,1\]

**Example 2:**

**Input:** root = \[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14\]
**Output:** \[2,6,14,11,7,3,12,8,4,13,9,10,5,1\]

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 104]`.
*   `0 <= Node.val <= 104`
*   The height of the n-ary tree is less than or equal to `1000`.

**Follow up:** Recursive solution is trivial, could you do it iteratively?

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: postorder

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. Summary:

- **Algorithm:** Iterative stack — push node, push children left-to-right, collect values, reverse at end. O(n) time/space.
- **Steps:** Define `Node`, implement `postorder` iteratively, write 6 test cases.
- **Confidence:** HIGH — classic well-known pattern.

[Committed changes to planner branch]