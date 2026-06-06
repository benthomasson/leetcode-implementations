# Review: Uncommon Words from Two Sentences

## Solution
- **Approach**: Counts all words from both sentences combined using Counter, returns words appearing exactly once
- **Time Complexity**: O(n + m) where n, m are sentence lengths
- **Space Complexity**: O(n + m) for word storage
- **Correctness**: Has Issues - **Critical bug: function named `k_similarity` instead of appropriate name for uncommon-words problem** (k_similarity is a different LeetCode problem about string transformations)

## Tests
- **Coverage**: Good - covers examples, edge cases (duplicates, no overlap, identical sentences, words appearing multiple times)
- **Edge Cases**: Yes - single words, all unique, duplicates within sentences, word appearing 3+ times

## Plan
- **Quality**: Adequate - correctly identifies O(n) Counter approach, but references wrong function name `k_similarity`

## Overall
Algorithm is correct for finding uncommon words, but the function is named after a completely different LeetCode problem (k-similarity is about anagram transformations). All files consistently use this wrong name. The solution needs to be renamed to match the actual problem.
