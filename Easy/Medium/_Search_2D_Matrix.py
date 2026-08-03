# LC#74 - Search a 2D Matrix
# Difficulty: Medium
# Topics: Array, Binary Search, Matrix
#
# Approach: Treat m×n matrix as sorted 1D array.
#           Binary search on virtual flat index 0 to m*n-1.
#           Convert flat mid index to 2D: row=mid//n, col=mid%n
# Time: O(log(m*n)) | Space: O(1)
#
# ML Connection: Efficient matrix search is core to attention
# mechanisms in transformers where key-value lookups in
# large embedding matrices must be done in O(log n) time
# using approximate nearest neighbor search

class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // n][mid % n]
            
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
