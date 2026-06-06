# Plan (Iteration 1)

Task: Solve the LeetCode problem "valid-word-square":

Given an array of strings `words`, return `true` _if it forms a valid **word square**_.

A sequence of strings forms a valid **word square** if the `kth` row and column read the same string, where `0 <= k < max(numRows, numColumns)`.

**Example 1:**

**Input:** words = \[ "abcd ", "bnrt ", "crmy ", "dtye "\]
**Output:** true
**Explanation:**
The 1st row and 1st column both read  "abcd ".
The 2nd row and 2nd column both read  "bnrt ".
The 3rd row and 3rd column both read  "crmy ".
The 4th row and 4th column both read  "dtye ".
Therefore, it is a valid word square.

**Example 2:**

**Input:** words = \[ "abcd ", "bnrt ", "crm ", "dt "\]
**Output:** true
**Explanation:**
The 1st row and 1st column both read  "abcd ".
The 2nd row and 2nd column both read  "bnrt ".
The 3rd row and 3rd column both read  "crm ".
The 4th row and 4th column both read  "dt ".
Therefore, it is a valid word square.

**Example 3:**

**Input:** words = \[ "ball ", "area ", "read ", "lady "\]
**Output:** false
**Explanation:**
The 3rd row reads  "read " while the 3rd column reads  "lead ".
Therefore, it is NOT a valid word square.

**Constraints:**

*   `1 <= words.length <= 500`
*   `1 <= words[i].length <= 500`
*   `words[i]` consists of only lowercase English letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: valid_word_square

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The algorithm is a straightforward character-by-character transpose check with bounds handling for ragged arrays. O(n) time, O(1) space.

[Committed changes to planner branch]