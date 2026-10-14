"""
Problem: Pascal's Triangle (LC #118)
Difficulty: Easy
Link: https://leetcode.com/problems/pascals-triangle/

Approach:
- Start with [[1]]
- Each row starts and ends with 1
- Middle elements = sum of two elements above
- Build row by row using previous row
- Time: O(n²) | Space: O(n²)

ML Connection:
- Pascal's triangle generates binomial coefficients
  used in polynomial feature expansion in ML
- The values appear in binomial distributions used
  in statistical hypothesis testing for ML models
"""

class Solution:
    def generate(self, numRows):
        result = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            result.append(row)
        return result
