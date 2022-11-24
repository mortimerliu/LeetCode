#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (39.76%)
# Likes:    11589
# Dislikes: 465
# Total Accepted:    1.1M
# Total Submissions: 2.9M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
#
#
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
#
#
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
#
#
#
# Constraints:
#
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
#
#
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
#
#

# @lc code=start
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Backtesting

        Time: O(N * L^3) - TLE
        Space: O(N^2 + L); can be reduced to O(L) if we modify the board directly
        """
        m, n, k = len(board), len(board[0]), len(word)
        visited = [[False] * n for _ in range(m)]

        def search(x: int, y: int, i: int) -> bool:
            if i == k:
                return True

            # add a virtual node (-1, -1) that connects to all nodes
            if (x, y) == (-1, -1):
                next_points = [(u, v) for u in range(m) for v in range(n)]
            else:
                next_points = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

            for nx, ny in next_points:
                if (
                    0 <= nx < m
                    and 0 <= ny < n
                    and word[i] == board[nx][ny]
                    and not visited[nx][ny]
                ):
                    visited[nx][ny] = True
                    if search(nx, ny, i + 1):
                        return True
                    visited[nx][ny] = False

            return False

        return search(-1, -1, 0)


# @lc code=end

# @lc code=start
class Solution2:
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        if len(word) == 0:  # all the characters are checked
            return True
        if (
            i < 0
            or i >= len(board)
            or j < 0
            or j >= len(board[0])
            or word[0] != board[i][j]
        ):
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian
        # check whether can find "word" along one direction
        res = (
            self.dfs(board, i + 1, j, word[1:])
            or self.dfs(board, i - 1, j, word[1:])
            or self.dfs(board, i, j + 1, word[1:])
            or self.dfs(board, i, j - 1, word[1:])
        )
        board[i][j] = tmp
        return res


# @lc code=end
