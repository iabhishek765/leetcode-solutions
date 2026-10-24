"""
Problem: Count Days Spent Together (LC #2409)
Difficulty: Easy
Link: https://leetcode.com/problems/count-days-spent-together/

Approach:
- Convert MM-DD to day-of-year using cumulative month days
- Overlap start = max(arriveAlice, arriveBob)
- Overlap end   = min(leaveAlice, leaveBob)
- Answer = max(0, end - start + 1)
- Time: O(1) | Space: O(1)

ML Connection:
- Date range overlap is used in time-series ML for
  finding co-occurrence windows in event data
- Interval intersection logic appears in temporal
  feature engineering for forecasting models
"""

class Solution:
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def toDays(date):
            m, d = int(date[:2]), int(date[3:])
            return sum(days[:m-1]) + d

        start = max(toDays(arriveAlice), toDays(arriveBob))
        end   = min(toDays(leaveAlice),  toDays(leaveBob))
        return max(0, end - start + 1)
