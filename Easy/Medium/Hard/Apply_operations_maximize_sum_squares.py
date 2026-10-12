"""
Problem: Apply Operations on Array to Maximize Sum of Squares (LC #2897)
Difficulty: Hard
Link: https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

Approach:
- Key insight: AND+OR ops can freely redistribute bits across array
- Count total set bits at each bit position across all numbers
- Greedily build k largest numbers by using available bits
- Square each and sum with modulo
- Time: O(32 * n + 32 * k) | Space: O(32)

ML Connection:
- Bit manipulation for feature extraction is used in
  locality sensitive hashing (LSH) for fast similarity search
- Greedy selection of top-k features mirrors SelectKBest
  in scikit-learn for dimensionality reduction
"""

class Solution:
    def maxSum(self, nums, k):
        MOD = 10**9 + 7

        bit_count = [0] * 32
        for num in nums:
            for i in range(32):
                if num & (1 << i):
                    bit_count[i] += 1

        result = 0
        for _ in range(k):
            num = 0
            for i in range(32):
                if bit_count[i] > 0:
                    num |= (1 << i)
                    bit_count[i] -= 1
            result = (result + num * num) % MOD

        return result
