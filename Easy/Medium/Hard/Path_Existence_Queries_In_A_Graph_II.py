"""
LC#3534 - Path Existence Queries in a Graph II [Hard]
Topic: BFS + Sorted Neighbor Lookup
ML Connection: Efficient graph traversal with range-based neighbor 
finding mirrors how approximate nearest neighbor search works in 
vector databases for ML retrieval systems.
"""

from collections import deque
import bisect

class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        # sort indices by nums value for range-based neighbor lookup
        sorted_idx = sorted(range(n), key=lambda i: nums[i])
        sorted_vals = [nums[i] for i in sorted_idx]
        rank = [0] * n  # rank[node] = position in sorted_idx
        for p, i in enumerate(sorted_idx):
            rank[i] = p

        def bfs(src, dst):
            if src == dst:
                return 0
            dist = [-1] * n
            dist[src] = 0
            q = deque([src])
            # unvisited positions in sorted order
            unvisited = list(range(n))
            unvisited_set = set(range(n))
            unvisited_set.remove(src)

            while q:
                u = q.popleft()
                lo = bisect.bisect_left(sorted_vals, nums[u] - maxDiff)
                hi = bisect.bisect_right(sorted_vals, nums[u] + maxDiff)
                to_visit = []
                for p in range(lo, hi):
                    v = sorted_idx[p]
                    if v in unvisited_set:
                        to_visit.append(v)
                for v in to_visit:
                    unvisited_set.remove(v)
                    dist[v] = dist[u] + 1
                    if v == dst:
                        return dist[v]
                    q.append(v)
            return -1

        return [bfs(u, v) for u, v in queries]
