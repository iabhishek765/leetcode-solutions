# LC#57 - Insert Interval
# Difficulty: Medium
# Topics: Array, Greedy
#
# Approach: 3-phase linear scan - skip non-overlapping left,
#           merge all overlapping by expanding newInterval,
#           append remaining non-overlapping right
# Time: O(n) | Space: O(n)
#
# ML Connection: Interval insertion/merging mirrors how
# attention span windows are dynamically updated in
# streaming transformer inference pipelines

class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        while i < n:
            result.append(intervals[i])
            i += 1

        return result
