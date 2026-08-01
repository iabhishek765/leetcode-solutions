# LC#69 - Sqrt(x)
# Difficulty: Easy
# Topics: Math, Binary Search
#
# Approach: Binary search between 1 and x//2.
#           If mid*mid == x → perfect square, return mid.
#           If mid*mid < x → answer in right half, left=mid+1
#           If mid*mid > x → answer in left half, right=mid-1
#           When loop ends, right = floor(sqrt(x))
# Time: O(log x) | Space: O(1)
#
# ML Connection: Binary search is used in hyperparameter
# tuning (bisection method) to find optimal learning rate
# or threshold values in ML model calibration

class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left = 1
        right = x // 2
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right
