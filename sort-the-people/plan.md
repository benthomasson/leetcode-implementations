# Plan (Iteration 1)

Task: Solve the LeetCode problem "sort-the-people":

You are given an array of strings `names`, and an array `heights` that consists of **distinct** positive integers. Both arrays are of length `n`.

For each index `i`, `names[i]` and `heights[i]` denote the name and height of the `ith` person.

Return `names` _sorted in **descending** order by the people's heights_.

**Example 1:**

**Input:** names = \[ "Mary ", "John ", "Emma "\], heights = \[180,165,170\]
**Output:** \[ "Mary ", "Emma ", "John "\]
**Explanation:** Mary is the tallest, followed by Emma and John.

**Example 2:**

**Input:** names = \[ "Alice ", "Bob ", "Bob "\], heights = \[155,185,150\]
**Output:** \[ "Bob ", "Alice ", "Bob "\]
**Explanation:** The first Bob is the tallest, followed by Alice and the second Bob.

**Constraints:**

*   `n == names.length == heights.length`
*   `1 <= n <= 103`
*   `1 <= names[i].length <= 20`
*   `1 <= heights[i] <= 105`
*   `names[i]` consists of lower and upper case English letters.
*   All the values of `heights` are distinct.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: sort_names_by_height

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. This is a straightforward zip-sort problem — the implementer should have no issues.

[Committed changes to planner branch]