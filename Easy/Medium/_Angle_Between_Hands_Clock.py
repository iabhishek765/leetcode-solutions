# LC#1344 - Angle Between Hands of a Clock
# Difficulty: Medium
# Topics: Math
#
# Approach: Calculate each hand's angle from 12 o'clock position
#           Minute hand: 6 deg/min. Hour hand: 30 deg/hr + 0.5 deg/min
#           (hour hand moves as minutes pass too)
# Time: O(1) | Space: O(1)
#
# ML Connection: Angular/circular math like this appears in
# positional encoding for transformers, where angles represent
# relative positions using sine/cosine functions

class Solution(object):
    def angleClock(self, hour, minutes):
        minute_angle = minutes * 6
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360 - diff)
