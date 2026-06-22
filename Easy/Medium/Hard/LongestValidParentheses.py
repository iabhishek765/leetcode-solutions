"""
LC#32 - Longest Valid Parentheses [Hard]
Topic: Stack
ML Connection: Tracking valid/invalid sequence boundaries with a stack 
is similar to how parsers validate structured input (e.g., JSON, syntax 
trees) before feeding data into ML pipelines.
"""

class Solution(object):
    def longestValidParentheses(self, s):
        max_len = 0
        stack = [-1]  # base index marker

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # new base marker
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
