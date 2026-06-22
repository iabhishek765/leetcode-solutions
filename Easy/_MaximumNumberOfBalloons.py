"""
LC#1189 - Maximum Number of Balloons [Easy]
Topic: Hash Map / Counting
ML Connection: Frequency counting here is the same core idea used in 
Bag-of-Words and building tokenizer vocabularies in NLP.
"""

from collections import Counter

class Solution(object):
    def maxNumberOfBalloons(self, text):
        count = Counter(text)
        need = Counter("balloon")
        return min(count[c] // need[c] for c in need)
