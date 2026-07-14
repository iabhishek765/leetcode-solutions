# LC#56 - Merge Intervals
# Difficulty: Medium
# Topics: Array, Sorting, Greedy
#
# Approach: Sort by start time, then greedily merge overlapping
#           intervals by extending end time when overlap detected
# Time: O(n log n) | Space: O(n)
#
# ML Connection: Interval merging is used in NLP for merging
# overlapping named entity spans, and in time-series ML for
# consolidating overlapping event windows before feature extraction

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        
        for start, end in intervals[1:]:
            if start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])
        
        return result
