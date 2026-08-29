"""
LC#2948 - Make Lexicographically Smallest Array by Swapping Elements [Medium]
Topic: Greedy / Sorting / Grouping
ML Connection: Grouping elements by proximity and sorting within groups 
mirrors how clustering algorithms (K-means, DBSCAN) group nearby 
data points and process them independently.
"""

class Solution:
    def lexicographicallySmallestArray(self, nums: list, limit: int) -> list:
        n = len(nums)
        # pair each value with its original index, sort by value
        sorted_pairs = sorted(enumerate(nums), key=lambda x: x[1])

        result = [0] * n
        i = 0
        while i < n:
            j = i + 1
            # extend group while adjacent values within limit
            while j < n and sorted_pairs[j][1] - sorted_pairs[j-1][1] <= limit:
                j += 1

            # group = sorted_pairs[i:j]
            group = sorted_pairs[i:j]
            # original indices of this group, sorted
            indices = sorted(p[0] for p in group)
            # values already sorted (from sorted_pairs)
            values = [p[1] for p in group]

            # assign sorted values to sorted indices
            for idx, val in zip(indices, values):
                result[idx] = val

            i = j

        return result
