# Plan (Iteration 1)

Task: Solve the LeetCode problem "number-of-unequal-triplets-in-array":

You are given a **0-indexed** array of positive integers `nums`. Find the number of triplets `(i, j, k)` that meet the following conditions:

*   `0 <= i < j < k < nums.length`
*   `nums[i]`, `nums[j]`, and `nums[k]` are **pairwise distinct**.
    *   In other words, `nums[i] != nums[j]`, `nums[i] != nums[k]`, and `nums[j] != nums[k]`.

Return _the number of triplets that meet the conditions._

**Example 1:**

**Input:** nums = \[4,4,2,4,3\]
**Output:** 3
**Explanation:** The following triplets meet the conditions:
- (0, 2, 4) because 4 != 2 != 3
- (1, 2, 4) because 4 != 2 != 3
- (2, 3, 4) because 2 != 4 != 3
Since there are 3 triplets, we return 3.
Note that (2, 0, 4) is not a valid triplet because 2 > 0.

**Example 2:**

**Input:** nums = \[1,1,1,1,1\]
**Output:** 0
**Explanation:** No triplets meet the conditions so we return 0.

**Constraints:**

*   `3 <= nums.length <= 100`
*   `1 <= nums[i] <= 1000`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: countTriplets

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. 

**Summary:** Use `Counter` + prefix sum to count triplets in O(n) time. For each value group with count `c`, multiply `left * c * right` where `left`/`right` are counts of elements in other groups before/after. Two files: `solution.py` and `test_solution.py` with comprehensive edge case coverage.

[Committed changes to planner branch]