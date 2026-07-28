# LC#3517 - Smallest Palindromic Rearrangement I
# Difficulty: Medium
# Topics: String, Greedy, Sorting, Hash Table
#
# Approach: Count char frequencies. Sort chars ascending.
#           Build left half using pairs (in sorted order).
#           Find odd-count char for middle.
#           Result = left + middle + reverse(left)
# Time: O(n log n) | Space: O(n)
#
# ML Connection: Frequency counting + greedy ordering mirrors
# Huffman encoding used in lossless compression of ML model
# weights and tokenizer vocabulary construction

from collections import Counter

class Solution:
    def smallestPalindrome(self, s):
        count = Counter(s)
        
        half = []
        middle = ''
        
        for ch in sorted(count.keys()):
            pairs = count[ch] // 2
            half.extend([ch] * pairs)
            if count[ch] % 2 == 1:
                middle = ch
        
        left = ''.join(half)
        return left + middle + left[::-1]
