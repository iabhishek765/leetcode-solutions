"""
Problem: 4Sum (LC #18)
Difficulty: Medium
Link: https://leetcode.com/problems/4sum/

Approach:
- Sort the array first
- Fix two pointers i and j, use two-pointer for remaining two
- Skip duplicates at every level (i, j, beg, end)
- Time: O(n³) | Space: O(1)

ML Connection:
- Multi-pointer search is used in similarity matching
  and clustering algorithms like K-Means
- Duplicate skipping logic appears in data deduplication
  pipelines used in ML data preprocessing
"""

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                beg, end = j + 1, n - 1

                while beg < end:
                    total = nums[i] + nums[j] + nums[beg] + nums[end]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[beg], nums[end]])
                        while beg < end and nums[beg] == nums[beg+1]:
                            beg += 1
                        while beg < end and nums[end] == nums[end-1]:
                            end -= 1
                        beg += 1
                        end -= 1

                    elif total < target:
                        beg += 1
                    else:
                        end -= 1

        return ans
