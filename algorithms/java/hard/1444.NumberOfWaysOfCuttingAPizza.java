/*
 * @lc app=leetcode id=1444 lang=java
 *
 * [1444] Number of Ways of Cutting a Pizza
 *
 * https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/description/
 *
 * algorithms
 * Hard (57.92%)
 * Likes:    1631
 * Dislikes: 90
 * Total Accepted:    61.6K
 * Total Submissions: 96.7K
 * Testcase Example:  '["A..","AAA","..."]\n3'
 *
 * Given a rectangular pizza represented as a rows x cols matrix containing the
 * following characters: 'A' (an apple) and '.' (empty cell) and given the
 * integer k. You have to cut the pizza into k pieces using k-1 cuts. 
 *
 * For each cut you choose the direction: vertical or horizontal, then you
 * choose a cut position at the cell boundary and cut the pizza into two
 * pieces. If you cut the pizza vertically, give the left part of the pizza to
 * a person. If you cut the pizza horizontally, give the upper part of the
 * pizza to a person. Give the last piece of pizza to the last person.
 *
 * Return the number of ways of cutting the pizza such that each piece contains
 * at least one apple. Since the answer can be a huge number, return this
 * modulo 10^9 + 7.
 *
 *
 * Example 1:
 *
 *
 *
 *
 * Input: pizza = ["A..","AAA","..."], k = 3
 * Output: 3
 * Explanation: The figure above shows the three ways to cut the pizza. Note
 * that pieces must contain at least one apple.
 *
 *
 * Example 2:
 *
 *
 * Input: pizza = ["A..","AA.","..."], k = 3
 * Output: 1
 *
 *
 * Example 3:
 *
 *
 * Input: pizza = ["A..","A..","..."], k = 1
 * Output: 1
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= rows, cols <= 50
 * rows == pizza.length
 * cols == pizza[i].length
 * 1 <= k <= 10
 * pizza consists of characters 'A' and '.' only.
 *
 *
 */

// @lc code=start
class Solution {
    public int ways(String[] pizza, int k) {
        // Double DP
        int m = pizza.length, n = pizza[0].length(), MOD = 1000000007;
        int[][] count = new int[m + 1][n + 1];
        int[][] f = new int[m][n];
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                count[i][j] = (pizza[i].charAt(j) == 'A' ? 1 : 0) + count[i][j + 1] + count[i + 1][j]
                        - count[i + 1][j + 1];
                f[i][j] = count[i][j] > 0 ? 1 : 0;
            }
        }

        for (int remain = 1; remain < k; remain++) {
            int[][] g = new int[m][n];
            for (int i = m - 1; i >= 0; i--) {
                for (int j = n - 1; j >= 0; j--) {
                    for (int ii = i + 1; ii < m; ii++) {
                        if (count[i][j] > count[ii][j]) {
                            g[i][j] += f[ii][j];
                            g[i][j] %= MOD;
                        }
                    }
                    for (int jj = j + 1; jj < n; jj++) {
                        if (count[i][j] > count[i][jj]) {
                            g[i][j] += f[i][jj];
                            g[i][j] %= MOD;
                        }
                    }
                }
            }
            f = g;
        }
        return f[0][0];
    }
}
// @lc code=end
