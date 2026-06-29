"""
LC#1967 - Number of Strings That Appear as Substrings in Word [Easy]
Topic: String Matching
ML Connection: Substring matching is the foundation of basic text 
search and is used in preprocessing steps like keyword extraction 
before feeding text into NLP models.
"""

class Solution(object):
    def numOfStrings(self, patterns, word):
        count = 0
        for p in patterns:
            if p in word:
                count += 1
        return count
