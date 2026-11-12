"""
Problem: Restore IP Addresses (LC #93)
Difficulty: Medium
Link: https://leetcode.com/problems/restore-ip-addresses/

Approach:
- Backtracking: choose a segment length of 1-3 digits, 4 times
- Valid segment: value <= 255 and no leading zero (except "0")
- Prune when remaining digits can't fill remaining segments
- Accept only when 4 segments use all digits
- Time: O(3^4) = constant for fixed 4 parts | Space: O(1) extra

ML Connection:
- Backtracking with pruning is the same search pattern used in
  hyperparameter search and constraint-based decoding.
"""

class Solution:
    def restoreIpAddresses(self, s):
        res = []

        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    res.append('.'.join(parts))
                return
            remaining = len(s) - start
            parts_left = 4 - len(parts)
            if remaining < parts_left or remaining > parts_left * 3:
                return
            for length in range(1, 4):
                if start + length > len(s):
                    break
                seg = s[start:start + length]
                if (len(seg) > 1 and seg[0] == '0') or int(seg) > 255:
                    continue
                backtrack(start + length, parts + [seg])

        backtrack(0, [])
        return res
