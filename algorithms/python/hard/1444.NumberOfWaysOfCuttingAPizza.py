#
# @lc app=leetcode id=1444 lang=python3
#
# [1444] Number of Ways of Cutting a Pizza
#
# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/description/
#
# algorithms
# Hard (57.92%)
# Likes:    1631
# Dislikes: 90
# Total Accepted:    61.6K
# Total Submissions: 96.7K
# Testcase Example:  '["A..","AAA","..."]\n3'
#
# Given a rectangular pizza represented as a rows x cols matrix containing the
# following characters: 'A' (an apple) and '.' (empty cell) and given the
# integer k. You have to cut the pizza into k pieces using k-1 cuts.
#
# For each cut you choose the direction: vertical or horizontal, then you
# choose a cut position at the cell boundary and cut the pizza into two pieces.
# If you cut the pizza vertically, give the left part of the pizza to a person.
# If you cut the pizza horizontally, give the upper part of the pizza to a
# person. Give the last piece of pizza to the last person.
#
# Return the number of ways of cutting the pizza such that each piece contains
# at least one apple. Since the answer can be a huge number, return this modulo
# 10^9 + 7.
#
#
# Example 1:
#
#
#
#
# Input: pizza = ["A..","AAA","..."], k = 3
# Output: 3
# Explanation: The figure above shows the three ways to cut the pizza. Note
# that pieces must contain at least one apple.
#
#
# Example 2:
#
#
# Input: pizza = ["A..","AA.","..."], k = 3
# Output: 1
#
#
# Example 3:
#
#
# Input: pizza = ["A..","A..","..."], k = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= rows, cols <= 50
# rows == pizza.length
# cols == pizza[i].length
# 1 <= k <= 10
# pizza consists of characters 'A' and '.' only.
#
#
#


# @lc code=start
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        """
        Solution 1: DP + DP

        first use DP to calculate # apples for pizza with i, j as top left corner
        dp1[i][j] = (
            int(pizza[i][j] == 'A')
            + dp1[i+1][j]
            + dp1[i][j+1]
            - dp1[i+1][j+1]
        )

        second use DP to calculate # ways to cut for pizza with i, j as top left
        corner and k cuts
        dp2[i][j][k] = (
            sum(
                dp2[ii][j][k-1] if dp1[i][j] - dp1[ii][j] > 0 else 0
                for ii in range(i+1, m)
            )
            + sum(
                dp2[i][jj][k-1] if dp1[i][j] - dp1[i][jj] > 0 else 0
                for jj in range(j+1, n)
            )
        )
        dp2[i][j][0] = 1 if dp1[i][j] > 0 else 0

        finalAns = dp2[0][0][k-1]
        """
        m, n = len(pizza), len(pizza[0])
        dp1 = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp1[i][j] = (
                    int(pizza[i][j] == "A")
                    + dp1[i + 1][j]
                    + dp1[i][j + 1]
                    - dp1[i + 1][j + 1]
                )

        dp2_prev = [[int(dp1[i][j] > 0) for j in range(n)] for i in range(m)]
        for _ in range(k - 1):
            dp2_cur = [[0] * n for _ in range(m)]
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    dp2_cur[i][j] = sum(
                        dp2_prev[ii][j] if dp1[i][j] > dp1[ii][j] else 0
                        for ii in range(i + 1, m)
                    ) + sum(
                        dp2_prev[i][jj] if dp1[i][j] > dp1[i][jj] else 0
                        for jj in range(j + 1, n)
                    )
            dp2_prev = dp2_cur
        return dp2_prev[0][0] % 1000000007


# @lc code=end
