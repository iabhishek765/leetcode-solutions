# LC#3514 - Number of Unique XOR Triplets II
# Difficulty: Medium
# Topics: Array, Bit Manipulation, Hash Table
#
# Approach: Two-pass set approach - first collect all unique
#           pairwise XORs (i<=j), then XOR each with every
#           element (extending to k). Count unique results.
# Time: O(n^2) | Space: O(n^2)
#
# ML Connection: XOR-based feature hashing is used in the
# "hashing trick" for high-dimensional sparse feature spaces
# in online learning (Vowpal Wabbit, sklearn HashingVectorizer)

class Solution:
    def uniqueXorTriplets(self, nums):
        pair_xors = set()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                pair_xors.add(nums[i] ^ nums[j])
        
        result = set()
        for px in pair_xors:
            for num in nums:
                result.add(px ^ num)
        
        return len(result)
