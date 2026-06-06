# Plan (Iteration 1)

Task: Solve the LeetCode problem "sign-of-the-product-of-an-array":

There is a function `signFunc(x)` that returns:

*   `1` if `x` is positive.
*   `-1` if `x` is negative.
*   `0` if `x` is equal to `0`.

You are given an integer array `nums`. Let `product` be the product of all values in the array `nums`.

Return `signFunc(product)`.

**Example 1:**

**Input:** nums = \[-1,-2,-3,-4,3,2,1\]
**Output:** 1
**Explanation:** The product of all values in the array is 144, and signFunc(144) = 1

**Example 2:**

**Input:** nums = \[1,5,0,2,-3\]
**Output:** 0
**Explanation:** The product of all values in the array is 0, and signFunc(0) = 0

**Example 3:**

**Input:** nums = \[-1,1,-1,1,-1\]
**Output:** -1
**Explanation:** The product of all values in the array is -1, and signFunc(-1) = -1

**Constraints:**

*   `1 <= nums.length <= 1000`
*   `-100 <= nums[i] <= 100`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: signFunc

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is simple: count negatives, check for zeros, skip the actual product computation entirely.

[Committed changes to planner branch]