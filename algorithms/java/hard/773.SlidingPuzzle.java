/*
 * @lc app=leetcode id=773 lang=java
 *
 * [773] Sliding Puzzle
 *
 * https://leetcode.com/problems/sliding-puzzle/description/
 *
 * algorithms
 * Hard (63.92%)
 * Likes:    1860
 * Dislikes: 47
 * Total Accepted:    85.2K
 * Total Submissions: 133K
 * Testcase Example:  '[[1,2,3],[4,0,5]]'
 *
 * On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty
 * square represented by 0. A move consists of choosing 0 and a 4-directionally
 * adjacent number and swapping it.
 *
 * The state of the board is solved if and only if the board is
 * [[1,2,3],[4,5,0]].
 *
 * Given the puzzle board board, return the least number of moves required so
 * that the state of the board is solved. If it is impossible for the state of
 * the board to be solved, return -1.
 *
 *
 * Example 1:
 *
 *
 * Input: board = [[1,2,3],[4,0,5]]
 * Output: 1
 * Explanation: Swap the 0 and the 5 in one move.
 *
 *
 * Example 2:
 *
 *
 * Input: board = [[1,2,3],[5,4,0]]
 * Output: -1
 * Explanation: No number of moves will make the board solved.
 *
 *
 * Example 3:
 *
 *
 * Input: board = [[4,1,2],[5,0,3]]
 * Output: 5
 * Explanation: 5 is the smallest number of moves that solves the board.
 * An example path:
 * After move 0: [[4,1,2],[5,0,3]]
 * After move 1: [[4,1,2],[0,5,3]]
 * After move 2: [[0,1,2],[4,5,3]]
 * After move 3: [[1,0,2],[4,5,3]]
 * After move 4: [[1,2,0],[4,5,3]]
 * After move 5: [[1,2,3],[4,5,0]]
 *
 *
 *
 * Constraints:
 *
 *
 * board.length == 2
 * board[i].length == 3
 * 0 <= board[i][j] <= 5
 * Each value board[i][j] is unique.
 *
 *
 */

// @lc code=start

import java.util.*;

class Solution {
    private static final int FINAL_STATE = 0b001010011100101000;
    private static final int[][] DIRS = { { 1, 3 }, { 0, 2, 4 }, { 1, 5 }, { 0, 4 }, { 1, 3, 5 }, { 2, 4 } };

    public int slidingPuzzle(int[][] board) {
        // Double-ended BFS
        int zeroIdx = -1;
        int currentState = 0;
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 3; j++) {
                currentState = (currentState << 3) | board[i][j];
                if (board[i][j] == 0) {
                    zeroIdx = 3 * i + j;
                }
            }
        }

        if (currentState == FINAL_STATE) {
            return 0;
        }

        Set<Integer> visited = new HashSet<>();
        Map<Integer, Integer> begin = new HashMap<>();
        begin.put(currentState, zeroIdx);
        visited.add(currentState);
        Map<Integer, Integer> end = new HashMap<>();
        end.put(FINAL_STATE, 5);
        visited.add(FINAL_STATE);
        int level = 0;

        while (!begin.isEmpty()) {
            if (begin.size() > end.size()) {
                Map<Integer, Integer> tmp = begin;
                begin = end;
                end = tmp;
            }
            level++;
            Map<Integer, Integer> next = new HashMap<>();
            for (Map.Entry<Integer, Integer> entry : begin.entrySet()) {
                int curState = entry.getKey();
                zeroIdx = entry.getValue();
                for (int destIdx : DIRS[zeroIdx]) {
                    int newState = swap(curState, zeroIdx, destIdx);
                    if (end.containsKey(newState)) {
                        return level;
                    }
                    if (visited.add(newState)) {
                        next.put(newState, destIdx);
                    }
                }
            }
            begin = next;
        }
        return -1;
    }

    private int swap(int state, int zeroIdex, int destIdx) {
        int mask = 0b111 << ((5 - destIdx) * 3);
        int num = state & mask;
        if (zeroIdex > destIdx) {
            // arithmetic shift
            num >>>= (zeroIdex - destIdx) * 3;
        } else {
            num <<= (destIdx - zeroIdex) * 3;
        }
        state &= ~mask;
        return state | num;
    }
}
// @lc code=end
