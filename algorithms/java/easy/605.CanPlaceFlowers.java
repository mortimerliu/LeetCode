/*
 * @lc app=leetcode id=605 lang=java
 *
 * [605] Can Place Flowers
 *
 * https://leetcode.com/problems/can-place-flowers/description/
 *
 * algorithms
 * Easy (32.89%)
 * Likes:    4931
 * Dislikes: 837
 * Total Accepted:    433.9K
 * Total Submissions: 1.3M
 * Testcase Example:  '[1,0,0,0,1]\n1'
 *
 * You have a long flowerbed in which some of the plots are planted, and some
 * are not. However, flowers cannot be planted in adjacent plots.
 * 
 * Given an integer array flowerbed containing 0's and 1's, where 0 means empty
 * and 1 means not empty, and an integer n, return true if n new flowers can be
 * planted in the flowerbed without violating the no-adjacent-flowers rule and
 * false otherwise.
 * 
 * 
 * Example 1:
 * Input: flowerbed = [1,0,0,0,1], n = 1
 * Output: true
 * Example 2:
 * Input: flowerbed = [1,0,0,0,1], n = 2
 * Output: false
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= flowerbed.length <= 2 * 10^4
 * flowerbed[i] is 0 or 1.
 * There are no two adjacent flowers in flowerbed.
 * 0 <= n <= flowerbed.length
 * 
 * 
 */

// @lc code=start
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int m = flowerbed.length;
        int left = -1;
        for (int i = 0; i <= m; i++) {
            if (i == m || flowerbed[i] == 1) {
                if (i == m) {
                    i++;
                }
                n -= (i - left - 1) / 2;
                left = i + 1;
                if (n <= 0) {
                    return true;
                }
            }
        }
        return false;
    }
}
// @lc code=end
