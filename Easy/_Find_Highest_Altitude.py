# LC#1732 - Find the Highest Altitude
# Difficulty: Easy
# Topics: Array, Prefix Sum
#
# Approach: Running prefix sum - track cumulative altitude
#           starting from 0, keep max value seen
# Time: O(n) | Space: O(1)
#
# ML Connection: Prefix sum / cumulative tracking is similar to
# tracking running loss or running mean during training loops
# (e.g. exponential moving average of metrics)

class Solution(object):
    def largestAltitude(self, gain):
        altitude = 0
        max_altitude = 0
        for g in gain:
            altitude += g
            max_altitude = max(max_altitude, altitude)
        return max_altitude
