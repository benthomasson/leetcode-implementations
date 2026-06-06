# Plan (Iteration 1)

Task: Solve the LeetCode problem "majority-element":

Given an array `nums` of size `n`, return _the majority element_.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example 1:**

**Input:** nums = \[3,2,3\]
**Output:** 3

**Example 2:**

**Input:** nums = \[2,2,1,1,1,2,2\]
**Output:** 2

**Constraints:**

*   `n == nums.length`
*   `1 <= n <= 5 * 104`
*   `-109 <= nums[i] <= 109`

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: majority_element

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Boyer-Moore Voting Algorithm, O(n) time, O(1) space. Straightforward implementation with standard edge-case tests.

[Committed changes to planner branch]