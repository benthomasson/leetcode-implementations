# Plan (Iteration 1)

Task: Solve the LeetCode problem "check-if-array-is-sorted-and-rotated":

Given an array `nums`, return `true` _if the array was originally sorted in non-decreasing order, then rotated **some** number of positions (including zero)_. Otherwise, return `false`.

There may be **duplicates** in the original array.

**Note:** An array `A` rotated by `x` positions results in an array `B` of the same length such that `A[i] == B[(i+x) % A.length]`, where `%` is the modulo operation.

**Example 1:**

**Input:** nums = \[3,4,5,1,2\]
**Output:** true
**Explanation:** \[1,2,3,4,5\] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: \[3,4,5,1,2\].

**Example 2:**

**Input:** nums = \[2,1,3,4\]
**Output:** false
**Explanation:** There is no sorted array once rotated that can make nums.

**Example 3:**

**Input:** nums = \[1,2,3\]
**Output:** true
**Explanation:** \[1,2,3\] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

**Constraints:**

*   `1 <= nums.length <= 100`
*   `1 <= nums[i] <= 100`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: check_arithmetic_subarrays

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The approach is straightforward: count circular breaks in O(n) time — at most 1 break means sorted-and-rotated.

[Committed changes to planner branch]