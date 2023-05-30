#
# @lc app=leetcode id=2218 lang=python3
#
# [2218] Maximum Value of K Coins From Piles
#
# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/description/
#
# algorithms
# Hard (48.03%)
# Likes:    2044
# Dislikes: 35
# Total Accepted:    56.7K
# Total Submissions: 92.1K
# Testcase Example:  '[[1,100,3],[7,8,9]]\n2'
#
# There are n piles of coins on a table. Each pile consists of a positive
# number of coins of assorted denominations.
#
# In one move, you can choose any coin on top of any pile, remove it, and add
# it to your wallet.
#
# Given a list piles, where piles[i] is a list of integers denoting the
# composition of the i^th pile from top to bottom, and a positive integer k,
# return the maximum total value of coins you can have in your wallet if you
# choose exactly k coins optimally.
#
#
# Example 1:
#
#
# Input: piles = [[1,100,3],[7,8,9]], k = 2
# Output: 101
# Explanation:
# The above diagram shows the different ways we can choose k coins.
# The maximum total we can obtain is 101.
#
#
# Example 2:
#
#
# Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
# Output: 706
# Explanation:
# The maximum total can be obtained if we choose all coins from the last
# pile.
#
#
#
# Constraints:
#
#
# n == piles.length
# 1 <= n <= 1000
# 1 <= piles[i][j] <= 10^5
# 1 <= k <= sum(piles[i].length) <= 2000
#
#
#


# @lc code=start
import functools


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        """
        Solution 1: DP

        dp(i_0, ..., i_{n-1}, k) = max(
            dp(i_0, ..., i_{j-1}, ..., i_{n-1}, k+1) + V(i_{j}, k-1)
            for j in range(n)
        )

        O(n * m * k)
        """

        # @functools.lru_cache(maxsize=None)
        # def dp(state, count):
        #     if count == k:
        #         return 0
        #     res = 0
        #     for i in range(len(piles)):
        #         j = (state // (10 ** (4 * i))) % (10**4)
        #         if j < len(piles[i]):
        #             res = max(res, piles[i][j] + dp(state + 10 ** (4 * i), count + 1))
        #     return res

        # return dp(0, 0)

        """
        Solution 2: DP - variants of 0/1 knapsack problem

        instead of just 0/1 two options, we have len(piles[i])+1 options
        weight of each coin is 1, profit is the value of the coin
        max weight is k

        dp[i][k]: optimal value by choosing k coins from piles[:i]

        dp[i][k] = max(dp[i-1][k-j] + sum(piles[i][:j]) for j in range(k+1))

        TC O(sum(piles[i].length) * k)
        """
        n = len(piles)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n):
            cur_pile = 0
            for j in range(min(len(piles[i]), k) + 1):  # pick j from piles[i]
                for l in range(j, k + 1):  # total l from piles[:i+1]
                    dp[i + 1][l] = max(dp[i + 1][l], cur_pile + dp[i][l - j])
                if j < len(piles[i]):
                    cur_pile += piles[i][j]
        return dp[n][k]


# @lc code=end
