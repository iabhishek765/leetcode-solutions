# LC#1833 - Maximum Ice Cream Bars
# Difficulty: Medium
# Topics: Array, Greedy, Sorting, Counting Sort
#
# Approach: Greedy - buy cheapest bars first to maximize count.
#           Use counting sort (bucket by price) since costs are
#           bounded, avoiding O(n log n) comparison sort
# Time: O(n + maxCost) | Space: O(maxCost)
#
# ML Connection: Counting sort / bucketing by value is the core
# idea behind histogram-based feature binning used in gradient
# boosting algorithms like LightGBM/XGBoost for faster splits

class Solution(object):
    def maxIceCream(self, costs, coins):
        max_cost = max(costs)
        count = [0] * (max_cost + 1)
        
        for c in costs:
            count[c] += 1
        
        bars = 0
        for price in range(1, max_cost + 1):
            if count[price] == 0:
                continue
            num_can_buy = min(count[price], coins // price)
            bars += num_can_buy
            coins -= num_can_buy * price
            if coins == 0:
                break
        
        return bars
