# Plan (Iteration 1)

Task: Solve the LeetCode problem "check-if-a-number-is-majority-element-in-a-sorted-array":

Given an integer array `nums` sorted in non-decreasing order and an integer `target`, return `true` _if_ `target` _is a **majority** element, or_ `false` _otherwise_.

A **majority** element in an array `nums` is an element that appears more than `nums.length / 2` times in the array.

**Example 1:**

**Input:** nums = \[2,4,5,5,5,5,5,6,6\], target = 5
**Output:** true
**Explanation:** The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 > 9/2 is true.

**Example 2:**

**Input:** nums = \[10,100,101,101\], target = 101
**Output:** false
**Explanation:** The value 101 appears 2 times and the length of the array is 4.
Thus, 101 is not a majority element because 2 > 4/2 is false.

**Constraints:**

*   `1 <= nums.length <= 1000`
*   `1 <= nums[i], target <= 109`
*   `nums` is sorted in non-decreasing order.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: is_majority_element

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is simple: one binary search to find the leftmost occurrence, then a single index check at `first + n//2`. O(log n) time, O(1) space.

[Committed changes to planner branch]