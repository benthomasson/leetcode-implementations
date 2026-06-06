# Plan (Iteration 1)

Task: Solve the LeetCode problem "license-key-formatting":

You are given a license key represented as a string `s` that consists of only alphanumeric characters and dashes. The string is separated into `n + 1` groups by `n` dashes. You are also given an integer `k`.

We want to reformat the string `s` such that each group contains exactly `k` characters, except for the first group, which could be shorter than `k` but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return _the reformatted license key_.

**Example 1:**

**Input:** s =  "5F3Z-2e-9-w ", k = 4
**Output:**  "5F3Z-2E9W "
**Explanation:** The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.

**Example 2:**

**Input:** s =  "2-5g-3-J ", k = 2
**Output:**  "2-5G-3J "
**Explanation:** The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

**Constraints:**

*   `1 <= s.length <= 105`
*   `s` consists of English letters, digits, and dashes `'-'`.
*   `1 <= k <= 104`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: license_key_formatting

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is simple: strip dashes, uppercase, chunk from the right by `k`, join with dashes. O(n) time and space.

[Committed changes to planner branch]