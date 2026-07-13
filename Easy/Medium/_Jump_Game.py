# LC#55 - Jump Game
# Difficulty: Medium
# Topics: Array, Greedy
#
# Approach: Greedy - track max reachable index.
#           If current index > max_reach, we're stuck → False
#           Otherwise update max_reach and continue
# Time: O(n) | Space: O(1)
#
# ML Connection: Greedy reachability is similar to how
# beam search in sequence models decides which paths to
# keep exploring vs prune based on current best score

class Solution:
    def canJump(self, nums):
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True
