# Plan (Iteration 1)

Task: Solve the LeetCode problem "convert-sorted-array-to-binary-search-tree":

Given an integer array `nums` where the elements are sorted in **ascending order**, convert _it to a_ **_height-balanced_** _binary search tree_.

**Example 1:**

**Input:** nums = \[-10,-3,0,5,9\]
**Output:** \[0,-3,9,-10,null,5\]
**Explanation:** \[0,-10,5,null,-3,null,9\] is also accepted:
 

**Example 2:**

**Input:** nums = \[1,3\]
**Output:** \[3,1\]
**Explanation:** \[1,null,3\] and \[3,1\] are both height-balanced BSTs.

**Constraints:**

*   `1 <= nums.length <= 104`
*   `-104 <= nums[i] <= 104`
*   `nums` is sorted in a **strictly increasing** order.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: sorted_array_to_bst

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Straightforward recursive mid-point selection — no surprises here.

[Committed changes to planner branch]