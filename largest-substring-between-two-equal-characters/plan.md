# Plan (Iteration 1)

Task: Solve the LeetCode problem "largest-substring-between-two-equal-characters":

Given a string `s`, return _the length of the longest substring between two equal characters, excluding the two characters._ If there is no such substring return `-1`.

A **substring** is a contiguous sequence of characters within a string.

**Example 1:**

**Input:** s =  "aa "
**Output:** 0
**Explanation:** The optimal substring here is an empty substring between the two `'a's`.

**Example 2:**

**Input:** s =  "abca "
**Output:** 2
**Explanation:** The optimal substring here is  "bc ".

**Example 3:**

**Input:** s =  "cbzxy "
**Output:** -1
**Explanation:** There are no characters that appear twice in s.

**Constraints:**

*   `1 <= s.length <= 300`
*   `s` contains only lowercase English letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: maxLengthBetweenEqualCharacters

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The approach is straightforward: single-pass with a first-occurrence hash map, O(n) time, O(1) space.

[Committed changes to planner branch]