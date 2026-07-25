# LC#3536 - Maximum Product of Two Digits
# Difficulty: Easy
# Topics: Math, Sorting
#
# Approach: Extract digits as list, sort descending,
#           return product of first two (largest pair)
# Time: O(d log d) | Space: O(d) where d = digits count
#
# ML Connection: Finding top-k elements by value is a core
# operation in beam search decoding and top-k sampling
# used in LLM text generation (GPT, LLaMA inference)

class Solution:
    def maxProduct(self, n):
        digits = sorted([int(d) for d in str(n)], reverse=True)
        return digits[0] * digits[1]
