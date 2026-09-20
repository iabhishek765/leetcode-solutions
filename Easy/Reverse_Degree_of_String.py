# LC#3498 - Reverse Degree of a String
# Difficulty: Easy
# Topics: String, Math
#
# Approach: For each char at 1-indexed position i,
#           reversed_alpha = 26 - (ord(c) - ord('a'))
#           ('a'=26, 'z'=1). Multiply by position, sum all.
# Time: O(n) | Space: O(1)
#
# ML Connection: Weighted positional scoring mirrors
# TF-IDF weighting in NLP where term importance is
# multiplied by positional or frequency-based weights

class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for i, c in enumerate(s):
            rev_alpha = 26 - (ord(c) - ord('a'))
            result += rev_alpha * (i + 1)
        return result
