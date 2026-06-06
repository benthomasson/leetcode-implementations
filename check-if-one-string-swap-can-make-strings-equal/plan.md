# Plan (Iteration 1)

Task: Solve the LeetCode problem "check-if-one-string-swap-can-make-strings-equal":

You are given two strings `s1` and `s2` of equal length. A **string swap** is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return `true` _if it is possible to make both strings equal by performing **at most one string swap** on **exactly one** of the strings._ Otherwise, return `false`.

**Example 1:**

**Input:** s1 =  "bank ", s2 =  "kanb "
**Output:** true
**Explanation:** For example, swap the first character with the last character of s2 to make  "bank ".

**Example 2:**

**Input:** s1 =  "attack ", s2 =  "defend "
**Output:** false
**Explanation:** It is impossible to make them equal with one string swap.

**Example 3:**

**Input:** s1 =  "kelb ", s2 =  "kelb "
**Output:** true
**Explanation:** The two strings are already equal, so no string swap operation is required.

**Constraints:**

*   `1 <= s1.length, s2.length <= 100`
*   `s1.length == s2.length`
*   `s1` and `s2` consist of only lowercase English letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: are_almost_equal

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The algorithm is straightforward: count mismatches, check if exactly 0 or exactly 2 with a valid cross-swap. O(n) time, O(1) space.

[Committed changes to planner branch]