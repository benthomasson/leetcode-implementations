# Plan (Iteration 1)

Task: Solve the LeetCode problem "two-out-of-three":

Given three integer arrays `nums1`, `nums2`, and `nums3`, return _a **distinct** array containing all the values that are present in **at least two** out of the three arrays. You may return the values in **any** order_.

**Example 1:**

**Input:** nums1 = \[1,1,3,2\], nums2 = \[2,3\], nums3 = \[3\]
**Output:** \[3,2\]
**Explanation:** The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2.

**Example 2:**

**Input:** nums1 = \[3,1\], nums2 = \[2,3\], nums3 = \[1,2\]
**Output:** \[2,3,1\]
**Explanation:** The values that are present in at least two arrays are:
- 2, in nums2 and nums3.
- 3, in nums1 and nums2.
- 1, in nums1 and nums3.

**Example 3:**

**Input:** nums1 = \[1,2,2\], nums2 = \[4,3,3\], nums3 = \[5\]
**Output:** \[\]
**Explanation:** No value is present in at least two arrays.

**Constraints:**

*   `1 <= nums1.length, nums2.length, nums3.length <= 100`
*   `1 <= nums1[i], nums2[j], nums3[k] <= 100`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: largest_odd

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Key points:

- **Algorithm:** `(set1 & set2) | (set1 & set3) | (set2 & set3)` — union of pairwise set intersections. O(n) time/space.
- **Note:** The required function name `largest_odd` doesn't match the problem, but we follow the spec as given.
- **Confidence: HIGH** — textbook set problem with a clean one-liner solution.

[Committed changes to planner branch]