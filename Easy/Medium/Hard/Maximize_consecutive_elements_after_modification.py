"""
Problem: Maximize Consecutive Elements in an Array After Modification (LC #3041)
Difficulty: Hard
Link: https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

Approach:
- Each element can stay x or become x+1
- Sort, then dp[v] = longest consecutive run ending at value v
- For each x (ascending): update dp[x+1] from dp[x] first, then dp[x]
  from dp[x-1], so one element is never used for both values
- Answer is the maximum dp value
- Time: O(n log n) | Space: O(n)

ML Connection:
- Sorting then extending runs with a lookup table is the same idea
  as bucketing/discretizing values before building count features.
"""

class Solution:
    def maxSelectedElements(self, nums):
        nums.sort()
        dp = {}
        best = 1
        for x in nums:
            dp[x + 1] = max(dp.get(x + 1, 0), dp.get(x, 0) + 1)
            dp[x] = max(dp.get(x, 0), dp.get(x - 1, 0) + 1)
            best = max(best, dp[x], dp[x + 1])
        return best
