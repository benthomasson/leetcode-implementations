# Plan (Iteration 1)

Task: Solve the LeetCode problem "count-good-triplets":

Given an array of integers `arr`, and three integers `a`, `b` and `c`. You need to find the number of good triplets.

A triplet `(arr[i], arr[j], arr[k])` is **good** if the following conditions are true:

*   `0 <= i < j < k < arr.length`
*   `|arr[i] - arr[j]| <= a`
*   `|arr[j] - arr[k]| <= b`
*   `|arr[i] - arr[k]| <= c`

Where `|x|` denotes the absolute value of `x`.

Return _the number of good triplets_.

**Example 1:**

**Input:** arr = \[3,0,1,1,9,7\], a = 7, b = 2, c = 3
**Output:** 4
**Explanation:** There are 4 good triplets: \[(3,0,1), (3,0,1), (3,1,1), (0,1,1)\].

**Example 2:**

**Input:** arr = \[1,1,2,2,3\], a = 0, b = 0, c = 1
**Output:** 0
**Explanation:** No triplet satisfies all conditions.

**Constraints:**

*   `3 <= arr.length <= 100`
*   `0 <= arr[i] <= 1000`
*   `0 <= a, b, c <= 1000`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: minNumberOfFrogs

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Key callout: the task references `minNumberOfFrogs` as the function name — that's a copy-paste error from a different problem. The correct LeetCode signature is `countGoodTriplets`. Brute-force O(n³) with early pruning on the (i,j) pair is the right approach given n ≤ 100.

[Committed changes to planner branch]