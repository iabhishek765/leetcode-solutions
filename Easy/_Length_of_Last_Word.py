# LC#58 - Length of Last Word
# Difficulty: Easy
# Topics: String
#
# Approach: Split string by whitespace (handles trailing spaces
#           automatically), return length of last element
# Time: O(n) | Space: O(n)
#
# ML Connection: Tokenization and word boundary detection are
# core NLP preprocessing steps — this is the simplest form
# of word segmentation used before embedding lookup

class Solution:
    def lengthOfLastWord(self, s):
        x = s.split()
        return len(x[-1])
