"""
Problem: Valid Parentheses (LC #20)
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/

Approach:
- Use a stack to track opening brackets
- For every closing bracket, check if top of stack matches
- If stack is empty at end, all brackets matched
- Time: O(n) | Space: O(n)

ML Connection:
- Stack-based parsing is used in expression trees
  which are the basis of decision tree splitting logic
- Bracket matching logic appears in tokenizers used
  in NLP preprocessing pipelines
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack
