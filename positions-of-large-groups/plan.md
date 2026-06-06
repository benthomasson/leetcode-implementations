# Plan (Iteration 1)

Task: Solve the LeetCode problem "positions-of-large-groups":

In a string `s` of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like `s = "abbxxxxzyy "` has the groups `"a "`, `"bb "`, `"xxxx "`, `"z "`, and `"yy "`.

A group is identified by an interval `[start, end]`, where `start` and `end` denote the start and end indices (inclusive) of the group. In the above example, `"xxxx "` has the interval `[3,6]`.

A group is considered **large** if it has 3 or more characters.

Return _the intervals of every **large** group sorted in **increasing order by start index**_.

**Example 1:**

**Input:** s =  "abbxxxxzzy "
**Output:** \[\[3,6\]\]
**Explanation:** `"xxxx " is the only` large group with start index 3 and end index 6.

**Example 2:**

**Input:** s =  "abc "
**Output:** \[\]
**Explanation:** We have groups  "a ",  "b ", and  "c ", none of which are large groups.

**Example 3:**

**Input:** s =  "abcdddeeeeaabbbcd "
**Output:** \[\[3,5\],\[6,9\],\[12,14\]\]
**Explanation:** The large groups are  "ddd ",  "eeee ", and  "bbb ".

**Constraints:**

*   `1 <= s.length <= 1000`
*   `s` contains lowercase English letters only.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: largestTriangleArea

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`.

**Summary:** Single-pass linear scan tracking group start indices — O(n) time, O(1) space. One notable issue: the task says to use function name `largestTriangleArea` which is a copy-paste error from a different problem. The plan recommends using `largeGroupPositions` to match LeetCode's expected signature.

[Committed changes to planner branch]