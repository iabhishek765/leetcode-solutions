"""
LC#3754 - Concatenate Non-Zero Digits and Multiply by Sum I [Easy]
Topic: String / Math
ML Connection: Digit filtering and feature extraction from raw numbers
is used in data preprocessing pipelines before feeding into models.
"""

class Solution(object):
    def sumAndMultiply(self, n):
        digits = [d for d in str(n) if d != '0']
        if not digits:
            return 0
        x = int("".join(digits))
        s = sum(int(d) for d in digits)
        return x * s
