# LC#66 - Plus One
# Difficulty: Easy
# Topics: Array, Math
#
# Approach: Scan from right - if digit < 9 increment and return.
#           If 9, set to 0 and carry. If all 9s, prepend 1.
# Time: O(n) | Space: O(1)
#
# ML Connection: Arbitrary precision arithmetic on digit arrays
# is used in numerical computing libraries (mpmath) for
# high-precision ML calculations like log-likelihood in
# statistical models

class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
