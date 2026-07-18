# LC#1979 - Find Greatest Common Divisor of Array
# Difficulty: Easy
# Topics: Array, Math, Number Theory
#
# Approach: GCD of smallest and largest only — no need to
#           check all pairs since divisors of min/max
#           constrain the answer completely
# Time: O(n) for min/max + O(log min) for gcd | Space: O(1)
#
# ML Connection: GCD is used in learning rate scheduling —
# cyclic LR schedules use GCD of epoch lengths to find
# the common period for resetting learning rates

from math import gcd

class Solution:
    def findGCD(self, nums):
        return gcd(min(nums), max(nums))
