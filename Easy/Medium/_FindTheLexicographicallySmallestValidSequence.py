"""
LC#3302 - Find the Lexicographically Smallest Valid Sequence [Medium]
Topic: Greedy + Suffix Array
ML Connection: Greedy subsequence matching with one allowed error mirrors 
approximate string matching used in fuzzy search and edit-distance 
based retrieval in NLP systems.
"""

class Solution:
    def validSequence(self, word1: str, word2: str) -> list:
        n, m = len(word1), len(word2)

        # suf[i] = chars of word2's suffix matchable in word1[i:]
        suf = [0] * (n + 1)
        ptr = m - 1
        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1]
            if ptr >= 0 and word1[i] == word2[ptr]:
                suf[i] += 1
                ptr -= 1

        result = []
        j = 0
        used_wildcard = False

        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                result.append(i)
                j += 1
            elif not used_wildcard and suf[i + 1] >= m - j - 1:
                # Use wildcard here: match word2[j] with word1[i] (1 change)
                # Then suf[i+1] covers word2[j+1:]
                result.append(i)
                j += 1
                used_wildcard = True

        return result if j == m else []
