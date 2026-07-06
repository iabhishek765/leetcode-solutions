"""
LC#48 - Rotate Image [Medium]
Topic: Matrix / In-place Manipulation
ML Connection: Image rotation is a core data augmentation technique 
in CNNs — rotating training images improves model generalization.
"""

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        # Step 1: Transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()
