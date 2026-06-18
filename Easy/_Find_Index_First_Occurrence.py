# LC#28 - Find the Index of the First Occurrence in a String
# Difficulty: Easy
# Topics: String, String Matching
#
# Approach: Brute force - slide window of needle's length
#           across haystack, compare substrings
# Time: O(n*m) | Space: O(1)
#
# ML Connection: Substring search is the foundation of pattern
# matching used in NLP tasks like keyword/entity spotting in
# text before more advanced tokenization or embedding lookup

class Solution(object):
    def strStr(self, haystack, needle):
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1
