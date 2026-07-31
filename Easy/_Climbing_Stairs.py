# LC#70 - Climbing Stairs
# Difficulty: Easy
# Topics: Math, DP, Memoization
#
# Approach: Classic Fibonacci DP - ways(n) = ways(n-1) + ways(n-2)
#           Use two variables instead of array to save space.
#           Base cases: n=1 → 1, n=2 → 2
# Time: O(n) | Space: O(1)
#
# ML Connection: Fibonacci recurrence appears in analyzing
# complexity of recursive neural architectures and in
# dynamic programming used for sequence model decoding.
# Space-optimized DP (rolling variables) is used in
# memory-efficient transformer implementations.

class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        
        prev2 = 1
        prev1 = 2
        
        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return prev1
