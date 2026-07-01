"""
LC#2812 - Find the Safest Path in a Grid [Medium]
Topic: Multi-source BFS + Binary Search
ML Connection: Multi-source BFS is used in robotics path planning and 
safe zone detection — finding cells furthest from obstacles, similar 
to safety margins in reinforcement learning environments.
"""

from collections import deque

class Solution(object):
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        dq = deque()

        # Step 1: multi-source BFS from all thieves
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    dq.append((r, c))

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while dq:
            r, c = dq.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    dq.append((nr, nc))

        # Step 2: binary search on safeness value
        def canReach(safe):
            if dist[0][0] < safe or dist[n-1][n-1] < safe:
                return False
            visited = [[False] * n for _ in range(n)]
            q = deque([(0, 0)])
            visited[0][0] = True
            while q:
                r, c = q.popleft()
                if r == n-1 and c == n-1:
                    return True
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and dist[nr][nc] >= safe:
                        visited[nr][nc] = True
                        q.append((nr, nc))
            return False

        lo, hi, ans = 0, n, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if canReach(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
