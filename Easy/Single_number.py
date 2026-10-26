"""
Problem: Single Number (LC #136)
Difficulty: Easy
Link: https://leetcode.com/problems/single-number/

Approach:
- XOR all numbers together
- Pairs cancel out (a ^ a = 0)
- Single element remains (0 ^ a = a)
- Time: O(n) | Space: O(1)

ML Connection:
- XOR is a fundamental operation in binary neural
  networks for ultra-efficient model inference
- Bit-level operations are used in hashing features
  for memory-efficient ML at scale (feature hashing)
"""

class Solution:
    def singleNumber(self, nums):
        result = 0
        for n in nums:
            result ^= n
        return result
