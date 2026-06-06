# Plan (Iteration 1)

Task: Solve the LeetCode problem "di-string-match":

A permutation `perm` of `n + 1` integers of all the integers in the range `[0, n]` can be represented as a string `s` of length `n` where:

*   `s[i] == 'I'` if `perm[i] < perm[i + 1]`, and
*   `s[i] == 'D'` if `perm[i] > perm[i + 1]`.

Given a string `s`, reconstruct the permutation `perm` and return it. If there are multiple valid permutations perm, return **any of them**.

**Example 1:**

**Input:** s = "IDID"
**Output:** \[0,4,1,3,2\]

**Example 2:**

**Input:** s = "III"
**Output:** \[0,1,2,3\]

**Example 3:**

**Input:** s = "DDI"
**Output:** \[3,2,0,1\]

**Constraints:**

*   `1 <= s.length <= 105`
*   `s[i]` is either `'I'` or `'D'`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: isPalindrome

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The two-pointer greedy approach is optimal and straightforward for this problem.

[Committed changes to planner branch]