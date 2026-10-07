"""
Problem: Remove Invalid Parentheses (LC #301)
Difficulty: Hard
Link: https://leetcode.com/problems/remove-invalid-parentheses/

Approach:
- BFS level by level, each level removes one more character
- At first level where valid strings found, collect all and stop
- Use visited set to avoid duplicate candidates
- is_valid: count open brackets, return True if ends at 0
- Time: O(2^n) | Space: O(2^n)

ML Connection:
- BFS state-space search is used in reinforcement learning
  for exploring action spaces in model-based RL
- Level-by-level exploration mirrors breadth-first
  hyperparameter search in AutoML pipelines
"""

from collections import deque

class Solution:
    def removeInvalidParentheses(self, s):
        def is_valid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        visited = {s}
        queue = deque([s])
        result = []
        found = False

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if is_valid(curr):
                    result.append(curr)
                    found = True
                if found:
                    continue
                for i in range(len(curr)):
                    if curr[i] not in '()':
                        continue
                    candidate = curr[:i] + curr[i+1:]
                    if candidate not in visited:
                        visited.add(candidate)
                        queue.append(candidate)
            if found:
                break

        return result
