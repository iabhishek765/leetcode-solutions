"""
LC#3532 - Path Existence Queries in a Graph I [Medium]
Topic: Union-Find (DSU)
ML Connection: Union-Find is used in clustering algorithms like 
single-linkage hierarchical clustering — merging nearby data points.
"""

class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            a, b = find(a), find(b)
            if a != b:
                parent[a] = b

        # Since nums is sorted, only check adjacent nodes
        for i in range(n - 1):
            if nums[i+1] - nums[i] <= maxDiff:
                union(i, i+1)

        return [find(u) == find(v) for u, v in queries]
