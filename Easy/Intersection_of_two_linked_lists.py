"""
Problem: Intersection of Two Linked Lists (LC #160)
Difficulty: Easy
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/

Approach:
- Two pointers a and b start at headA and headB
- When one reaches the end, redirect it to the other list's head
- Both then walk lenA + lenB steps in total, so they meet at the
  intersection node (or both reach None if no intersection)
- Compare node identity with `is`
- Time: O(m + n) | Space: O(1)

ML Connection:
- Aligning two sequences of different lengths by traversing
  both fully is the same idea as padding/aligning variable-length
  inputs before comparing them.
"""

class Solution:
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
