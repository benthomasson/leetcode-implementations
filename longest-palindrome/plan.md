# Plan (Iteration 1)

Task: Solve the LeetCode problem "longest-palindrome":

Given a string `s` which consists of lowercase or uppercase letters, return _the length of the **longest palindrome**_ that can be built with those letters.

Letters are **case sensitive**, for example, `"Aa "` is not considered a palindrome here.

**Example 1:**

**Input:** s =  "abccccdd "
**Output:** 7
**Explanation:** One longest palindrome that can be built is  "dccaccd ", whose length is 7.

**Example 2:**

**Input:** s =  "a "
**Output:** 1
**Explanation:** The longest palindrome that can be built is  "a ", whose length is 1.

**Constraints:**

*   `1 <= s.length <= 2000`
*   `s` consists of lowercase **and/or** uppercase English letters only.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: longestPalindrome

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is simple greedy counting — no ambiguity here.

[Committed changes to planner branch]