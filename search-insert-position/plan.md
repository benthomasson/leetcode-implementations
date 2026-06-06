# Plan (Iteration 1)

Task: Solve the LeetCode problem "search-insert-position":

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

**Input:** nums = \[1,3,5,6\], target = 5
**Output:** 2

**Example 2:**

**Input:** nums = \[1,3,5,6\], target = 2
**Output:** 1

**Example 3:**

**Input:** nums = \[1,3,5,6\], target = 7
**Output:** 4

**Constraints:**

*   `1 <= nums.length <= 104`
*   `-104 <= nums[i] <= 104`
*   `nums` contains **distinct** values sorted in **ascending** order.
*   `-104 <= target <= 104`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: searchInsert

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. This is a straightforward binary search problem — the left pointer naturally gives the insertion position when the target isn't found.

[Committed changes to planner branch]