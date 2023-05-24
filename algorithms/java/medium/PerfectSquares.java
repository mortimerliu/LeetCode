package algorithms.java.medium;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * [Medium] 279. Perfect Squares
 *
 * Given an integer n, return the least number of perfect square numbers that
 * sum to n.
 *
 * A perfect square is an integer that is the square of an integer; in other
 * words, it is the product of some integer with
 * itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are
 * not.
 *
 * Example 1:
 *
 * Input: n = 12
 * Output: 3
 * Explanation: 12 = 4 + 4 + 4.
 *
 * Example 2:
 *
 * Input: n = 13
 * Output: 2
 * Explanation: 13 = 4 + 9.
 *
 * Constraints:
 *
 * 1 <= n <= 104
 *
 * @author Hongru Liu
 */
class Solution1 {
    /**
     * @param n: the number to be divided
     * @return: the least number of perfect square numbers that sum to n
     */
    public int numSquares(int n) {
        ArrayList<Integer> squareNums = new ArrayList<>();
        int i = 1;
        while (i * i <= n) {
            squareNums.add(i * i);
            i++;
        }

        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int j = 1; j <= n; j++) {
            for (int k : squareNums) {
                if (j >= k) {
                    dp[j] = Math.min(dp[j], 1 + dp[j - k]);
                } else {
                    break;
                }
            }
        }

        return dp[n];
    }
}

class Solution2 {
    public int numSquares(int n) {
        Set<Integer> squareNums = new HashSet<>();
        for (int i = 1; i * i <= n; i++) {
            squareNums.add(i * i);
        }

        for (int count = 1; count <= n; count++) {
            if (isDividedBy(n, count, squareNums)) {
                return count;
            }
        }
        return n;
    }

    private boolean isDividedBy(int n, int count, Set<Integer> squareNums) {
        if (count == 1) {
            return squareNums.contains(n);
        }
        for (int k : squareNums) {
            if (k < n && isDividedBy(n - k, count - 1, squareNums)) {
                return true;
            }
        }
        return false;
    }
}

class Solution3 {
    public int numSquares(int n) {
        List<Integer> squareNums = new ArrayList<>();
        for (int i = 1; i * i <= n; i++) {
            squareNums.add(i * i);
        }

        // BFS
        Set<Integer> queue = new HashSet<>();
        queue.add(n);

        int level = 0;
        while (!queue.isEmpty()) {
            Set<Integer> newQueue = new HashSet<>();
            level++;
            for (int remainder : queue) {
                for (int k : squareNums) {
                    if (k == remainder) {
                        return level;
                    } else if (k < remainder) {
                        newQueue.add(remainder - k);
                    } else {
                        break;
                    }
                }
            }
            queue = newQueue;
        }
        return n;
    }
}
