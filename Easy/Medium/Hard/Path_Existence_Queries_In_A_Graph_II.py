"""
LC#3534 - Path Existence Queries in a Graph II [Hard]
Topic: BFS + Sorted Neighbor Lookup
ML Connection: Efficient graph traversal with range-based neighbor 
finding mirrors how approximate nearest neighbor search works in 
vector databases for ML retrieval systems.
"""

import bisect

class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        # Sort nodes based on nums values
        order = sorted(range(n), key=lambda i: nums[i])
        vals = [nums[i] for i in order]

        # rank[node] = position in sorted order
        rank = [0] * n
        for i, node in enumerate(order):
            rank[node] = i

        # next_pos[i] = farthest position reachable
        # from position i in one step
        next_pos = [0] * n

        for i in range(n):
            next_pos[i] = bisect.bisect_right(
                vals, vals[i] + maxDiff
            ) - 1

        # Binary lifting table
        LOG = n.bit_length()
        jump = [next_pos]

        for k in range(1, LOG):
            prev = jump[k - 1]
            curr = [0] * n

            for i in range(n):
                curr[i] = prev[prev[i]]

            jump.append(curr)

        answer = []

        # Process every query
        for u, v in queries:
            left = rank[u]
            right = rank[v]

            if left > right:
                left, right = right, left

            # Same node
            if left == right:
                answer.append(0)
                continue

            # Check if path is impossible
            if next_pos[left] == left:
                answer.append(-1)
                continue

            steps = 0
            current = left

            # Use binary lifting
            for k in range(LOG - 1, -1, -1):
                nxt = jump[k][current]

                if nxt < right and nxt > current:
                    current = nxt
                    steps += (1 << k)

            # Final jump
            if next_pos[current] >= right:
                answer.append(steps + 1)
            else:
                answer.append(-1)

        return answer
