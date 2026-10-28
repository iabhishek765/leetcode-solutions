"""
Problem: Max Points on a Line (LC #149)
Difficulty: Hard
Link: https://leetcode.com/problems/max-points-on-a-line/

Approach:
- For each anchor point, compute slope to all others
- Normalize slope as (dx/gcd, dy/gcd) to avoid float precision
- Normalize sign: dx always >= 0
- Max frequency of same slope + 1 = max collinear points
- Time: O(n²) | Space: O(n)

ML Connection:
- Collinearity detection is used in PCA and feature
  selection to remove redundant features in ML
- Slope normalization mirrors feature scaling used
  before training linear regression models
"""

from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n

        result = 2

        for i in range(n):
            slopes = defaultdict(int)
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                g = gcd(abs(dx), abs(dy))
                if g:
                    dx //= g
                    dy //= g
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = abs(dy)
                slopes[(dx, dy)] += 1
            if slopes:
                result = max(result, max(slopes.values()) + 1)

        return result
