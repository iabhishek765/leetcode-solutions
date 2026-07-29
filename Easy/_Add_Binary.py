# LC#67 - Add Binary
# Difficulty: Easy
# Topics: Math, String, Bit Manipulation, Simulation
#
# Approach: Two pointers from right, add digits + carry.
#           total%2 = current bit, total//2 = next carry.
#           Reverse result at end.
# Time: O(max(m,n)) | Space: O(max(m,n))
#
# ML Connection: Binary addition with carry is the fundamental
# operation in hardware accelerators (TPUs/GPUs) for computing
# floating point additions in neural network forward passes

class Solution:
    def addBinary(self, a, b):
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        
        return ''.join(reversed(result))
