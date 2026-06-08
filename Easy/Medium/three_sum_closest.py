"""
Problem: 3Sum Closest (LC #16)
Difficulty: Medium
Link: https://leetcode.com/problems/3sum-closest/

Approach:
- Sort the array first
- Use three pointers: fix i, move left & right
- Track closest sum using absolute difference
- Time: O(n²) | Space: O(1)

ML Connection:
- Two-pointer technique is used in similarity search
  and nearest neighbor algorithms (like KNN in ML)
- Sorting + search pattern appears in vector databases
  used for embedding retrieval in LLMs
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum
        
        return closest_sum
