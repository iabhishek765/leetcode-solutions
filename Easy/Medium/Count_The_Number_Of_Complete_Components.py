"""
LC#2685 - Count the Number of Complete Components [Medium]
Topic: Union-Find / Graph
ML Connection: Complete subgraph detection is used in clique-finding 
algorithms — identifying fully connected neuron groups in neural 
network pruning and community detection in graph ML.
"""

from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n, edges):
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            a, b = find(a), find(b)
            if a == b:
                return
            if rank[a] < rank[b]:
                a, b = b, a
            parent[b] = a
            if rank[a] == rank[b]:
                rank[a] += 1

        for u, v in edges:
            union(u, v)

        node_count = defaultdict(int)
        edge_count = defaultdict(int)

        for i in range(n):
            node_count[find(i)] += 1

        for u, v in edges:
            edge_count[find(u)] += 1

        ans = 0
        for root in node_count:
            k = node_count[root]
            if edge_count[root] == k * (k - 1) // 2:
                ans += 1

        return ans
