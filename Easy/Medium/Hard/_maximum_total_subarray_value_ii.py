"""
Problem: Maximum Total Subarray Value II (LC #3691)
Difficulty: Hard
Link: https://leetcode.com/problems/maximum-total-subarray-value-ii/

Approach:
- Value of each subarray = max - min
- Subarrays must be distinct (same l,r can't repeat)
- Generate all subarray values, sort descending
- Pick top k values and sum them
- Time: O(n² log n) | Space: O(n²)

ML Connection:
- Selecting top-k features by score is exactly what
  SelectKBest does in scikit-learn feature selection
- Max-min range is used in data normalization and
  outlier detection in ML preprocessing pipelines
"""

import heapq

class Solution(object):
    def maxTotalValue(self, nums, k):
        n = len(nums)
        all_values = []

        for l in range(n):
            cur_max = nums[l]
            cur_min = nums[l]
            for r in range(l, n):
                cur_max = max(cur_max, nums[r])
                cur_min = min(cur_min, nums[r])
                all_values.append(cur_max - cur_min)

        all_values.sort(reverse=True)
        return sum(all_values[:k])
