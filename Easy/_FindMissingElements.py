"""
LC#3731 - Find Missing Elements [Easy]
Topic: Hash Set
ML Connection: Finding gaps in a range is used in data validation 
pipelines — detecting missing time steps in time-series data before 
feeding into sequence models.
"""

class Solution:
    def findMissingElements(self, nums: list) -> list:
        num_set = set(nums)
        return [x for x in range(min(nums), max(nums) + 1) if x not in num_set]
