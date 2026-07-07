"""
LC#49 - Group Anagrams [Medium]
Topic: Hash Map / String
ML Connection: Grouping by canonical form (sorted chars) is the same 
idea as feature hashing in ML — mapping different inputs to the same 
bucket based on their signature.
"""

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
        return list(groups.values())
