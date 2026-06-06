# Plan (Iteration 1)

Task: Solve the LeetCode problem "most-frequent-even-element":

Given an integer array `nums`, return _the most frequent even element_.

If there is a tie, return the **smallest** one. If there is no such element, return `-1`.

**Example 1:**

**Input:** nums = \[0,1,2,2,4,4,1\]
**Output:** 2
**Explanation:**
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.

**Example 2:**

**Input:** nums = \[4,4,4,9,2,4\]
**Output:** 4
**Explanation:** 4 is the even element appears the most.

**Example 3:**

**Input:** nums = \[29,47,21,41,13,37,25,7\]
**Output:** -1
**Explanation:** There is no even element.

**Constraints:**

*   `1 <= nums.length <= 2000`
*   `0 <= nums[i] <= 105`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: most_frequent_even

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. Straightforward problem — count even element frequencies with a Counter, return the smallest key with max count, or -1 if none exist.

[Committed changes to planner branch]