# Plan (Iteration 1)

Task: Solve the LeetCode problem "maximum-average-subarray-i":

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose **length is equal to** `k` that has the maximum average value and return _this value_. Any answer with a calculation error less than `10-5` will be accepted.

**Example 1:**

**Input:** nums = \[1,12,-5,-6,50,3\], k = 4
**Output:** 12.75000
**Explanation:** Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

**Example 2:**

**Input:** nums = \[5\], k = 1
**Output:** 5.00000

**Constraints:**

*   `n == nums.length`
*   `1 <= k <= n <= 105`
*   `-104 <= nums[i] <= 104`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: findMaxAverage

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Sliding window is the clear optimal approach here — nothing else to deliberate.

[Committed changes to planner branch]