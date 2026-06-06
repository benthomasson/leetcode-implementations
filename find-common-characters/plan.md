# Plan (Iteration 1)

Task: Solve the LeetCode problem "find-common-characters":

Given a string array `words`, return _an array of all characters that show up in all strings within the_ `words` _(including duplicates)_. You may return the answer in **any order**.

**Example 1:**

**Input:** words = \["bella","label","roller"\]
**Output:** \["e","l","l"\]

**Example 2:**

**Input:** words = \["cool","lock","cook"\]
**Output:** \["c","o"\]

**Constraints:**

*   `1 <= words.length <= 100`
*   `1 <= words[i].length <= 100`
*   `words[i]` consists of lowercase English letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. 

**Summary:** Use `Counter` intersection across all words — initialize from the first word, `&=` with each subsequent word's counter, then expand to a list. O(n·m) time, O(1) space. Tests should cover the two provided examples plus edge cases (single word, no overlap, uniform characters, etc.).

[Committed changes to planner branch]