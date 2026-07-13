# LC#1291 - Sequential Digits
# Difficulty: Medium
# Topics: Enumeration, Sliding Window on String
#
# Approach: Slide a window of increasing length over "123456789"
#           Convert each window to int, check if in [low, high]
#           Result is naturally sorted since we go length by length
# Time: O(1) | Space: O(1) — at most 36 such numbers exist
#
# ML Connection: Fixed-alphabet enumeration is used in
# tokenization schemes where vocabulary is built by sliding
# windows over a fixed character set (BPE tokenization)

class Solution:
    def sequentialDigits(self, low, high):
        result = []
        digits = "123456789"
        
        for length in range(2, 10):
            for start in range(9 - length + 1):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    result.append(num)
        
        return result
