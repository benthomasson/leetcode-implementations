# Review: Count Pairs of Similar Strings

## Solution
- **Approach**: Use frozenset to canonicalize each word's character set, count frequency of each set with Counter, then sum pairs using combination formula n*(n-1)/2 for each group.
- **Time Complexity**: O(n * m) where n is number of words, m is average word length
- **Space Complexity**: O(n * k) where k is average number of unique characters
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes all examples, edge cases (single word, all identical sets, all unique, single-char words)
- **Edge Cases**: Yes - single word, all same character set, all different character sets, repeated characters within words

## Plan
- **Quality**: Good - concise explanation of the key insight (frozenset canonicalization + combination formula), appropriate for minimal effort level

## Overall
Clean, optimal solution with excellent test coverage. The frozenset approach correctly identifies similar words regardless of character frequency or order, and the combination formula efficiently counts pairs without nested loops.
