"""
Problem: Remove Outermost Parentheses (LC #1021)
Difficulty: Easy
Link: https://leetcode.com/problems/remove-outermost-parentheses/

Approach:
- Track depth of nesting
- Add '(' only when depth > 0 (not outermost), then increment
- Decrement depth first for ')', add only when depth > 0
- Time: O(n) | Space: O(n)

ML Connection:
- Depth tracking mirrors hidden state in RNNs/LSTMs
  where bracket nesting = sequence context tracking
- Stack depth logic appears in expression parsers
  used in symbolic math for ML research tools
"""

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0

        for c in s:
            if c == '(':
                if depth > 0:
                    result.append(c)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    result.append(c)

        return ''.join(result)
