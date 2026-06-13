"""
Problem: Weighted Word Mapping (LC #3838)
Difficulty: Easy
Link: https://leetcode.com/problems/weighted-word-mapping/

Approach:
- For each word, sum weights of its characters
- Take sum % 26 → map to letter using reverse alphabetical
- 0→'z', 1→'y' ... 25→'a' means chr(ord('z') - idx)
- Time: O(n * m) | Space: O(1)
  where n = words, m = avg word length

ML Connection:
- Character weight mapping is similar to TF-IDF
  where each term gets a weighted score in NLP
- Modular indexing used in hash embeddings for
  memory-efficient text representation in ML models
"""

class Solution(object):
    def mapWordWeights(self, words, weights):
        result = []
        for word in words:
            total = sum(weights[ord(c) - ord('a')] for c in word)
            idx = total % 26
            result.append(chr(ord('z') - idx))
        return ''.join(result)
