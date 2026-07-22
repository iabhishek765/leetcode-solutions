# LC#64 - Minimum Path Sum
# Difficulty: Medium
# Topics: Array, DP, Matrix
#
# Approach: Grid DP - dp[i][j] = min(dp[i-1][j], dp[i][j-1])
#           + grid[i][j]. Fill first row/col with prefix sums.
# Time: O(m*n) | Space: O(m*n)
#
# ML Connection: Minimum cost path in a grid is the foundation
# of Viterbi algorithm used in HMMs for speech recognition
# and NLP sequence labeling (POS tagging, NER)

class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[m-1][n-1]
