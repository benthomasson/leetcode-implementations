# Plan (Iteration 1)

Task: Solve the LeetCode problem "keyboard-row":

Given an array of strings `words`, return _the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below_.

In the **American keyboard**:

*   the first row consists of the characters `"qwertyuiop "`,
*   the second row consists of the characters `"asdfghjkl "`, and
*   the third row consists of the characters `"zxcvbnm "`.

**Example 1:**

**Input:** words = \[ "Hello ", "Alaska ", "Dad ", "Peace "\]
**Output:** \[ "Alaska ", "Dad "\]

**Example 2:**

**Input:** words = \[ "omk "\]
**Output:** \[\]

**Example 3:**

**Input:** words = \[ "adsdf ", "sfd "\]
**Output:** \[ "adsdf ", "sfd "\]

**Constraints:**

*   `1 <= words.length <= 20`
*   `1 <= words[i].length <= 100`
*   `words[i]` consists of English letters (both lowercase and uppercase).

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: find_words

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `/workspaces/keyboard-row/planner/PLAN.md`. Simple dict-lookup approach with set-based row checking — O(n·m) time, O(1) space.

[Committed changes to planner branch]