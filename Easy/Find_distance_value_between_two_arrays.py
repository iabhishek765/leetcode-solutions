"""
Problem: Find the Distance Value Between Two Arrays (LC #1385)
Difficulty: Easy
Link: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

Approach:
- Sort arr2, then binary search for the closest value to each x
- Only the first element >= x and the one before it can be nearest
- If neither is within d, x contributes to the count
- Time: O((n + m) log m) | Space: O(1) extra

ML Connection:
- Finding the nearest neighbor of a point in a sorted set is
  the core step of KNN and of nearest-centroid assignment.
"""

from bisect import bisect_left

class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        count = 0
        for x in arr1:
            i = bisect_left(arr2, x)
            near_right = i < len(arr2) and arr2[i] - x <= d
            near_left = i > 0 and x - arr2[i - 1] <= d
            if not near_right and not near_left:
                count += 1
        return count
