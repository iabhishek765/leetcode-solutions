# LC#60 - Permutation Sequence
# Difficulty: Hard
# Topics: Math, Recursion
#
# Approach: Factorial number system — each position has (n-1)!
#           permutations. Divide k by factorial to find which
#           digit belongs at each position, remove used digits
# Time: O(n^2) | Space: O(n)
#
# ML Connection: Factorial number system is used in ranking
# and ordering algorithms — similar to how ranking losses
# (LambdaRank, ListNet) enumerate permutations of document
# relevance scores in learning-to-rank ML systems

class Solution:
    def getPermutation(self, n, k):
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i-1] * i
        
        digits = list(range(1, n + 1))
        k -= 1
        result = []
        
        for i in range(n, 0, -1):
            idx = k // factorial[i-1]
            result.append(str(digits[idx]))
            digits.pop(idx)
            k %= factorial[i-1]
        
        return ''.join(result)
