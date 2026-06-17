# LC#3614 - Process String with Special Operations II
# Difficulty: Hard
# Topics: String, Simulation, Binary Search / Reverse Simulation
#
# Approach: Don't build the actual string (can explode exponentially
#           due to '#'). Track only length at each step, then walk
#           backwards from index k, undoing each operation to find
#           the original source character.
# Time: O(n) | Space: O(n)
#
# ML Connection: This "track size, simulate backwards" trick is
# similar to how backpropagation recomputes gradients by walking
# the computation graph in reverse instead of storing every
# intermediate full tensor in memory.

class Solution(object):
    def processStr(self, s, k):
        length = 0
        lengths = []
        for ch in s:
            if ch == '*':
                length = max(0, length - 1)
            elif ch == '#':
                length *= 2
            elif ch == '%':
                pass
            else:
                length += 1
            lengths.append(length)
        
        if k >= length:
            return '.'
        
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            curr_len = lengths[i]
            
            if ch == '*':
                continue
            elif ch == '#':
                half = curr_len // 2
                if k >= half:
                    k -= half
            elif ch == '%':
                k = curr_len - 1 - k
            else:
                if k == curr_len - 1:
                    return ch
        
        return '.'
