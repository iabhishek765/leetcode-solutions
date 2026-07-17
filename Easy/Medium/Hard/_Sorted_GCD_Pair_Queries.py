# LC#3312 - Sorted GCD Pair Queries
# Difficulty: Hard
# Topics: Array, Math, Binary Search, Number Theory, Prefix Sum
#
# Approach: Count pairs with exact GCD g using frequency array
#           + inclusion-exclusion (Mobius-style). Build prefix
#           sum over GCD counts, binary search for each query
# Time: O(M log M + Q log M) where M = max(nums) | Space: O(M)
#
# ML Connection: Inclusion-exclusion counting over divisors
# mirrors feature interaction counting in factorization machines
# used for CTR prediction in recommendation systems

from math import gcd
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums, queries):
        max_val = max(nums)
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1
        
        cnt = [0] * (max_val + 1)
        for g in range(1, max_val + 1):
            div_count = sum(freq[g::g])
            cnt[g] = div_count * (div_count - 1) // 2
        
        for g in range(max_val, 0, -1):
            for multiple in range(2 * g, max_val + 1, g):
                cnt[g] -= cnt[multiple]
        
        prefix = []
        total = 0
        for g in range(1, max_val + 1):
            total += cnt[g]
            prefix.append(total)
        
        result = []
        for q in queries:
            idx = bisect_right(prefix, q)
            result.append(idx + 1)
        
        return result
