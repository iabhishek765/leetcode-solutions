"""
LC#3620 - Network Recovery Pathways [Hard]
Topic: Binary Search + Dijkstra (Modified)
ML Connection: Finding max-min cost paths under constraints mirrors 
resource-constrained routing in distributed ML systems — e.g., 
maximizing the weakest link in a model-parallel training pipeline.
"""

import heapq
from collections import defaultdict

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        graph = defaultdict(list)
        for u, v, cost in edges:
            graph[u].append((v, cost))

        # costs sorted uniquely for binary search
        all_costs = sorted(set(c for _, _, c in edges))

        def canAchieve(min_score):
            # Dijkstra: minimize total cost, only use edges >= min_score
            # only traverse online intermediate nodes
            dist = [float('inf')] * n
            dist[0] = 0
            heap = [(0, 0)]  # (total_cost, node)

            while heap:
                total, u = heapq.heappop(heap)
                if total > dist[u]:
                    continue
                if u == n - 1:
                    return True
                for v, cost in graph[u]:
                    if cost < min_score:
                        continue
                    if v != n - 1 and not online[v]:
                        continue
                    new_cost = total + cost
                    if new_cost <= k and new_cost < dist[v]:
                        dist[v] = new_cost
                        heapq.heappush(heap, (new_cost, v))

            return dist[n-1] <= k

        ans = -1
        lo, hi = 0, len(all_costs) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if canAchieve(all_costs[mid]):
                ans = all_costs[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
