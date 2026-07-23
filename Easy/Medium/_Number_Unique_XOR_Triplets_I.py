# LC#3513 - Number of Unique XOR Triplets I
# Difficulty: Medium
# Topics: Array, Math, Bit Manipulation
#
# Approach: Since nums is permutation of [1..n], XOR triplets
#           can achieve all values 0 to (next_power_of_2 - 1).
#           Find smallest power of 2 > n, that's the count.
# Time: O(log n) | Space: O(1)
#
# ML Connection: XOR-based hashing and bit manipulation are
# used in locality-sensitive hashing (LSH) for approximate
# nearest neighbor search in high-dimensional ML embeddings

class Solution:
    def uniqueXorTriplets(self, nums):
        n = len(nums)
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        p = 1
        while p <= n:
            p <<= 1
        
        return p
