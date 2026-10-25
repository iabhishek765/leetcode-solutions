"""
Problem: Candy (LC #135)
Difficulty: Hard
Link: https://leetcode.com/problems/candy/

Approach:
- Start with 1 candy each
- Left→right pass: rating > left neighbor → +1 candy
- Right→left pass: rating > right neighbor → max(current, right+1)
- Two passes ensure both neighbor constraints satisfied
- Time: O(n) | Space: O(n)

ML Connection:
- Two-pass dynamic programming mirrors forward-backward
  algorithm in Hidden Markov Models used in NLP/speech
- Greedy constraint satisfaction appears in reward
  shaping techniques in reinforcement learning
"""

class Solution:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)
