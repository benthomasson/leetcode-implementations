# Plan (Iteration 1)

Task: Solve the LeetCode problem "image-smoother":

An **image smoother** is a filter of the size `3 x 3` that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

Given an `m x n` integer matrix `img` representing the grayscale of an image, return _the image after applying the smoother on each cell of it_.

**Example 1:**

**Input:** img = \[\[1,1,1\],\[1,0,1\],\[1,1,1\]\]
**Output:** \[\[0,0,0\],\[0,0,0\],\[0,0,0\]\]
**Explanation:**
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

**Example 2:**

**Input:** img = \[\[100,200,100\],\[200,50,200\],\[100,200,100\]\]
**Output:** \[\[137,141,137\],\[141,138,141\],\[137,141,137\]\]
**Explanation:**
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138

**Constraints:**

*   `m == img.length`
*   `n == img[i].length`
*   `1 <= m, n <= 200`
*   `0 <= img[i][j] <= 255`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: imageSmoother

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. 

**Summary:** Straightforward O(m·n) solution — for each cell, sum its valid 3x3 neighbors using clamped indices, floor-divide by the count, write to a new output matrix. Tests should cover both examples plus edge cases (1x1, single row/column, boundary values).

[Committed changes to planner branch]