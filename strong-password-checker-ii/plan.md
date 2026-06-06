# Plan (Iteration 1)

Task: Solve the LeetCode problem "strong-password-checker-ii":

A password is said to be **strong** if it satisfies all the following criteria:

*   It has at least `8` characters.
*   It contains at least **one lowercase** letter.
*   It contains at least **one uppercase** letter.
*   It contains at least **one digit**.
*   It contains at least **one special character**. The special characters are the characters in the following string: `"!@#$%^&*()-+ "`.
*   It does **not** contain `2` of the same character in adjacent positions (i.e., `"aab "` violates this condition, but `"aba "` does not).

Given a string `password`, return `true` _if it is a **strong** password_. Otherwise, return `false`.

**Example 1:**

**Input:** password =  "IloveLe3tcode! "
**Output:** true
**Explanation:** The password meets all the requirements. Therefore, we return true.

**Example 2:**

**Input:** password =  "Me+You--IsMyDream "
**Output:** false
**Explanation:** The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.

**Example 3:**

**Input:** password =  "1aB! "
**Output:** false
**Explanation:** The password does not meet the length requirement. Therefore, we return false.

**Constraints:**

*   `1 <= password.length <= 100`
*   `password` consists of letters, digits, and special characters: `"!@#$%^&*()-+ "`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: merge_nodes_between_zeros

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

## SELF-REVIEW

1. **What went well:** Straightforward problem — the algorithm is obvious (single-pass with flags), so planning was quick and appropriate.
2. **Missing info:** None needed — the problem is fully specified.
3. **Next time:** Nothing to change for simple validation problems like this.
4. **Confidence:** **HIGH** — This is a simple linear scan with well-defined criteria. No ambiguity in requirements or approach.

[Committed changes to planner branch]