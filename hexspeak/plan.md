# Plan (Iteration 1)

Task: Solve the LeetCode problem "hexspeak":

A decimal number can be converted to its **Hexspeak representation** by first converting it to an uppercase hexadecimal string, then replacing all occurrences of the digit `'0'` with the letter `'O'`, and the digit `'1'` with the letter `'I'`. Such a representation is valid if and only if it consists only of the letters in the set `{'A', 'B', 'C', 'D', 'E', 'F', 'I', 'O'}`.

Given a string `num` representing a decimal integer `n`, _return the **Hexspeak representation** of_ `n` _if it is valid, otherwise return_ `"ERROR "`.

**Example 1:**

**Input:** num =  "257 "
**Output:**  "IOI "
**Explanation:** 257 is 101 in hexadecimal.

**Example 2:**

**Input:** num =  "3 "
**Output:**  "ERROR "

**Constraints:**

*   `1 <= num.length <= 12`
*   `num` does not contain leading zeros.
*   num represents an integer in the range `[1, 1012]`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: to_hexspeak

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. This is a straightforward string manipulation problem — convert to hex, substitute two characters, validate against a character set. No complex design decisions needed.

[Committed changes to planner branch]