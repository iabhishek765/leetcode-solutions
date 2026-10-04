"""
Problem: Valid Parenthesis String (LC #678)
Difficulty: Medium
Link: https://leetcode.com/problems/valid-parenthesis-string/

Approach:
- Track range [min_open, max_open] of possible open counts
- '(' increases both, ')' decreases both
- '*' decreases min (treat as ')') and increases max (treat as '(')
- If max_open < 0 at any point → impossible → False
- Clamp min_open to 0 (can't have negative opens)
- At end, valid if min_open == 0
- Time: O(n) | Space: O(1)

ML Connection:
- Range tracking (min/max bounds) is used in
  interval arithmetic for neural network verification
- Greedy range shrinking appears in beam search
  pruning used in sequence generation models
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0

        for c in s:
            if c == '(':
                min_open += 1
                max_open += 1
            elif c == ')':
                min_open -= 1
                max_open -= 1
            else:  # '*'
                min_open -= 1
                max_open += 1

            if max_open < 0:
                return False
            min_open = max(min_open, 0)

        return min_open == 0
