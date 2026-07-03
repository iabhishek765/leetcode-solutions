"""
LC#3620 - Network Recovery Pathways [Hard]
Topic: Binary Search + Topological Sort DP (DAG)
ML Connection: DAG shortest path with constraints mirrors 
computation graph optimization in ML frameworks like PyTorch.
"""

from collections import defaultdict, deque

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        graph = defaultdict(list)
        in_degree = [0] * n
        all_costs = set()

        for u, v, cost in edges:
            graph[u].append((v, cost))
            in_degree[v] += 1
            all_costs.add(cost)

        # Topological sort once (reuse for all binary search checks)
        topo = []
        temp = in_degree[:]
        q = deque([i for i in range(n) if temp[i] == 0])
        while q:
            node = q.popleft()
            topo.append(node)
            for v, _ in graph[node]:
                temp[v] -= 1
                if temp[v] == 0:
                    q.append(v)

        all_costs = sorted(all_costs)

        def canReach(min_cost):
            dist = [float('inf')] * n
            dist[0] = 0
            for u in topo:
                if dist[u] == float('inf'):
                    continue
                for v, cost in graph[u]:
                    if cost < min_cost:
                        continue
                    if v != n - 1 and not online[v]:
                        continue
                    nd = dist[u] + cost
                    if nd < dist[v]:
                        dist[v] = nd
            return dist[n - 1] <= k

        lo, hi, ans = 0, len(all_costs) - 1, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if canReach(all_costs[mid]):
                ans = all_costs[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
