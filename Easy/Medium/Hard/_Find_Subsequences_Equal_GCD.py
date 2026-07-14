# LC#3336 - Find the Number of Subsequences With Equal GCD
# Difficulty: Hard
# Topics: Array, Math, DP, Number Theory
#
# Approach: DP with state (gcd1, gcd2) tracking GCDs of two
#           disjoint subsequences. For each num: skip, add to
#           seq1, or add to seq2. Count states where g1==g2!=0
# Time: O(n * M^2) where M = max(nums) | Space: O(M^2)
#
# ML Connection: GCD-based grouping relates to lattice structures
# in number theory used in cryptographic ML models and
# factorization machines for recommendation systems

from math import gcd

class Solution:
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7
        dp = {}
        
        for num in nums:
            new_dp = {}
            for (g1, g2), cnt in dp.items():
                new_dp[(g1, g2)] = (new_dp.get((g1, g2), 0) + cnt) % MOD
            for (g1, g2), cnt in dp.items():
                ng1 = gcd(g1, num)
                new_dp[(ng1, g2)] = (new_dp.get((ng1, g2), 0) + cnt) % MOD
            for (g1, g2), cnt in dp.items():
                ng2 = gcd(g2, num)
                new_dp[(g1, ng2)] = (new_dp.get((g1, ng2), 0) + cnt) % MOD
            new_dp[(num, 0)] = (new_dp.get((num, 0), 0) + 1) % MOD
            new_dp[(0, num)] = (new_dp.get((0, num), 0) + 1) % MOD
            dp = new_dp
        
        result = 0
        for (g1, g2), cnt in dp.items():
            if g1 == g2 and g1 != 0:
                result = (result + cnt) % MOD
        return result
