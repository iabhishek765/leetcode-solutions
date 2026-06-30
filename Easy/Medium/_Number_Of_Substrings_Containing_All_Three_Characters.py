"""
LC#1358 - Number of Substrings Containing All Three Characters [Medium]
Topic: Sliding Window
ML Connection: Sliding window counting is the same technique used in 
NLP for computing n-gram statistics or rolling context windows over 
a sequence of tokens.
"""

class Solution(object):
    def numberOfSubstrings(self, s):
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                count[s[left]] -= 1
                left += 1

            result += left

        return result
