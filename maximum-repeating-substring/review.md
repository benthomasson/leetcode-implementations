# Review: Maximum Repeating Substring

## Solution
- **Approach**: Iteratively checks if word concatenated k+1 times is a substring of sequence, incrementing k until no longer found.
- **Time Complexity**: O(n × m × k) where n=len(sequence), m=len(word), k=max repeats (string search is O(n×m) per iteration)
- **Space Complexity**: O(m × k) for constructing repeated word string
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes all LeetCode examples plus 7 additional edge cases
- **Edge Cases**: Yes - word not found, word longer than sequence, exact match, full repetition (single/multi-char), single char inputs, repetition in middle

## Plan
- **Quality**: Adequate - brief description matches MINIMAL effort level, correctly identifies algorithm

## Overall
Solution is correct and efficient for the constraints (max length 100). Tests are comprehensive. Note: Function name `longestAwesomeSubstring` doesn't match problem name (should be `maxRepeating`) - likely copy-paste error from different problem.
