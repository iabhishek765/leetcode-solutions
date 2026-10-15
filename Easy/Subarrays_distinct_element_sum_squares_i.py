"""
Problem: Subarrays Distinct Element Sum of Squares I (LC #2913)
Difficulty: Easy
Link: https://leetcode.com/problems/subarrays-distinct-element-sum-squares-i/

Approach:
- Brute force: for each start i, expand j to the right
- Use set to track distinct elements in current subarray
- Add len(set)^2 to result at each step
- Time: O(n²) | Space: O(n)

ML Connection:
- Distinct element counting is used in cardinality
  estimation for large ML datasets and databases
- Set-based deduplication is a preprocessing step
  in cleaning training data for ML models
"""

class Solution:
    def sumCounts(self, nums):
        n = len(nums)
        result = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                result += len(seen) ** 2
        return result
