# Plan (Iteration 1)

Task: Solve the LeetCode problem "number-of-strings-that-appear-as-substrings-in-word":

Given an array of strings `patterns` and a string `word`, return _the **number** of strings in_ `patterns` _that exist as a **substring** in_ `word`.

A **substring** is a contiguous sequence of characters within a string.

**Example 1:**

**Input:** patterns = \[ "a ", "abc ", "bc ", "d "\], word =  "abc "
**Output:** 3
**Explanation:**
-  "a " appears as a substring in  "abc ".
-  "abc " appears as a substring in  "abc ".
-  "bc " appears as a substring in  "abc ".
-  "d " does not appear as a substring in  "abc ".
3 of the strings in patterns appear as a substring in word.

**Example 2:**

**Input:** patterns = \[ "a ", "b ", "c "\], word =  "aaaaabbbbb "
**Output:** 2
**Explanation:**
-  "a " appears as a substring in  "aaaaabbbbb ".
-  "b " appears as a substring in  "aaaaabbbbb ".
-  "c " does not appear as a substring in  "aaaaabbbbb ".
2 of the strings in patterns appear as a substring in word.

**Example 3:**

**Input:** patterns = \[ "a ", "a ", "a "\], word =  "ab "
**Output:** 3
**Explanation:** Each of the patterns appears as a substring in word  "ab ".

**Constraints:**

*   `1 <= patterns.length <= 100`
*   `1 <= patterns[i].length <= 100`
*   `1 <= word.length <= 100`
*   `patterns[i]` and `word` consist of lowercase English letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: longest_beautiful_substring

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Key points:

- **Algorithm:** `sum(1 for p in patterns if p in word)` — simple iteration with Python's `in` operator.
- **Function name:** The task metadata says `longest_beautiful_substring` which is a copy-paste error. Recommending `numOfStrings` to match the actual LeetCode problem.
- **Tests:** Cover all 3 examples plus edge cases (no match, all match, duplicates, pattern == word, pattern longer than word).
- **Confidence:** HIGH — trivial problem, constraints are tiny.

[Committed changes to planner branch]