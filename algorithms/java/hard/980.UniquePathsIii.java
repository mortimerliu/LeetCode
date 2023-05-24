/*
 * @lc app=leetcode id=980 lang=java
 *
 * [980] Unique Paths III
 *
 * https://leetcode.com/problems/unique-paths-iii/description/
 *
 * algorithms
 * Hard (79.68%)
 * Likes:    4589
 * Dislikes: 173
 * Total Accepted:    175.5K
 * Total Submissions: 214.9K
 * Testcase Example:  '[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]'
 *
 * You are given an m x n integer array grid where grid[i][j] could be:
 *
 *
 * 1 representing the starting square. There is exactly one starting
 * square.
 * 2 representing the ending square. There is exactly one ending square.
 * 0 representing empty squares we can walk over.
 * -1 representing obstacles that we cannot walk over.
 *
 *
 * Return the number of 4-directional walks from the starting square to the
 * ending square, that walk over every non-obstacle square exactly once.
 *
 *
 * Example 1:
 *
 *
 * Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
 * Output: 2
 * Explanation: We have the following two paths:
 * 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
 * 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
 *
 *
 * Example 2:
 *
 *
 * Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
 * Output: 4
 * Explanation: We have the following four paths:
 * 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
 * 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
 * 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
 * 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
 *
 *
 * Example 3:
 *
 *
 * Input: grid = [[0,1],[2,0]]
 * Output: 0
 * Explanation: There is no path that walks over every empty square exactly
 * once.
 * Note that the starting and ending square can be anywhere in the grid.
 *
 *
 *
 * Constraints:
 *
 *
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 20
 * 1 <= m * n <= 20
 * -1 <= grid[i][j] <= 2
 * There is exactly one starting cell and one ending cell.
 *
 *
 */

// @lc code=start
class Solution {
    int count;
    int num_empty = 1;
    int[][] grid;
    int nrow;
    int ncol;

    public int uniquePathsIII(int[][] grid) {
        // backtrack
        int start_row = 0, start_col = 0;
        this.grid = grid;
        this.nrow = grid.length;
        this.ncol = grid[0].length;
        for (int i = 0; i < nrow; i++) {
            for (int j = 0; j < ncol; j++) {
                if (grid[i][j] == 0) {
                    num_empty++;
                } else if (grid[i][j] == 1) {
                    start_row = i;
                    start_col = j;
                }
            }
        }
        backtrack(start_row, start_col, 0);
        return count;
    }

    void backtrack(int i, int j, int d) {
        if (grid[i][j] == 2 && d == num_empty) {
            count++;
        } else {
            int tmp = grid[i][j];
            grid[i][j] = -2;
            int[] rows = { i, i, i - 1, i + 1 };
            int[] cols = { j - 1, j + 1, j, j };
            for (int k = 0; k < 4; k++) {
                int ni = rows[k];
                int nj = cols[k];
                if (ni >= 0 && ni < nrow && nj >= 0 && nj < ncol && grid[ni][nj] >= 0) {
                    backtrack(ni, nj, d + 1);
                }
            }
            grid[i][j] = tmp;
        }
    }
}
// @lc code=end
