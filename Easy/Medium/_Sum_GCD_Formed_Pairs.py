# LC#3867 - Sum of GCD of Formed Pairs
# Difficulty: Medium
# Topics: Array, Math, Sorting, Number Theory
#
# Approach: Build prefixGcd[i] = gcd(nums[i], max(nums[0..i]))
#           Sort prefixGcd, pair smallest+largest with two
#           pointers, sum GCD of each pair
# Time: O(n log n) | Space: O(n)
#
# ML Connection: Prefix aggregations (running max, running GCD)
# are used in online learning algorithms where model parameters
# are updated incrementally as new data arrives

from math import gcd

class Solution:
    def gcdSum(self, nums):
        prefix_gcd = []
        max_so_far = 0
        
        for num in nums:
            max_so_far = max(max_so_far, num)
            prefix_gcd.append(gcd(num, max_so_far))
        
        prefix_gcd.sort()
        
        result = 0
        left, right = 0, len(prefix_gcd) - 1
        
        while left < right:
            result += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1
        
        return result
