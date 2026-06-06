# Plan (Iteration 1)

Task: Solve the LeetCode problem "find-first-palindromic-string-in-the-array":

Given an array of strings `words`, return _the first **palindromic** string in the array_. If there is no such string, return _an **empty string**_ `" "`.

A string is **palindromic** if it reads the same forward and backward.

**Example 1:**

**Input:** words = \[ "abc ", "car ", "ada ", "racecar ", "cool "\]
**Output:**  "ada "
**Explanation:** The first string that is palindromic is  "ada ".
Note that  "racecar " is also palindromic, but it is not the first.

**Example 2:**

**Input:** words = \[ "notapalindrome ", "racecar "\]
**Output:**  "racecar "
**Explanation:** The first and only string that is palindromic is  "racecar ".

**Example 3:**

**Input:** words = \[ "def ", "ghi "\]
**Output:**  " "
**Explanation:** There are no palindromic strings, so the empty string is returned.

**Constraints:**

*   `1 <= words.length <= 100`
*   `1 <= words[i].length <= 100`
*   `words[i]` consists only of lowercase English letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: minimizeTheDifference

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. 

**Summary:** Linear scan with `s == s[::-1]` palindrome check. O(n·m) time, O(m) space. Straightforward problem — the implementer just needs to wire up the function, docstring, and tests.

[Committed changes to planner branch]