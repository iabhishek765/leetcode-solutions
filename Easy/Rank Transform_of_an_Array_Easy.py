# LC#1331 - Rank Transform of an Array
# Difficulty: Easy
# Topics: Array, Hash Table, Sorting
#
# Approach: Sort unique elements, assign rank 1,2,3...
#           via enumeration, then map original array using dict
# Time: O(n log n) | Space: O(n)
#
# ML Connection: Rank transformation is a core preprocessing
# step in ML — used in rank-based feature scaling and
# Spearman correlation, which is robust to outliers unlike
# Pearson correlation

class Solution:
    def arrayRankTransform(self, arr):
        rank_map = {v: i+1 for i, v in enumerate(sorted(set(arr)))}
        return [rank_map[v] for v in arr]
