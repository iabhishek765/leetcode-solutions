"""
LC#1621 - Number of Sets of K Non-Overlapping Line Segments [Medium]
Topic: Math / Combinatorics
ML Connection: Counting valid configurations under constraints mirrors 
how combinatorial search spaces are estimated in neural architecture 
search (NAS) — computing valid layer combinations.
"""

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        def comb(n, r, mod):
            if r > n:
                return 0
            num = den = 1
            for i in range(r):
                num = num * (n - i) % mod
                den = den * (i + 1) % mod
            return num * pow(den, mod - 2, mod) % mod

        return comb(n + k - 1, 2 * k, MOD)
