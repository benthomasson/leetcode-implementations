# Plan (Iteration 1)

Task: Solve the LeetCode problem "merge-two-sorted-lists":

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return _the head of the merged linked list_.

**Example 1:**

**Input:** list1 = \[1,2,4\], list2 = \[1,3,4\]
**Output:** \[1,1,2,3,4,4\]

**Example 2:**

**Input:** list1 = \[\], list2 = \[\]
**Output:** \[\]

**Example 3:**

**Input:** list1 = \[\], list2 = \[0\]
**Output:** \[0\]

**Constraints:**

*   The number of nodes in both lists is in the range `[0, 50]`.
*   `-100 <= Node.val <= 100`
*   Both `list1` and `list2` are sorted in **non-decreasing** order.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: merge_two_lists

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The approach is straightforward: iterative merge with a dummy head, O(n+m) time, O(1) space. Ready for the implementer.

[Committed changes to planner branch]