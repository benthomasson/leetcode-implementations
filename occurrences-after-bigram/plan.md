# Plan (Iteration 1)

Task: Solve the LeetCode problem "occurrences-after-bigram":

Given two strings `first` and `second`, consider occurrences in some text of the form `"first second third "`, where `second` comes immediately after `first`, and `third` comes immediately after `second`.

Return _an array of all the words_ `third` _for each occurrence of_ `"first second third "`.

**Example 1:**

**Input:** text = "alice is a good girl she is a good student", first = "a", second = "good"
**Output:** \["girl","student"\]

**Example 2:**

**Input:** text = "we will we will rock you", first = "we", second = "will"
**Output:** \["we","rock"\]

**Constraints:**

*   `1 <= text.length <= 1000`
*   `text` consists of lowercase English letters and spaces.
*   All the words in `text` a separated by **a single space**.
*   `1 <= first.length, second.length <= 10`
*   `first` and `second` consist of lowercase English letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: remove_outer_parentheses

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Key callout: the task specifies `remove_outer_parentheses` as the function name, which is a copy-paste error — the correct LeetCode method name is `findOcurrences`.

[Committed changes to planner branch]