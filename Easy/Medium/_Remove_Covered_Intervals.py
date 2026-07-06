"""
LC#1288 - Remove Covered Intervals [Medium]
Topic: Sorting + Greedy
ML Connection: Interval merging/filtering is used in NLP for 
named entity recognition — removing overlapping span predictions.
"""

class Solution(object):
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        max_right = 0

        for l, r in intervals:
            if r > max_right:
                count += 1
                max_right = r

        return count
