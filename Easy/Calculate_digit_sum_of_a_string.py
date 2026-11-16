"""
Problem: Calculate Digit Sum of a String (LC #2243)
Difficulty: Easy
Link: https://leetcode.com/problems/calculate-digit-sum-of-a-string/

Approach:
- While len(s) > k, split s into chunks of size k
- Replace each chunk with the string of its digit sum
- Join the results and repeat
- Time: O(n) per round, rounds shrink quickly | Space: O(n)

ML Connection:
- Repeatedly splitting into groups and reducing each group is the
  same pattern as hierarchical aggregation (pooling/reduce steps)
  used when combining features in batches.
"""

class Solution:
    def digitSum(self, s, k):
        while len(s) > k:
            s = ''.join(
                str(sum(int(c) for c in s[i:i + k]))
                for i in range(0, len(s), k)
            )
        return s
