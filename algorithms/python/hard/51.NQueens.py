#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (63.14%)
# Likes:    10094
# Dislikes: 224
# Total Accepted:    545.5K
# Total Submissions: 844.6K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle. You
# may return the answer in any order.
#
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space,
# respectively.
#
#
# Example 1:
#
#
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [["Q"]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 9
#
#
#


# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Solution 1: backtrack

        Note: queen can move horizontally, vertically, and diagonally

        thus, we need to make sure, no two queens are placed at two places
        x1, y1 and x2, y2 such that
          x1 == x2 or y1 == y2 or x1-y1 == x2-y2 or x1+y1 == x2+y2

        fill row by row, and track filled for y, x-y, and x+y
        """
        y = [False] * n
        x_plus_y = [False] * (2 * n - 1)
        # x - y + n - 1 to ensure non-negativity
        x_minus_y = [False] * (2 * n - 1)
        ans = []
        candidate = [["."] * n for _ in range(n)]

        def fill(i, j):
            candidate[i][j] = "Q"
            y[j] = True
            x_minus_y[i - j + n - 1] = True
            x_plus_y[i + j] = True

        def unfill(i, j):
            candidate[i][j] = "."
            y[j] = False
            x_minus_y[i - j + n - 1] = False
            x_plus_y[i + j] = False

        def backtrack(i):
            if i == n:
                ans.append(["".join(row) for row in candidate])
            else:
                for j in range(n):
                    if not (y[j] or x_plus_y[i + j] or x_minus_y[i - j + n - 1]):
                        fill(i, j)
                        backtrack(i + 1)
                        unfill(i, j)

        backtrack(0)
        return ans


# @lc code=end
