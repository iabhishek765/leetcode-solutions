"""
Problem: Stone Removal Game (LC #3360)
Difficulty: Easy
Link: https://leetcode.com/problems/stone-removal-game/

Approach:
- Simulate: moves remove 10, 9, 8, ... stones, alternating players
- Stop when the pile can't cover the current move
- The player who cannot move loses, so Alice wins if it is Bob's turn
  when the loop ends
- Time: O(1) (at most 10 moves) | Space: O(1)

ML Connection:
- Simulating a turn-based game step by step is the basic loop used in
  reinforcement learning environments.
"""

class Solution:
    def canAliceWin(self, n):
        take = 10
        alice = True
        while take > 0 and n >= take:
            n -= take
            take -= 1
            alice = not alice
        return not alice
