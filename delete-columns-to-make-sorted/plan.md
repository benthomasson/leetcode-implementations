# Plan (Iteration 1)

Task: Solve the LeetCode problem "delete-columns-to-make-sorted":

You are given an array of `n` strings `strs`, all of the same length.

The strings can be arranged such that there is one on each line, making a grid.

*   For example, `strs = [ "abc ", "bce ", "cae "]` can be arranged as follows:

abc
bce
cae

You want to **delete** the columns that are **not sorted lexicographically**. In the above example (**0-indexed**), columns 0 (`'a'`, `'b'`, `'c'`) and 2 (`'c'`, `'e'`, `'e'`) are sorted, while column 1 (`'b'`, `'c'`, `'a'`) is not, so you would delete column 1.

Return _the number of columns that you will delete_.

**Example 1:**

**Input:** strs = \[ "cba ", "daf ", "ghi "\]
**Output:** 1
**Explanation:** The grid looks as follows:
  cba
  daf
  ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.

**Example 2:**

**Input:** strs = \[ "a ", "b "\]
**Output:** 0
**Explanation:** The grid looks as follows:
  a
  b
Column 0 is the only column and is sorted, so you will not delete any columns.

**Example 3:**

**Input:** strs = \[ "zyx ", "wvu ", "tsr "\]
**Output:** 3
**Explanation:** The grid looks as follows:
  zyx
  wvu
  tsr
All 3 columns are not sorted, so you will delete all 3.

**Constraints:**

*   `n == strs.length`
*   `1 <= n <= 100`
*   `1 <= strs[i].length <= 1000`
*   `strs[i]` consists of lowercase English letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: minDifference

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Key points:

- **Algorithm:** Simple column-wise iteration, O(n*m) time, O(1) space. For each column, check if consecutive rows are sorted; count those that aren't.
- **Flag:** The task says function name should be `minDifference`, but LeetCode's actual name for this problem is `minDeletionSize`. Implementer should decide which to use.
- **Confidence:** HIGH — this is a straightforward problem.

[Committed changes to planner branch]