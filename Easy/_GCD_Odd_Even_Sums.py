# LC#3658 - GCD of Odd and Even Sums
# Difficulty: Easy
# Topics: Math, Number Theory
#
# Approach: Use formulas - sum of first n odds = n^2,
#           sum of first n evens = n*(n+1), then apply GCD
# Time: O(log n) | Space: O(1)
#
# ML Connection: GCD and number theory are foundational in
# cryptographic protocols used to secure ML model APIs
# and federated learning communication

from math import gcd

class Solution:
    def gcdOfOddEvenSums(self, n):
        sum_odd = n * n
        sum_even = n * (n + 1)
        return gcd(sum_odd, sum_even)
