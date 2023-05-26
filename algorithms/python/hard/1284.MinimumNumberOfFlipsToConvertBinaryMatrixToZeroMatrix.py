#
# @lc app=leetcode id=1284 lang=python3
#
# [1284] Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
#
# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/description/
#
# algorithms
# Hard (72.00%)
# Likes:    867
# Dislikes: 85
# Total Accepted:    29.5K
# Total Submissions: 41K
# Testcase Example:  '[[0,0],[0,1]]'
#
# Given a m x n binary matrix mat. In one step, you can choose one cell and
# flip it and all the four neighbors of it if they exist (Flip is changing 1 to
# 0 and 0 to 1). A pair of cells are called neighbors if they share one edge.
#
# Return the minimum number of steps required to convert mat to a zero matrix
# or -1 if you cannot.
#
# A binary matrix is a matrix with all cells equal to 0 or 1 only.
#
# A zero matrix is a matrix with all cells equal to 0.
#
#
# Example 1:
#
#
# Input: mat = [[0,0],[0,1]]
# Output: 3
# Explanation: One possible solution is to flip (1, 0) then (0, 1) and finally
# (1, 1) as shown.
#
#
# Example 2:
#
#
# Input: mat = [[0]]
# Output: 0
# Explanation: Given matrix is a zero matrix. We do not need to change it.
#
#
# Example 3:
#
#
# Input: mat = [[1,0,0],[1,0,0]]
# Output: -1
# Explanation: Given matrix cannot be a zero matrix.
#
#
#
# Constraints:
#
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 3
# mat[i][j] is either 0 or 1.
#
#
#

# @lc code=start
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        """
        Solution 1: try all possible answers

        1. each tile should only be flipped at most once (flipping twice cancels
           both operations)
        2. the order of flipping doesn't matter

        # optimization: try small steps first

        # complexity:
        Time: O(2^(mn)*m*n)
        """
        # m, n = len(mat), len(mat[0])
        # idx2cord = lambda idx: (idx // n, idx % n)
        # cord2idx = lambda i, j: i * n + j

        # init_state = 0
        # for i in range(m):
        #     for j in range(n):
        #         if mat[i][j]:
        #             init_state |= 1 << cord2idx(i,j)

        # def flip_one_tile(state, i, j):
        #     for x, y in zip((i, i, i, i-1, i+1), (j, j-1, j+1, j, j)):
        #         if 0<=x<m and 0<=y<n:
        #             state ^= 1 << cord2idx(x, y)
        #     return state

        # def flip(state, i):
        #     idx = count = 0
        #     while (1 << idx) <= i:
        #         if i & (1 << idx):
        #             count += 1
        #             state = flip_one_tile(state, *idx2cord(idx))
        #         idx += 1
        #     return state, count

        # ans = m * n + 1
        # for i in range(2 ** (m*n)):
        #     state, count = flip(init_state, i)
        #     if not state:
        #         ans = min(ans, count)
        # return -1 if ans == m * n + 1 else ans

        """
        Solution 2: smart enumeration

        from solution 1, we need to one more obervation:

        3. since the order doesn't matter, we can decide to flip tiles or not row
           by row. when working on row i, all tiles from row 0 to row i-2
           (inclusive) should be all 0 (as we can only change row i-1 by flipping
           tiles in row i). Then what we really need to is thus flip all tiles in
           row i where mat[i-1][j] is still 1. This further means that we really
           only need to try out all different options for row 1 and the actions
           for remaining rows are already determined.

        This makes the complexity to O(m*n*2^n)

        # implemented in Java
        """



# @lc code=end
