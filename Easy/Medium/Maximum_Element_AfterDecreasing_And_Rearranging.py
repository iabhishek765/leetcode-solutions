"""
LC#1846 - Maximum Element After Decreasing and Rearranging [Medium]
Topic: Greedy + Sorting
ML Connection: Greedily capping growth step-by-step is similar to 
gradient clipping — limiting how much a value can increase per step 
to keep the sequence stable.
"""

class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        prev = 1
        arr[0] = 1  # first element must be 1

        for i in range(1, len(arr)):
            arr[i] = min(arr[i], prev + 1)
            prev = arr[i]

        return prev
