# Plan (Iteration 1)

Task: Solve the LeetCode problem "greatest-english-letter-in-upper-and-lower-case":

Given a string of English letters `s`, return _the **greatest** English letter which occurs as **both** a lowercase and uppercase letter in_ `s`. The returned letter should be in **uppercase**. If no such letter exists, return _an empty string_.

An English letter `b` is **greater** than another letter `a` if `b` appears **after** `a` in the English alphabet.

**Example 1:**

**Input:** s =  "l**Ee**TcOd**E** "
**Output:**  "E "
**Explanation:**
The letter 'E' is the only letter to appear in both lower and upper case.

**Example 2:**

**Input:** s =  "a**rR**AzFif "
**Output:**  "R "
**Explanation:**
The letter 'R' is the greatest letter to appear in both lower and upper case.
Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.

**Example 3:**

**Input:** s =  "AbCdEfGhIjK "
**Output:**  " "
**Explanation:**
There is no letter that appears in both lower and upper case.

**Constraints:**

*   `1 <= s.length <= 1000`
*   `s` consists of lowercase and uppercase English letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: get_max_occurrences

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. 

**Summary:** Convert `s` to a set, iterate Z→A, return the first letter found in both cases. O(n) time, O(n) space. Confidence: **HIGH**.

[Committed changes to planner branch]