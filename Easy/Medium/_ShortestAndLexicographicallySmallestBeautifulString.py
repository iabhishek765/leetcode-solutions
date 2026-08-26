"""
LC#2904 - Shortest and Lexicographically Smallest Beautiful String [Medium]
Topic: Sliding Window
ML Connection: Finding optimal substrings under constraints mirrors 
attention window selection in transformers — finding the most 
relevant fixed-size context window.
"""

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        left = 0
        ones = 0
        result = ""

        for right in range(n):
            if s[right] == '1':
                ones += 1

            while ones == k:
                window = s[left:right+1]
                if not result or len(window) < len(result) or \
                   (len(window) == len(result) and window < result):
                    result = window
                if s[left] == '1':
                    ones -= 1
                left += 1

        return result
