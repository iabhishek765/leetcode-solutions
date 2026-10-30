# Problem: Tenth Line (LC #195)
# Difficulty: Easy
# Link: https://leetcode.com/problems/tenth-line/
#
# Approach:
# sed -n '10p' prints only line 10 and suppresses all other output.
# If the file has fewer than 10 lines, nothing is printed.
# Alternatives: awk 'NR == 10' or tail -n +10 | head -n 1
# Time: O(n) | Space: O(1)
#
# ML Connection:
# Command-line text processing (sed/awk) is used daily in
# data cleaning and dataset inspection before ML training.

sed -n '10p' file.txt
