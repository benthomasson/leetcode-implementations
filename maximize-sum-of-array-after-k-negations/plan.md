# Plan (Iteration 1)

Task: Solve the LeetCode problem "maximize-sum-of-array-after-k-negations":

Given an integer array `nums` and an integer `k`, modify the array in the following way:

*   choose an index `i` and replace `nums[i]` with `-nums[i]`.

You should apply this process exactly `k` times. You may choose the same index `i` multiple times.

Return _the largest possible sum of the array after modifying it in this way_.

**Example 1:**

**Input:** nums = \[4,2,3\], k = 1
**Output:** 5
**Explanation:** Choose index 1 and nums becomes \[4,-2,3\].

**Example 2:**

**Input:** nums = \[3,-1,0,2\], k = 3
**Output:** 6
**Explanation:** Choose indices (1, 2, 2) and nums becomes \[3,1,0,2\].

**Example 3:**

**Input:** nums = \[2,-3,-1,5,-4\], k = 2
**Output:** 13
**Explanation:** Choose indices (1, 4) and nums becomes \[2,3,-1,5,4\].

**Constraints:**

*   `1 <= nums.length <= 104`
*   `-100 <= nums[i] <= 100`
*   `1 <= k <= 104`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: is_univalued

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`.

**Summary:** Greedy approach — sort, negate the most negative elements first, then if remaining `k` is odd, negate the smallest absolute value element. O(n log n) time. One note: the task specifies function name `is_univalued` which doesn't match this problem — the implementer should use `largest_sum_after_k_negations` (or the standard LeetCode name) and alias if needed.

[Committed changes to planner branch]