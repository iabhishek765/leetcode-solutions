# LC#54 - Spiral Matrix
# Difficulty: Medium
# Topics: Array, Matrix, Simulation
#
# Approach: Boundary shrinking - maintain top/bottom/left/right
#           pointers, traverse each edge then shrink inward.
#           Guard conditions prevent double-counting single rows/cols
# Time: O(m*n) | Space: O(1) excluding output
#
# ML Connection: Spiral/sequential matrix traversal appears in
# convolutional neural networks where feature maps are scanned
# in specific spatial patterns for pooling and attention operations

class Solution:
    def spiralOrder(self, matrix):
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        
        return result
