# Plan (Iteration 1)

Task: Solve the LeetCode problem "remove-duplicates-from-sorted-list":

Given the `head` of a sorted linked list, _delete all duplicates such that each element appears only once_. Return _the linked list **sorted** as well_.

**Example 1:**

**Input:** head = \[1,1,2\]
**Output:** \[1,2\]

**Example 2:**

**Input:** head = \[1,1,2,3,3\]
**Output:** \[1,2,3\]

**Constraints:**

*   The number of nodes in the list is in the range `[0, 300]`.
*   `-100 <= Node.val <= 100`
*   The list is guaranteed to be **sorted** in ascending order.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: delete_duplicates

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. Single-pass in-place pointer traversal — O(n) time, O(1) space. Straightforward problem, high confidence.

[Committed changes to planner branch]