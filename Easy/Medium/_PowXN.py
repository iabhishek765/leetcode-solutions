"""
LC#50 - Pow(x, n) [Medium]
Topic: Math / Binary Exponentiation
ML Connection: Fast matrix exponentiation (same idea) is used to 
speed up linear RNNs and long-range sequence models in ML research.
"""

class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1.0 / x
            n = -n

        result = 1.0
        while n:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result
