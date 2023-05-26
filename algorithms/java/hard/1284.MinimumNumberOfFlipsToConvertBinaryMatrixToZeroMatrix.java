/*
 * @lc app=leetcode id=1284 lang=java
 *
 * [1284] Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
 *
 * https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/description/
 *
 * algorithms
 * Hard (72.00%)
 * Likes:    867
 * Dislikes: 85
 * Total Accepted:    29.5K
 * Total Submissions: 41K
 * Testcase Example:  '[[0,0],[0,1]]'
 *
 * Given a m x n binary matrix mat. In one step, you can choose one cell and
 * flip it and all the four neighbors of it if they exist (Flip is changing 1
 * to 0 and 0 to 1). A pair of cells are called neighbors if they share one
 * edge.
 *
 * Return the minimum number of steps required to convert mat to a zero matrix
 * or -1 if you cannot.
 *
 * A binary matrix is a matrix with all cells equal to 0 or 1 only.
 *
 * A zero matrix is a matrix with all cells equal to 0.
 *
 *
 * Example 1:
 *
 *
 * Input: mat = [[0,0],[0,1]]
 * Output: 3
 * Explanation: One possible solution is to flip (1, 0) then (0, 1) and finally
 * (1, 1) as shown.
 *
 *
 * Example 2:
 *
 *
 * Input: mat = [[0]]
 * Output: 0
 * Explanation: Given matrix is a zero matrix. We do not need to change it.
 *
 *
 * Example 3:
 *
 *
 * Input: mat = [[1,0,0],[1,0,0]]
 * Output: -1
 * Explanation: Given matrix cannot be a zero matrix.
 *
 *
 *
 * Constraints:
 *
 *
 * m == mat.length
 * n == mat[i].length
 * 1 <= m, n <= 3
 * mat[i][j] is either 0 or 1.
 *
 *
 */

// @lc code=start
import java.util.*;

class Solution {
    public int minFlips(int[][] mat) {
        // smart enumeration
        return backtrack(mat, new ArrayList<>());
    }

    private int backtrack(int[][] mat, ArrayList<Integer> operations) {
        if (operations.size() == mat[0].length) {
            return flip(mat, operations);
        } else {
            // option 1: not flip
            operations.add(0);
            int numFlips1 = backtrack(mat, operations);
            // option 2: flip
            operations.set(operations.size() - 1, 1);
            int numFlips2 = backtrack(mat, operations);
            operations.remove(operations.size() - 1);
            return better(numFlips1, numFlips2);
        }

    }

    private int better(int x, int y) {
        return x < 0 || (y >= 0 && y < x) ? y : x;
    }

    private int flip(int[][] mat, ArrayList<Integer> operations) {
        // whether the tile is flipped by operations from previous row
        int[] isChanged = new int[mat[0].length];
        // whether to flip a tile
        // for row 0: it is defined by operations
        // for row 1 to n-1: we must flip tile mat[i][j] if mat[i-1][j] == 1
        // so lastRow = curRow from previous row
        int[] lastRow = operations.stream().mapToInt(Integer::intValue).toArray();
        int numFlips = 0;
        for (int[] row : mat) {
            // store the state for current row
            int[] curRow = isChanged;
            for (int j = 0; j < row.length; ++j) {
                // flip the row if it is flipped by operatons from previous row
                curRow[j] ^= row[j];
                // if mat[i-1][j] == 1
                if (lastRow[j] == 1) {
                    flipOneTile(curRow, j);
                    ++numFlips;
                }
            }
            // for tile at col j in row i+1, a tile wil be flipped if the tile
            // at col j in row i-1 is 1 when flipping row i
            isChanged = lastRow;
            lastRow = curRow;
        }
        for (int x : lastRow) {
            if (x == 1) {
                return -1;
            }
        }
        return numFlips;
    }

    private void flipOneTile(int[] state, int j) {
        state[j] ^= 1;
        if (j > 0) {
            state[j - 1] ^= 1;
        }
        if (j + 1 < state.length) {
            state[j + 1] ^= 1;
        }
    }
}
// @lc code=end
