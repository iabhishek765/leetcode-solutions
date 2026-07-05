"""
LC#1301 - Number of Paths with Max Score [Hard]
Topic: 2D DP
ML Connection: Tracking both max value and count simultaneously is 
used in Viterbi algorithm — finding most likely sequence + its count 
in Hidden Markov Models.
"""

class Solution(object):
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)
        
        dp  = [[0] * n for _ in range(n)]
        cnt = [[0] * n for _ in range(n)]
        
        cnt[n-1][n-1] = 1  # start cell 'S'
        
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i == n-1 and j == n-1) or board[i][j] in ('X', 'S'):
                    if board[i][j] == 'X':
                        cnt[i][j] = 0
                    continue
                
                val = 0 if board[i][j] == 'E' else int(board[i][j])
                
                # check 3 neighbors: down, right, diagonal
                for di, dj in [(1,0),(0,1),(1,1)]:
                    ni, nj = i+di, j+dj
                    if ni < n and nj < n and cnt[ni][nj] > 0:
                        if dp[ni][nj] + val > dp[i][j]:
                            dp[i][j] = dp[ni][nj] + val
                            cnt[i][j] = cnt[ni][nj]
                        elif dp[ni][nj] + val == dp[i][j]:
                            cnt[i][j] = (cnt[i][j] + cnt[ni][nj]) % MOD

        if cnt[0][0] == 0:
            return [0, 0]
        return [dp[0][0], cnt[0][0]]
