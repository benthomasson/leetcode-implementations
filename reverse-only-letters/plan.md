# Plan (Iteration 1)

Task: Solve the LeetCode problem "reverse-only-letters":

Given a string `s`, reverse the string according to the following rules:

*   All the characters that are not English letters remain in the same position.
*   All the English letters (lowercase or uppercase) should be reversed.

Return `s` _after reversing it_.

**Example 1:**

**Input:** s = "ab-cd"
**Output:** "dc-ba"

**Example 2:**

**Input:** s = "a-bC-dEf-ghIj"
**Output:** "j-Ih-gfE-dCba"

**Example 3:**

**Input:** s = "Test1ng-Leet=code-Q!"
**Output:** "Qedo1ct-eeLg=ntse-T!"

**Constraints:**

*   `1 <= s.length <= 100`
*   `s` consists of characters with ASCII values in the range `[33, 122]`.
*   `s` does not contain `'\ "'` or `'\\'`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: num_rescue_boats

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. 

**Summary:** Two-pointer swap, skip non-letters with `isalpha()`, O(n) time/space. One flag — the required function name `num_rescue_boats` doesn't match this problem but I'm preserving it per spec.

[Committed changes to planner branch]