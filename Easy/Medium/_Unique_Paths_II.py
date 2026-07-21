# LC#63 - Unique Paths II
# Difficulty: Medium
# Topics: Array, DP, Matrix
#
# Approach: Same as LC#62 but obstacles = 0 paths.
#           Handle first row/col carefully — once blocked,
#           all cells after it in that row/col are also 0
# Time: O(m*n) | Space: O(m*n)
#
# ML Connection: Obstacle-aware pathfinding is used in
# robot navigation with occupancy grids — a core problem
# in robotics ML where agents must plan collision-free paths

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(1, m):
            dp[i][0] = 0 if obstacleGrid[i][0] == 1 else dp[i-1][0]
        
        for j in range(1, n):
            dp[0][j] = 0 if obstacleGrid[0][j] == 1 else dp[0][j-1]
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
