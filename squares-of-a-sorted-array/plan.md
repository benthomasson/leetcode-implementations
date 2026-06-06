# Plan (Iteration 1)

Task: Solve the LeetCode problem "squares-of-a-sorted-array":

Given an integer array `nums` sorted in **non-decreasing** order, return _an array of **the squares of each number** sorted in non-decreasing order_.

**Example 1:**

**Input:** nums = \[-4,-1,0,3,10\]
**Output:** \[0,1,9,16,100\]
**Explanation:** After squaring, the array becomes \[16,1,0,9,100\].
After sorting, it becomes \[0,1,9,16,100\].

**Example 2:**

**Input:** nums = \[-7,-3,2,3,11\]
**Output:** \[4,9,9,49,121\]

**Constraints:**

*   `1 <= nums.length <= 104`
*   `-104 <= nums[i] <= 104`
*   `nums` is sorted in **non-decreasing** order.

**Follow up:** Squaring each element and sorting the new array is very trivial, could you find an `O(n)` solution using a different approach?

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: distinctSubseqII

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Summary:

**Algorithm:** Two-pointer approach, O(n) time. Pointers at both ends of the sorted array, compare absolute values, fill result array from the back.

**Key note:** The required function name `distinctSubseqII` doesn't match the problem — following the requirement as stated.

**Confidence:** HIGH — canonical problem with a well-known optimal solution.

[Committed changes to planner branch]