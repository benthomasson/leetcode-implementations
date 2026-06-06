# Plan (Iteration 1)

Task: Solve the LeetCode problem "divide-array-into-equal-pairs":

You are given an integer array `nums` consisting of `2 * n` integers.

You need to divide `nums` into `n` pairs such that:

*   Each element belongs to **exactly one** pair.
*   The elements present in a pair are **equal**.

Return `true` _if nums can be divided into_ `n` _pairs, otherwise return_ `false`.

**Example 1:**

**Input:** nums = \[3,2,3,2,2,2\]
**Output:** true
**Explanation:** 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

**Example 2:**

**Input:** nums = \[1,2,3,4\]
**Output:** false
**Explanation:** 
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.

**Constraints:**

*   `nums.length == 2 * n`
*   `1 <= n <= 500`
*   `1 <= nums[i] <= 500`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: max_bombs_detonated

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. This is a straightforward counting problem — count each number's frequency with `Counter`, return `True` iff all counts are even.

[Committed changes to planner branch]