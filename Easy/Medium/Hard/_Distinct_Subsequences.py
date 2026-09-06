"""
LC#115 - Distinct Subsequences [Hard]
Topic: Dynamic Programming
ML Connection: Counting subsequence matches is the core of 
sequence alignment algorithms — used in bioinformatics ML models 
for DNA/protein sequence analysis.
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # empty t can be formed from any prefix of s in exactly 1 way
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i-1][j]  # skip s[i-1]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]  # use s[i-1]

        return dp[m][n]
