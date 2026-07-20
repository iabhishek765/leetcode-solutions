# LC#62 - Unique Paths
# Difficulty: Medium
# Topics: Math, DP, Combinatorics
#
# Approach: DP - dp[i][j] = dp[i-1][j] + dp[i][j-1]
#           Each cell = sum of paths from top and left
#           First row and column are all 1s (only one way)
# Time: O(m*n) | Space: O(m*n)
#
# ML Connection: Grid DP is foundational to dynamic
# programming in sequence alignment (used in NLP) and
# Viterbi algorithm for Hidden Markov Models in speech
# recognition and NLP tagging tasks

class Solution:
    def uniquePaths(self, m, n):
        dp = [[1] * n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
