# LC3014 - Minimum Number of Pushes to Type Word I
# Difficulty: Easy
# Topics: Math, Greedy
#
# Approach: 8 keys available (2-9). Assign letters greedily.
#           Letter at index i costs (i//8 + 1) pushes.
#           First 8 → cost 1, next 8 → cost 2, etc.
#           Word has distinct letters so no frequency needed.
# Time: O(n) | Space: O(1)
#
# ML Connection: Optimal key assignment is a form of greedy
# encoding — similar to Huffman coding where frequent symbols
# get shorter codes to minimize total encoding cost

class Solution:
    def minimumPushes(self, word):
        n = len(word)
        result = 0
        for i in range(n):
            result += (i // 8) + 1
        return result
