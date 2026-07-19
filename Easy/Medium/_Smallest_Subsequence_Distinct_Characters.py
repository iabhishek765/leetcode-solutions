# LC#1081 - Smallest Subsequence of Distinct Characters
# Difficulty: Medium
# Topics: String, Stack, Greedy, Monotonic Stack
#
# Approach: Monotonic stack - track last occurrence of each char.
#           For each char, pop stack if current < top AND top
#           appears later (safe to remove). Skip if already in stack.
# Time: O(n) | Space: O(1) - max 26 chars in stack
#
# ML Connection: Greedy sequence compression mirrors beam search
# pruning in seq2seq models where suboptimal tokens are dropped
# if better candidates appear later in the decoding step

class Solution:
    def smallestSubsequence(self, s):
        last = {c: i for i, c in enumerate(s)}
        stack = []
        in_stack = set()
        
        for i, c in enumerate(s):
            if c in in_stack:
                continue
            while stack and c < stack[-1] and last[stack[-1]] > i:
                in_stack.remove(stack.pop())
            stack.append(c)
            in_stack.add(c)
        
        return ''.join(stack)
