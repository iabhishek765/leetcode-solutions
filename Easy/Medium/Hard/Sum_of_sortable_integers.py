"""
Problem: Sum of Sortable Integers (LC #3886)
Difficulty: Hard
Link: https://leetcode.com/problems/sum-of-sortable-integers/

Approach:
- k is sortable if k divides n AND each chunk of k elements
  in original array has same multiset as corresponding chunk
  in globally sorted array (rotation can fix order within chunk)
- Check all divisors of n, validate each chunk
- Time: O(n * d(n) * k log k) where d(n) = number of divisors
- Space: O(n)

ML Connection:
- Chunk-based validation mirrors mini-batch checking
  in data pipeline validation for ML training
- Divisor enumeration appears in grid search for
  batch size selection in deep learning training
"""

class Solution:
    def sortableIntegers(self, nums):
        n = len(nums)
        sorted_nums = sorted(nums)
        result = 0

        def is_rotation_sortable(chunk):
            
            k = len(chunk)
            descents = sum(1 for i in range(k) if chunk[i] > chunk[(i+1) % k])
            return descents <= 1

        for k in range(1, n + 1):
            if n % k != 0:
                continue
            valid = True
            for i in range(0, n, k):
                chunk = nums[i:i+k]
                
                if sorted(chunk) != sorted_nums[i:i+k]:
                    valid = False
                    break
                
                if not is_rotation_sortable(chunk):
                    valid = False
                    break
            if valid:
                result += k

        return result
