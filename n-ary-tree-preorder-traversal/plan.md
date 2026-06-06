# Plan (Iteration 1)

Task: Solve the LeetCode problem "n-ary-tree-preorder-traversal":

Given the `root` of an n-ary tree, return _the preorder traversal of its nodes' values_.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

**Example 1:**

**Input:** root = \[1,null,3,2,4,null,5,6\]
**Output:** \[1,3,5,6,2,4\]

**Example 2:**

**Input:** root = \[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14\]
**Output:** \[1,2,3,6,7,11,14,4,8,12,5,9,13,10\]

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
- Function name should be: preorder

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Summary: Use an iterative stack-based preorder traversal — pop a node, record its value, push its children in reverse order. Define `Node` class, implement `preorder()`, and write tests covering empty tree, single node, both examples, deep chains, and wide trees.

[Committed changes to planner branch]