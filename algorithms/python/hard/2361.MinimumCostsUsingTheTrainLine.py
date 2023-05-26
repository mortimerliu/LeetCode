#
# @lc app=leetcode id=2361 lang=python3
#
# [2361] Minimum Costs Using the Train Line
#
# https://leetcode.com/problems/minimum-costs-using-the-train-line/description/
#
# algorithms
# Hard (77.19%)
# Likes:    83
# Dislikes: 18
# Total Accepted:    4.6K
# Total Submissions: 6K
# Testcase Example:  '[1,6,9,5]\n[5,2,3,10]\n8'
#
# A train line going through a city has two routes, the regular route and the
# express route. Both routes go through the same n + 1 stops labeled from 0 to
# n. Initially, you start on the regular route at stop 0.
#
# You are given two 1-indexed integer arrays regular and express, both of
# length n. regular[i] describes the cost it takes to go from stop i - 1 to
# stop i using the regular route, and express[i] describes the cost it takes to
# go from stop i - 1 to stop i using the express route.
#
# You are also given an integer expressCost which represents the cost to
# transfer from the regular route to the express route.
#
# Note that:
#
#
# There is no cost to transfer from the express route back to the regular
# route.
# You pay expressCost every time you transfer from the regular route to the
# express route.
# There is no extra cost to stay on the express route.
#
#
# Return a 1-indexed array costs of length n, where costs[i] is the minimum
# cost to reach stop i from stop 0.
#
# Note that a stop can be counted as reached from either route.
#
#
# Example 1:
#
#
# Input: regular = [1,6,9,5], express = [5,2,3,10], expressCost = 8
# Output: [1,7,14,19]
# Explanation: The diagram above shows how to reach stop 4 from stop 0 with
# minimum cost.
# - Take the regular route from stop 0 to stop 1, costing 1.
# - Take the express route from stop 1 to stop 2, costing 8 + 2 = 10.
# - Take the express route from stop 2 to stop 3, costing 3.
# - Take the regular route from stop 3 to stop 4, costing 5.
# The total cost is 1 + 10 + 3 + 5 = 19.
# Note that a different route could be taken to reach the other stops with
# minimum cost.
#
#
# Example 2:
#
#
# Input: regular = [11,5,13], express = [7,10,6], expressCost = 3
# Output: [10,15,24]
# Explanation: The diagram above shows how to reach stop 3 from stop 0 with
# minimum cost.
# - Take the express route from stop 0 to stop 1, costing 3 + 7 = 10.
# - Take the regular route from stop 1 to stop 2, costing 5.
# - Take the express route from stop 2 to stop 3, costing 3 + 6 = 9.
# The total cost is 10 + 5 + 9 = 24.
# Note that the expressCost is paid again to transfer back to the express
# route.
#
#
#
# Constraints:
#
#
# n == regular.length == express.length
# 1 <= n <= 10^5
# 1 <= regular[i], express[i], expressCost <= 10^5
#
#
#


# @lc code=start
class Solution:
    def minimumCosts(
        self, regular: List[int], express: List[int], expressCost: int
    ) -> List[int]:
        """
        Solution 1: DP

        dp[i]: min cost to reach i
        dp_reg[i]: min cost to reach i with reg as last route
        dp_exp[i]: min cost to reach i with exp as last route

        dp_reg[i] = min(dp_reg[i-1], dp_exp[i-1]) + regular[i]
        dp_exp[i] = min(dp_reg[i-1] + expressCost, dp_exp[i-1]) + express[i]
        dp[i] = min(dp_reg[i], dp_exp[i])

        dp_reg[0] = 0, dp_exp[0] = expressCost

        Space can be optimized to O(1) easily (doesn't count for the space for answer)

        Time O(n)
        """
        n = len(regular)
        dp_reg = [0] * (n + 1)
        dp_exp = [expressCost] * (n + 1)
        dp = [0] * n
        for i in range(1, n + 1):
            dp_reg[i] = min(dp_reg[i - 1], dp_exp[i - 1]) + regular[i - 1]
            dp_exp[i] = min(dp_reg[i - 1] + expressCost, dp_exp[i - 1]) + express[i - 1]
            dp[i - 1] = min(dp_reg[i], dp_exp[i])
        return dp


# @lc code=end
