package algorithms.java;
/*
 * @lc app=leetcode id=79 lang=java
 *
 * [79] Word Search
 *
 * https://leetcode.com/problems/word-search/description/
 *
 * algorithms
 * Medium (39.76%)
 * Likes:    11589
 * Dislikes: 465
 * Total Accepted:    1.1M
 * Total Submissions: 2.9M
 * Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
 *
 * Given an m x n grid of characters board and a string word, return true if
 * word exists in the grid.
 * 
 * The word can be constructed from letters of sequentially adjacent cells,
 * where adjacent cells are horizontally or vertically neighboring. The same
 * letter cell may not be used more than once.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
 * = "ABCCED"
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
 * = "SEE"
 * Output: true
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
 * = "ABCB"
 * Output: false
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == board.length
 * n = board[i].length
 * 1 <= m, n <= 6
 * 1 <= word.length <= 15
 * board and word consists of only lowercase and uppercase English letters.
 * 
 * 
 * 
 * Follow up: Could you use search pruning to make your solution faster with a
 * larger board?
 * 
 */

// @lc code=start
class Solution {

    /**
     * backtracking
     * 
     * Time: O(N * L^3)
     * Space: O(L + N^2)
     */
    public boolean exist(char[][] board, String word) {
        boolean[][] visited = new boolean[board.length][board[0].length];

        for (int x = 0; x < board.length; x++) {
            for (int y = 0; y < board[0].length; y++) {
                if (search(board, word, x, y, 0, visited)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean search(char[][] board, String word, int x, int y, int i, boolean[][] visited) {
        if (i == word.length()) {
            return true;
        }
        if (x >= board.length || x < 0 || y >= board[0].length || y < 0 || board[x][y] != word.charAt(i)
                || visited[x][y]) {
            return false;
        }
        visited[x][y] = true;
        if (search(board, word, x - 1, y, i + 1, visited) || search(board, word, x + 1, y, i + 1, visited)
                || search(board, word, x, y - 1, i + 1, visited) || search(board, word, x, y + 1, i + 1, visited)) {
            return true;
        }
        visited[x][y] = false;
        return false;
    }
}
// @lc code=end
