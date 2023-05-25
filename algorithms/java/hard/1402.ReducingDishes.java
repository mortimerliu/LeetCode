/*
 * @lc app=leetcode id=1402 lang=java
 *
 * [1402] Reducing Dishes
 *
 * https://leetcode.com/problems/reducing-dishes/description/
 *
 * algorithms
 * Hard (72.00%)
 * Likes:    2827
 * Dislikes: 283
 * Total Accepted:    112.4K
 * Total Submissions: 146.3K
 * Testcase Example:  '[-1,-8,0,5,-7]'
 *
 * A chef has collected data on the satisfaction level of his n dishes. Chef
 * can cook any dish in 1 unit of time.
 *
 * Like-time coefficient of a dish is defined as the time taken to cook that
 * dish including previous dishes multiplied by its satisfaction level i.e.
 * time[i] * satisfaction[i].
 *
 * Return the maximum sum of like-time coefficient that the chef can obtain
 * after dishes preparation.
 *
 * Dishes can be prepared in any order and the chef can discard some dishes to
 * get this maximum value.
 *
 *
 * Example 1:
 *
 *
 * Input: satisfaction = [-1,-8,0,5,-9]
 * Output: 14
 * Explanation: After Removing the second and last dish, the maximum total
 * like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
 * Each dish is prepared in one unit of time.
 *
 * Example 2:
 *
 *
 * Input: satisfaction = [4,3,2]
 * Output: 20
 * Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
 *
 *
 * Example 3:
 *
 *
 * Input: satisfaction = [-1,-4,-5]
 * Output: 0
 * Explanation: People do not like the dishes. No dish is prepared.
 *
 *
 *
 * Constraints:
 *
 *
 * n == satisfaction.length
 * 1 <= n <= 500
 * -1000 <= satisfaction[i] <= 1000
 *
 *
 */

// @lc code=start

import java.util.Arrays;

class Solution {
    public int maxSatisfaction(int[] satisfaction) {
        // greedy
        Arrays.sort(satisfaction);
        int ans = 0, sum = 0;
        for (int i = satisfaction.length - 1; i >= 0 && sum + satisfaction[i] >= 0; i--) {
            sum += satisfaction[i];
            ans += sum;
        }
        return ans;
    }
}
// @lc code=end
