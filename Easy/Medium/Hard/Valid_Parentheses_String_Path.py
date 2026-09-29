# LC#2267 - Check if There Is a Valid Parentheses String Path
# Difficulty: Hard
# Topics: Grid, DP, BFS
#
# Approach: DP where dp[i][j] = set of possible open-bracket
#           balance values reachable at cell (i,j).
#           '(' adds 1, ')' subtracts 1. Discard negatives.
#           Valid if balance 0 reachable at bottom-right.
#           Early exit if path length m+n-1 is odd.
# Time: O(m*n*(m+n)) | Space: O(m*n*(m+n))
#
# ML Connection: Tracking set of possible states at each
# grid cell mirrors beam search in seq2seq models where
# multiple candidate sequences are tracked simultaneously
# through a decoding grid.

class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 == 1:
            return False
        
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        if grid[0][0] == '(':
            dp[0][0].add(1)
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                candidates = set()
                if i > 0:
                    candidates |= dp[i-1][j]
                if j > 0:
                    candidates |= dp[i][j-1]
                
                for bal in candidates:
                    new_bal = bal + 1 if grid[i][j] == '(' else bal - 1
                    if new_bal >= 0:
                        dp[i][j].add(new_bal)
        
        return 0 in dp[m-1][n-1]
