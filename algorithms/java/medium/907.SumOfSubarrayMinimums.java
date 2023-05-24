/*
 * @lc app=leetcode id=907 lang=java
 *
 * [907] Sum of Subarray Minimums
 *
 * https://leetcode.com/problems/sum-of-subarray-minimums/description/
 *
 * algorithms
 * Medium (34.31%)
 * Likes:    6117
 * Dislikes: 415
 * Total Accepted:    145.9K
 * Total Submissions: 409K
 * Testcase Example:  '[3,1,2,4]'
 *
 * Given an array of integers arr, find the sum of min(b), where b ranges over
 * every (contiguous) subarray of arr. Since the answer may be large, return
 * the answer modulo 10^9 + 7.
 *
 *
 * Example 1:
 *
 *
 * Input: arr = [3,1,2,4]
 * Output: 17
 * Explanation:
 * Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4],
 * [3,1,2,4].
 * Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
 * Sum is 17.
 *
 *
 * Example 2:
 *
 *
 * Input: arr = [11,81,94,43,3]
 * Output: 444
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= arr.length <= 3 * 10^4
 * 1 <= arr[i] <= 3 * 10^4
 *
 *
 */

// @lc code=start

import java.util.*;

class Solution {
    public int sumSubarrayMins(int[] arr) {
        int MOD = 1000000007;
        Stack<Integer> stack = new Stack<>();
        // note the data type
        long ans = 0;
        for (int i = 0; i <= arr.length; i++) {
            while (!stack.isEmpty() && (i == arr.length || arr[i] < arr[stack.peek()])) {
                int j = stack.pop();
                int k = stack.isEmpty() ? -1 : stack.peek();
                // note the data type
                long count = (i - j) * (j - k) % MOD;
                ans += (count * arr[j]) % MOD;
                ans %= MOD;
            }
            stack.push(i);
        }
        return (int) (ans);
    }
}
// @lc code=end
