# Plan (Iteration 1)

Task: Solve the LeetCode problem "remove-linked-list-elements":

Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return _the new head_.

**Example 1:**

**Input:** head = \[1,2,6,3,4,5,6\], val = 6
**Output:** \[1,2,3,4,5\]

**Example 2:**

**Input:** head = \[\], val = 1
**Output:** \[\]

**Example 3:**

**Input:** head = \[7,7,7,7\], val = 7
**Output:** \[\]

**Constraints:**

*   The number of nodes in the list is in the range `[0, 104]`.
*   `1 <= Node.val <= 50`
*   `0 <= val <= 50`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: remove_elements

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The dummy node approach is the right call here — it's the cleanest O(n)/O(1) solution and eliminates all head-removal edge cases.

[Committed changes to planner branch]