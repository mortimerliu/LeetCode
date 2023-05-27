/*
 * @lc app=leetcode id=51 lang=java
 *
 * [51] N-Queens
 *
 * https://leetcode.com/problems/n-queens/description/
 *
 * algorithms
 * Hard (63.14%)
 * Likes:    10094
 * Dislikes: 224
 * Total Accepted:    545.5K
 * Total Submissions: 844.6K
 * Testcase Example:  '4'
 *
 * The n-queens puzzle is the problem of placing n queens on an n x n
 * chessboard such that no two queens attack each other.
 *
 * Given an integer n, return all distinct solutions to the n-queens puzzle.
 * You may return the answer in any order.
 *
 * Each solution contains a distinct board configuration of the n-queens'
 * placement, where 'Q' and '.' both indicate a queen and an empty space,
 * respectively.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 4
 * Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
 * Explanation: There exist two distinct solutions to the 4-queens puzzle as
 * shown above
 *
 *
 * Example 2:
 *
 *
 * Input: n = 1
 * Output: [["Q"]]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 9
 *
 *
 */

// @lc code=start
import java.util.*;

class Solution {
    int n;
    List<List<String>> ans;
    char[][] candidate;
    boolean[] y;
    boolean[] xPlusY;
    boolean[] xMinusY;

    public List<List<String>> solveNQueens(int n) {
        // backtrack
        this.n = n;
        ans = new ArrayList<>();
        initCandidate();
        y = new boolean[n];
        xPlusY = new boolean[2 * n - 1];
        xMinusY = new boolean[2 * n - 1];
        backtrack(0);
        return ans;
    }

    void fill(int i, int j) {
        candidate[i][j] = 'Q';
        y[j] = true;
        xPlusY[i + j] = true;
        xMinusY[i - j + n - 1] = true;
    }

    void unfill(int i, int j) {
        candidate[i][j] = '.';
        y[j] = false;
        xPlusY[i + j] = false;
        xMinusY[i - j + n - 1] = false;
    }

    void backtrack(int i) {
        if (i == n) {
            ans.add(createBoard());
        } else {
            for (int j = 0; j < n; j++) {
                if (!(y[j] || xPlusY[i + j] || xMinusY[i - j + n - 1])) {
                    fill(i, j);
                    backtrack(i + 1);
                    unfill(i, j);
                }
            }
        }
    }

    List<String> createBoard() {
        List<String> board = new ArrayList<>();
        for (char[] row : candidate) {
            String rowString = new String(row);
            board.add(rowString);
        }
        return board;
    }

    void initCandidate() {
        candidate = new char[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                candidate[i][j] = '.';
            }
        }
    }
}
// @lc code=end
