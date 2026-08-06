"""
LC#3345 - Smallest Divisible Digit Product I [Easy]
Topic: Math / Brute Force
ML Connection: Digit product constraints are used in combinatorial 
feature generation — filtering valid feature combinations by 
multiplicative properties.
"""

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for num in range(n, 10001):
            product = 1
            for d in str(num):
                product *= int(d)
            if product % t == 0:
                return num
