# LC#3612 - Process String with Special Operations I
# Difficulty: Medium
# Topics: String, Stack, Simulation
#
# Approach: Simulate left to right using list as stack
#           Handle *(pop), #(duplicate), %(reverse), letter(append)
# Time: O(n^2) worst case | Space: O(n)
#
# ML Connection: Similar to tokenizer post-processing pipelines
# where special tokens trigger operations like padding,
# truncation, or reversal on token sequences

class Solution(object):
    def processStr(self, s):
        result = []
        for ch in s:
            if ch == '*':
                if result:
                    result.pop()
            elif ch == '#':
                result = result + result
            elif ch == '%':
                result.reverse()
            else:
                result.append(ch)
        return ''.join(result)
