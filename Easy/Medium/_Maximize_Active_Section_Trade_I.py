# LC#3499 - Maximize Active Section with Trade I
# Difficulty: Medium
# Topics: String, Greedy, Run-Length Encoding
#
# Approach: Augment with '1' on both ends, build run-length
#           encoding. Find pattern (0-block, 1-bridge, 0-block)
#           Best gain = max(left_zeros + right_zeros - ones_bridge)
#           Add gain to base count of 1s
# Time: O(n) | Space: O(n)
#
# ML Connection: Run-length encoding is used in compressing
# sparse feature vectors in ML pipelines and in image
# segmentation where consecutive pixel labels are grouped


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count("1")

        t = "1" + s + "1"

        runs = []

        for ch in t:
            if not runs or runs[-1][0] != ch:
                runs.append([ch, 1])
            else:
                runs[-1][1] += 1

        best = 0

        for i in range(1, len(runs) - 1):
            if (
                runs[i][0] == "1"
                and runs[i - 1][0] == "0"
                and runs[i + 1][0] == "0"
            ):
                best = max(best, runs[i - 1][1] + runs[i + 1][1])

        return ones + best
