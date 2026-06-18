# LC#29 - Divide Two Integers
# Difficulty: Medium
# Topics: Math, Bit Manipulation
#
# Approach: Bit shifting - double divisor with left shift (<<1)
#           to find largest multiple that fits in dividend,
#           subtract and accumulate result, repeat
# Time: O(log^2 n) | Space: O(1)
#
# ML Connection: Bit shifting and fixed-point arithmetic are used
# in quantized neural networks (INT8/INT4) where division/scaling
# is done via shifts to avoid costly floating point operations
# on edge devices

class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        negative = (dividend < 0) != (divisor < 0)
        a = abs(dividend)
        b = abs(divisor)
        result = 0
        
        while a >= b:
            temp = b
            multiple = 1
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            a -= temp
            result += multiple
        
        return -result if negative else result
