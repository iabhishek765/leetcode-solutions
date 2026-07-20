# LC#1260 - Shift 2D Grid
# Difficulty: Easy
# Topics: Array, Matrix, Simulation
#
# Approach: Flatten 2D to 1D, rotate array by k using
#           slicing, reshape back to m x n grid
# Time: O(m*n) | Space: O(m*n)
#
# ML Connection: Flattening and reshaping tensors is a
# core operation in CNN architectures when transitioning
# between convolutional and fully-connected layers

class Solution:
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        flat = [grid[i][j] for i in range(m) for j in range(n)]
        k = k % (m * n)
        flat = flat[-k:] + flat[:-k]
        return [flat[i*n:(i+1)*n] for i in range(m)]
