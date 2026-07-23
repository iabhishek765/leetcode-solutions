# LC#65 - Valid Number
# Difficulty: Hard
# Topics: String, Finite Automaton
#
# Approach: Flag-based scan - track seen_digit, seen_dot,
#           seen_exp. Validate each char based on context.
#           Reset seen_digit after 'e' to ensure digits follow.
# Time: O(n) | Space: O(1)
#
# ML Connection: This flag-based state tracking is essentially
# a Finite State Automaton (FSA) — the same concept used in
# tokenizers and lexers for parsing ML config files and
# model definition languages like ONNX and TFLite schemas

class Solution:
    def isNumber(self, s):
        seen_digit = False
        seen_dot = False
        seen_exp = False
        
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in '+-':
                if i > 0 and s[i-1] not in 'eE':
                    return False
            elif c == '.':
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            elif c in 'eE':
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False
            else:
                return False
        
        return seen_digit
