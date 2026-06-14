"""
Problem: Maximum Twin Sum of a Linked List (LC #2130)
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

Approach:
- Traverse list and store all values in array
- Twin of node i is node (n-1-i)
- Find max of all twin sums using two pointers on array
- Time: O(n) | Space: O(n)

ML Connection:
- Symmetric pairing is used in Siamese Networks
  where twin inputs are compared for similarity
- Used in face verification and sentence similarity
  models in deep learning
"""

class Solution(object):
    def pairSum(self, head):
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        max_sum = 0
        n = len(vals)
        for i in range(n // 2):
            max_sum = max(max_sum, vals[i] + vals[n - 1 - i])

        return max_sum
