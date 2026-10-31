"""
Problem: Twisted Mirror Path Count (LC #3665)
Difficulty: Medium
Link: https://leetcode.com/problems/twisted-mirror-path-count/

Approach:
- dp[i][j] = number of ways to land on cell (i, j)
- From each cell, try moving right and down
- If the target is a mirror, keep reflecting until a free cell
  or out of bounds (right -> down, down -> right)
- Every move increases i + j, so row-major order is valid
- Time: O(m * n * (m + n)) worst case | Space: O(m * n)

ML Connection:
- Grid path counting is the basis of state-transition
  counting in reinforcement learning environments
- Reflection rules resemble deterministic transition
  functions in Markov decision processes
"""

class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0 or (i, j) == (m - 1, n - 1):
                    continue
                for d in (0, 1):
                    ni, nj = (i, j + 1) if d == 0 else (i + 1, j)
                    direction = d
                    while ni < m and nj < n and grid[ni][nj] == 1 and (ni, nj) != (m - 1, n - 1):
                        if direction == 0:
                            direction = 1
                            ni += 1
                        else:
                            direction = 0
                            nj += 1
                    if ni < m and nj < n:
                        dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % MOD

        return dp[m - 1][n - 1] % MOD
